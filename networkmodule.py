###################################################################################################
# Network

import app
import chr
import dbg
import net
import snd

import chr
import chrmgr
import background
import player
import playerSettingModule

import ui
import uiPhaseCurtain

import localeInfo

if app.__BL_MULTI_LANGUAGE__:
	import emotion
	import introCreate
	import introEmpire
	import serverInfo
	import textTail
	import uiAffectShower
	import uiCharacter
	import uiChat
	import uiDragonSoul
	import uiGuild
	import uiMapNameShower
	import uiParty
	import uiSelectMusic
	import uiScriptLocale
	import uiTarget
	import uiToolTip
	import struct
	import introHeader


class PopupDialog(ui.ScriptWindow):

	def __init__(self):
		print "NEW POPUP DIALOG ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.CloseEvent = 0

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE POPUP DIALOG "
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		PythonScriptLoader = ui.PythonScriptLoader()
		PythonScriptLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")

	def Open(self, Message, event = 0, ButtonName = localeInfo.UI_CANCEL):

		if True == self.IsShow():
			self.Close()

		self.Lock()
		self.SetTop()
		self.CloseEvent = event

		AcceptButton = self.GetChild("accept")
		AcceptButton.SetText(ButtonName)
		AcceptButton.SetEvent(ui.__mem_func__(self.Close))

		self.GetChild("message").SetText(Message)
		self.Show()

	def Close(self):
		if not self.IsShow():
			self.CloseEvent = 0
			return

		self.Unlock()
		self.Hide()

		if self.CloseEvent:
			self.CloseEvent()
			self.CloseEvent = 0

	@ui.WindowDestroy
	def Destroy(self):
		self.Close()
		self.ClearDictionary()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnIMEReturn(self):
		self.Close()
		return True

