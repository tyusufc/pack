import app
import os
import net
import mouseModule
import player
import snd
import localeInfo
import ui
import uiScriptLocale

class AutoBanQuizWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.answer = 0
		self.restSec = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "AutoBanQuiz.py")
		except:
			import exception
			exception.Abort("AutoBanQuiz.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild

			self.msgTexts = [
				GetObject("msg1"),
				GetObject("msg2"),
			]
			self.selButtons = [
				GetObject("select1"),
				GetObject("select2"),
				GetObject("select3"),
			]

			self.statusText = GetObject("status")
			self.answerButton = GetObject("answer")
			self.refreshButton = GetObject("refresh")
		except:
			import exception
			exception.Abort("AutoBanQuiz.LoadDialog.BindObject")

		self.selButtons[0].SAFE_SetEvent(self.__OnClickSelectButton0)
		self.selButtons[1].SAFE_SetEvent(self.__OnClickSelectButton1)
		self.selButtons[2].SAFE_SetEvent(self.__OnClickSelectButton2)

		self.answerButton.SAFE_SetEvent(self.__OnClickAnswerButton)
		self.refreshButton.SAFE_SetEvent(self.__OnClickRefreshButton)

	@ui.WindowDestroy
	def Destroy(self):
		self.ClearDictionary()

		self.msgTexts = []
		self.selButtons = []
		self.statusText = None
		self.answerButton = None
		self.refreshButton = None

	def Open(self, open, quiz, duration):
		srcLines = quiz.split("|")

		if len(srcLines) >= 5:
			msgLines = srcLines[:2]
			selLines = srcLines[2:]

			for msgText, msgLine in zip(self.msgTexts, msgLines):
				msgText.SetText(msgLine)

			for selButton, selLine in zip(self.selButtons, selLines):
				selButton.SetText(selLine)

		self.statusText.SetText("%s: %s" % (uiScriptLocale.AUTOBAN_QUIZ_REST_TIME, localeInfo.SecondToDHM(duration)))

		self.answer = 0
		self.endTime = app.GetTime() + duration

		for selectButton in self.selButtons:
			selectButton.SetUp()

		self.Show()
		self.Lock()

	def Close(self):
		self.Unlock()
		self.Hide()

	def Clear(self):
		pass

	def Refresh(self):
		pass

	def __OnClickSelectButton0(self):
		self.__Select(0)

	def __OnClickSelectButton1(self):
		self.__Select(1)

	def __OnClickSelectButton2(self):
		self.__Select(2)

	def __Select(self, index):
		for selectButton in self.selButtons:
			selectButton.SetUp()

		self.selButtons[index].Down()
		self.answer = index + 1

		print "autoban_select: %d" % (self.answer)

	def __OnClickAnswerButton(self):
		if self.answer:
			print "autoban_answer: %d" % (self.answer)
			net.SendChatPacket("/autoban_answer %d" % (self.answer))
			self.Close()
		else:
			print "autoban_noanswer"

	def __OnClickRefreshButton(self):
		print "autoban_refresh"
		net.SendChatPacket("/autoban_refresh")

	def OnPressEscapeKey(self):
		return True

	def OnUpdate(self):
		restTime = self.endTime - app.GetTime()
		if restTime < 0:
			restTime = 0

		self.statusText.SetText("%s: %s" % (uiScriptLocale.AUTOBAN_QUIZ_REST_TIME, localeInfo.SecondToDHM(restTime)))