##
## Main Stream
##
class MainStream(ui.NoWindow):
	isChrData=0

	def __init__(self):
		print("NEWMAIN STREAM ----------------------------------------------------------------------------")
		net.SetHandler(self)
		net.SetTCPRecvBufferSize(128*1024)
		net.SetTCPSendBufferSize(4096)
		net.SetUDPRecvBufferSize(4096)

		self.id=""
		self.pwd=""
		self.addr=""
		self.port=0
		self.account_addr=0
		self.account_port=0
		self.slot=0
		self.isAutoSelect=0
		self.isAutoLogin=0

		self.curtain = 0
		self.curPhaseWindow = 0
		self.newPhaseWindow = 0

	def __del__(self):
		print("---------------------------------------------------------------------------- DELETE MAIN STREAM ")
		if ui.WOC_ENABLE_PRINT_DEL_DEBUG: import dbg; dbg.TraceError("{} __del__ called".format(self.__class__.__name__))

	def Hide(self):
		pass

	@ui.WindowDestroy
	def Destroy(self):
		if self.curPhaseWindow:
			self.curPhaseWindow.Close()
			self.curPhaseWindow = 0

		if self.newPhaseWindow:
			self.newPhaseWindow.Close()
			self.newPhaseWindow = 0

		if self.popupWindow:
			self.popupWindow.Destroy()
			self.popupWindow = 0

		self.curtain = 0
		if ui.WOC_ENABLE_PRINT_REGISTERS: #dump all the
			ui.WocDumpRegisters()

	def Create(self):
		self.CreatePopupDialog()

		self.curtain = uiPhaseCurtain.PhaseCurtain()

	def SetPhaseWindow(self, newPhaseWindow):
		if self.newPhaseWindow:
			self.__ChangePhaseWindow()

		self.newPhaseWindow=newPhaseWindow

		if self.curPhaseWindow:
			self.curtain.FadeOut(self.__ChangePhaseWindow)
		else:
			self.__ChangePhaseWindow()

	def __ChangePhaseWindow(self):
		oldPhaseWindow=self.curPhaseWindow
		newPhaseWindow=self.newPhaseWindow
		self.curPhaseWindow=0
		self.newPhaseWindow=0

		if oldPhaseWindow:
			oldPhaseWindow.Close()

		if newPhaseWindow:
			newPhaseWindow.Open()

		self.curPhaseWindow=newPhaseWindow

		if self.curPhaseWindow:
			self.curtain.FadeIn()
		else:
			app.Exit()

	def CreatePopupDialog(self):
		self.popupWindow = PopupDialog()
		self.popupWindow.LoadDialog()
		self.popupWindow.SetCenterPosition()
		self.popupWindow.Hide()


	## SelectPhase
	##########################################################################################
	def SetLogoPhase(self):
		net.Disconnect()

		import introLogo
		self.SetPhaseWindow(introLogo.LogoWindow(self))

	def SetLoginPhase(self):
		net.Disconnect()

		import introLogin
		self.SetPhaseWindow(introLogin.LoginWindow(self))

	def SetSelectEmpirePhase(self):
		try:
			import introEmpire
			self.SetPhaseWindow(introEmpire.SelectEmpireWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetSelectEmpirePhase")


	def SetReselectEmpirePhase(self):
		try:
			import introEmpire
			self.SetPhaseWindow(introEmpire.ReselectEmpireWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetReselectEmpirePhase")

	def SetSelectCharacterPhase(self):
		try:
			if app.__BL_MULTI_LANGUAGE__:
				import introSelect
				if app.GetReloadLocale():
					app.ReloadLocaConfig()

					localeInfo.ReloadLocaleFile()
					uiScriptLocale.ReloadLocaleFile()

					app.SetDefaultFontName(localeInfo.UI_DEF_FONT)
					textTail.Initialize()
					uiAffectShower.AffectShower.ReloadVariables()
					emotion.ReloadEmotionDict()
					introCreate.CreateCharacterWindow.ReloadVariables()
					introEmpire.SelectEmpireWindow.ReloadVariables()
					introSelect.SelectCharacterWindow.ReloadVariables()
					serverInfo.ReloadVariables()
					uiCharacter.CharacterWindow.ReloadVariables()
					uiChat.ChatLine.ReloadVariables()
					uiChat.ChatLogWindow.ReloadVariables()
					uiDragonSoul.DragonSoulWindow.ReloadVariables()
					uiGuild.GuildWindow.ReloadVariables()
					uiGuild.BuildGuildBuildingWindow.ReloadVariables()
					uiMapNameShower.MapNameShower.ReloadVariables()
					uiParty.PartyMemberInfoBoard.ReloadVariables()
					uiParty.PartyMenu.ReloadVariables()
					uiSelectMusic.ReloadVariables()
					uiTarget.TargetBoard.ReloadVariables()
					uiToolTip.ItemToolTip.ReloadVariables()
					uiToolTip.SkillToolTip.ReloadVariables()

					localeInfo.LoadLocaleData()
					app.SetReloadLocale(False)
				else:
					localeInfo.LoadLocaleData()
			else:
				localeInfo.LoadLocaleData()
				import introSelect
			self.popupWindow.Close()
			self.SetPhaseWindow(introSelect.SelectCharacterWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetSelectCharacterPhase")

	def SetCreateCharacterPhase(self):
		try:
			import introCreate
			self.SetPhaseWindow(introCreate.CreateCharacterWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetCreateCharacterPhase")

	def SetTestGamePhase(self, x, y):
		try:
			import introLoading
			loadingPhaseWindow=introLoading.LoadingWindow(self)
			loadingPhaseWindow.LoadData(x, y)
			self.SetPhaseWindow(loadingPhaseWindow)
		except:
			import exception
			exception.Abort("networkModule.SetLoadingPhase")



	def SetLoadingPhase(self):
		try:
			import introLoading
			self.SetPhaseWindow(introLoading.LoadingWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetLoadingPhase")

	def SetGamePhase(self):
		try:
			import game
			self.popupWindow.Close()
			self.SetPhaseWindow(game.GameWindow(self))
		except:
			raise
			import exception
			exception.Abort("networkModule.SetGamePhase")

	################################
	# Functions used in python

	## Login
	def Connect(self):
		import constInfo
		if constInfo.KEEP_ACCOUNT_CONNETION_ENABLE:
			net.ConnectToAccountServer(self.addr, self.port, self.account_addr, self.account_port)
		else:
			net.ConnectTCP(self.addr, self.port)

		#net.ConnectUDP(IP, Port)

	def SetConnectInfo(self, addr, port, account_addr=0, account_port=0):
		self.addr = addr
		self.port = port
		self.account_addr = account_addr
		self.account_port = account_port

	def GetConnectAddr(self):
		return self.addr

	def SetLoginInfo(self, id, pwd):
		self.id = id
		self.pwd = pwd
		net.SetLoginInfo(id, pwd)

	def CancelEnterGame(self):
		pass

	## Select
	def SetCharacterSlot(self, slot):
		self.slot=slot

	def GetCharacterSlot(self):
		return self.slot

	## Empty
	def EmptyFunction(self):
		pass

	def SendAttackPacket(self, vid):
		import net
		"""Send an attack command to the server using available APIs."""

		# Eğer net.SendAttackPacket fonksiyonu varsa onu kullan
		try:
			if hasattr(net, "SendAttackPacket"):
				net.SendAttackPacket(vid)
				return
		except AttributeError:
			return

		# Eğer net.Send fonksiyonu varsa onu kullan
		if hasattr(net, "Send"):
			try:
				import introHeader
				import struct
				net.Send(introHeader.HEADER_CG_ATTACK, struct.pack("I", vid))
			except Exception:
				pass


		# Otomatik Av sistemi için stream tanımı
stream = MainStream()



