import uiScriptLocale
import app

QUEST_ICON_BACKGROUND = 'd:/ymir work/ui/game/quest/slot_base.sub'

SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
ICON_SLOT_FILE = "d:/ymir work/ui/public/Slot_Base.sub"
FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"
ROOT_PATH = "d:/ymir work/ui/game/windows/"

LOCALE_PATH = uiScriptLocale.WINDOWS_PATH

PATTERN_PATH = "d:/ymir work/ui/pattern/"
QUEST_BOARD_WINDOW_WIDTH	= 231
QUEST_BOARD_WINDOW_HEIGHT	= 340
QUEST_BOARD_PATTERN_Y_COUNT = 19
QUEST_BOARD_PATTERN_X_COUNT = 12

window = {
	"name" : "CharacterWindow",
	"style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - 361) / 2,

	"width" : 253,
	"height" : 405,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 253,
			"height" : 405,

			"children" :
			[
				{
					"name" : "Skill_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 238,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_SKILL, "all_align":"center" },
					),
				},
				{
					"name" : "Emoticon_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 238,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_ACTION, "all_align":"center" },
					),
				},
				{
					"name" : "Quest_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 238,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_QUEST, "all_align":"center" },
					),
				},

				## Tab Area
				{
					"name" : "TabControl",
					"type" : "window",

					"x" : 0,
					"y" : 371,

					"width" : 250,
					"height" : 31,

					"children" :
					(
						## Tab
						{
							"name" : "Tab_01",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : ROOT_PATH+"char_tab_01.sub",
						},
						{
							"name" : "Tab_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : ROOT_PATH+"char_tab_02.sub",
						},
						{
							"name" : "Tab_03",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : ROOT_PATH+"char_tab_03.sub",
						},
						{
							"name" : "Tab_04",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : ROOT_PATH+"char_tab_04.sub",
						},
						## RadioButton
						{
							"name" : "Tab_Button_01",
							"type" : "radio_button",

							"x" : 6,
							"y" : 5,

							"width" : 53,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_02",
							"type" : "radio_button",

							"x" : 61,
							"y" : 5,

							"width" : 67,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_03",
							"type" : "radio_button",

							"x" : 130,
							"y" : 5,

							"width" : 61,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_04",
							"type" : "radio_button",

							"x" : 192,
							"y" : 5,

							"width" : 55,
							"height" : 27,
						},
					),
				},

				## Page Area
				{
					"name" : "Character_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 253,
					"height" : 371,

					"children" :
					[

						## Title Area
						{
							"name" : "Character_TitleBar", "type" : "titlebar", "style" : ("attach",), "x" : 61, "y" : 7, "width" : 185, "color" : "red",
							"children" :
							(
								{ "name" : "TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_MAIN, "all_align":"center" },
							),
						},

						## Guild Name Slot
						{
							"name" : "Guild_Name_Slot",
							"type" : "image",
							"x" : 63,
							"y" :27+7,
							"image" : LARGE_VALUE_FILE,

							"children" :
							(
								{
									"name" : "Guild_Name",
									"type":"text",
									"text":"?? ??",
									"x":0,
									"y":0,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
									"all_align" : "center",
								},
							),
						},

						## Character Name Slot
						{
							"name" : "Character_Name_Slot",
							"type" : "image",
							"x" : 153,
							"y" :27+7,
							"image" : LARGE_VALUE_FILE,

							"children" :
							(
								{
									"name" : "Character_Name",
									"type":"text",
									"text":"??? ??",
									"x":0,
									"y":0,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
									"all_align" : "center",
								},
							),
						},

						## Lv_Exp_BackImg
						{ "name":"Lv_Exp_BackImg", "type":"image", "x":9, "y":60, "image":ROOT_PATH+"level_exp_info.sub" },

						{ "name":"Lv_ToolTip", "type":"button", "x":9, "y":60, "width" : 55, "height" : 25, },
						{ "name":"Exp_ToolTip", "type":"button", "x":61, "y":60, "width" : 180, "height" : 25, },

						## Lv
						{ "name":"Level_Value", "type":"text", "x":35, "y":84, "fontsize":"LARGE", "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },

						## EXP
						#{ "name":"Exp_Value", "type":"text", "x":165, "y":84, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },

						## EXP
						{
							"name":"Status_CurExp", "type":"window", "x":53+8, "y":84, "width":87, "height":42,
							"children" :
							(
								#{ "name":"Exp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_cur_exp.sub" },
								{ "name":"Exp_Value", "type":"text", "x":46, "y":0, "fontsize":"LARGE", "text":"2500000000", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },									),
						},


						{ "name" : "slash", "type":"text", "text":"/", "x":152, "y":87, "text_horizontal_align" : "center", },

						## REXP
						{
							"name":"Status_RestExp", "type":"window", "x":152, "y":84, "width":50, "height":20,
							"children" :
							(
								#{ "name":"RestExp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_last_exp.sub" },
								{ "name":"RestExp_Value", "type":"text", "x":46, "y":0, "fontsize":"LARGE", "text":"2500000000", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},

						## Face Slot
						{ "name" : "Face_Image", "type" : "image", "x" : 11, "y" : 11, "image" : "d:/ymir work/ui/game/windows/face_warrior.sub" },
						{ "name" : "Face_Slot", "type" : "image", "x" : 7, "y" : 7, "image" : FACE_SLOT_FILE, },

						## Passive Expanded Button
						{ "name":"passive_expanded_btn", "type" : "button", "x":166, "y":107, "default_image" : ROOT_PATH+"passive_expanded_button_01.sub", "over_image" : ROOT_PATH+"passive_expanded_button_02.sub", "down_image" : ROOT_PATH+"passive_expanded_button_03.sub", },

						## ??? ?? ??
						{ "name":"change_base_button",		"type" : "radio_button",	"x":8, "y":107, "default_image" : ROOT_PATH+"old_level_btn_03.sub", "over_image" : ROOT_PATH+"old_level_btn_03.sub", "down_image" : ROOT_PATH+"old_level_btn_01.sub", },
						{ "name":"change_conqueror_button",	"type" : "radio_button",	"x":87, "y":107, "default_image" : ROOT_PATH+"new_level_btn_03.sub", "over_image" : ROOT_PATH+"new_level_btn_03.sub", "down_image" : ROOT_PATH+"new_level_btn_01.sub", },

						## ?? ??
						{
							"name":"Status_Standard", "type":"window", "x":3, "y":125, "width":250, "height":250,
							"children" :
							[
								## ?? ?? ?
								{ "name":"Base_Info_bar", "type":"image", "x":6, "y":12-7, "image":ROOT_PATH+"base_info_bar.sub" },
								{ "name":"Char_Info_Status_img", "type" : "image", "x" : 12, "y" : 14-7, "image" : ROOT_PATH+"char_info_status_img.sub", },

								## ?? ?? ??
								{
									"name":"Status_Plus_Label",
									"type":"image",
									"x":191,
									"y":15-7,
									"image":ROOT_PATH+"char_info_status_plus_img.sub",
									"children" :
									[
										{ "name":"Status_Plus_Btn_Img", "type":"image", "x":19, "y":0, "image":ROOT_PATH+"char_info_status_value_img.sub", },
										{ "name":"Status_Plus_Value", "type":"text", "x":30, "y":0, "text":"270", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									],
								},

								## ?? ???
								{
									"name":"base_info", "type":"window", "x":0, "y":26, "width":150, "height":150,
									"children" :
									[
										## HTH
										{ "name":"HTH_Slot", "type":"image", "x":50, "y":0, "image":SMALL_VALUE_FILE },
										{ "name":"HTH_Value", "type":"text", "x":70, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"HTH_Plus", "type" : "button", "x":91, "y":3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## INT
										{ "name":"INT_Slot", "type":"image", "x":50, "y":31, "image":SMALL_VALUE_FILE },
										{ "name":"INT_Value", "type":"text", "x":70, "y":34, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"INT_Plus", "type" : "button", "x" : 91, "y" : 34, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## STR
										{ "name":"STR_Slot", "type":"image", "x":50, "y":62, "image":SMALL_VALUE_FILE },
										{ "name":"STR_Value", "type":"text", "x":70, "y":65, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"STR_Plus", "type" : "button", "x" : 91, "y" : 65, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## DEX
										{ "name":"DEX_Slot", "type":"image", "x":50, "y":93, "image":SMALL_VALUE_FILE },
										{ "name":"DEX_Value", "type":"text", "x":70, "y":96, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"DEX_Plus", "type" : "button", "x" : 91, "y" : 96, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## ????
										{ "name":"HTH_IMG", "type":"image",	"x":20, "y":-2, "image":ROOT_PATH+"char_info_con.sub" },
										{ "name":"INT_IMG", "type":"image",	"x":20, "y":29, "image":ROOT_PATH+"char_info_int.sub" },
										{ "name":"STR_IMG", "type":"image",	"x":20, "y":60, "image":ROOT_PATH+"char_info_str.sub" },
										{ "name":"DEX_IMG", "type":"image",	"x":20, "y":91, "image":ROOT_PATH+"char_info_dex.sub" },
									],
								},

								## ?? ???
								{
									"name":"sungma_info", "type":"window", "x":0, "y":26, "width":150, "height":150,
									"children" :
									[
										## SUNGMA_STR
										{ "name":"sungma_str_slot",	"type":"image",	"x":50, "y":0, "image":SMALL_VALUE_FILE },
										{ "name":"sungma_str_value","type":"text",	"x":70, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"sungma_str_plus",	"type":"button","x":91, "y":3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## SUNGMA_HP
										{ "name":"sungma_hp_slot",	"type":"image",	"x":50,	"y":31,	"image":SMALL_VALUE_FILE },
										{ "name":"sungma_hp_value", "type":"text",	"x":70,	"y":34,	"text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"sungma_hp_plus",	"type":"button","x":91,	"y":34,	"default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## SUNGMA_MOVE
										{ "name":"sungma_move_slot",	"type":"image", "x":50, "y":62, "image":SMALL_VALUE_FILE },
										{ "name":"sungma_move_value",	"type":"text", "x":70, "y":65, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"sungma_move_plus",	"type":"button", "x" : 91, "y" : 65, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## SUNGMA_IMMUNE
										{ "name":"sungma_immune_slot",	"type":"image", "x":50, "y":93, "image":SMALL_VALUE_FILE },
										{ "name":"sungma_immune_value",	"type":"text", "x":70, "y":96, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"sungma_immune_plus",	"type":"button", "x" : 91, "y" : 96, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },

										## ????
										{ "name":"SUNGMA_STR_IMG",		"type":"image",	"x":20,	"y":-2,	"image":ROOT_PATH+"char_info_sungma_str.sub" },
										{ "name":"SUNGMA_HP_IMG",		"type":"image",	"x":20,	"y":29,	"image":ROOT_PATH+"char_info_sungma_hp.sub" },
										{ "name":"SUNGMA_MOVE_IMG",		"type":"image",	"x":20,	"y":60,	"image":ROOT_PATH+"char_info_sungma_move.sub" },
										{ "name":"SUNGMA_IMMUNE_IMG",	"type":"image",	"x":20,	"y":91,"image":ROOT_PATH+"char_info_sungma_immune.sub" },
									],
								},

								## ???? ??
								{ "name":"HTH_Minus", "type" : "button", "x":7, "y":36-7, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								{ "name":"INT_Minus", "type" : "button", "x":7, "y":67-7, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								{ "name":"STR_Minus", "type" : "button", "x":7, "y":98-7, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								{ "name":"DEX_Minus", "type" : "button", "x":7, "y":129-7, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },


								## ???,???,???,???
								{ "name":"HEL_IMG",	"type":"image",	"x":118, "y":31-7, "image":ROOT_PATH+"char_info_hp.sub" },
								{ "name":"SP_IMG",	"type":"image",	"x":118, "y":62-7, "image":ROOT_PATH+"char_info_sp.sub" },
								{ "name":"ATT_IMG",	"type":"image",	"x":118, "y":93-7, "image":ROOT_PATH+"char_info_att.sub" },
								{ "name":"DEF_IMG",	"type":"image",	"x":118, "y":124-7, "image":ROOT_PATH+"char_info_def.sub" },

								####

								## HP
								{
									"name":"HEL_Label", "type":"window", "x":145, "y":33-7, "width":50, "height":20,
									"children" :
									[
										{ "name":"HP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"HP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									]
								},
								## SP
								{
									"name":"SP_Label", "type":"window", "x":145, "y":64-7, "width":50, "height":20,
									"children" :
									[
										{ "name":"SP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"SP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									]
								},
								## ATT
								{
									"name":"ATT_Label", "type":"window", "x":145, "y":95-7, "width":50, "height":20,
									"children" :
									[
										{ "name":"ATT_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"ATT_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									]
								},
								## DEF
								{
									"name":"DEF_Label", "type":"window", "x":145, "y":126-7, "width":50, "height":20,
									"children" :
									[
										{ "name":"DEF_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"DEF_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									]
								},
							],
						},

						## ?? ??
						{
							"name":"Status_Extent", "type":"window", "x":3, "y":270, "width":253, "height":125,
							"children" :
							(
								## ?? ?? ??
								#{ "name":"Status_Extent_Bar", "type":"horizontalbar", "x":12, "y":0, "width":223, },
								{ "name":"Status_Extent_Label", "type" : "image", "x" : 13, "y" : 0, "image" : ROOT_PATH+"status_extent_bar.sub", },


								{ "name":"MSPD_IMG", "type":"image", "x":20, "y":31 - 25, "image":ROOT_PATH+"char_info_movespeed.sub" },
								{ "name":"ASPD_IMG", "type":"image", "x":20, "y":62 - 25, "image":ROOT_PATH+"char_info_attspeed.sub" },
								{ "name":"CSPD_IMG", "type":"image", "x":20, "y":93 - 25, "image":ROOT_PATH+"char_info_magspeed.sub" },
								{ "name":"MATT_IMG", "type":"image", "x":118, "y":31 - 25, "image":ROOT_PATH+"char_info_magatt.sub" },
								{ "name":"MDEF_IMG", "type":"image", "x":118, "y":62 - 25, "image":ROOT_PATH+"char_info_magdef.sub" },
								{ "name":"ER_IMG", "type":"image", "x":118, "y":93 - 25, "image":ROOT_PATH+"char_info_hitpct.sub" },


								## ?? ?? ??? ???
								#{"name":"Status_Extent_ItemList1", "type" : "image", "x":11, "y":31, "image" : LOCALE_PATH+"label_ext_item1.sub", },
								#{"name":"Status_Extent_ItemList2", "type" : "image", "x":128, "y":32, "image" : LOCALE_PATH+"label_ext_item2.sub", },

								## MSPD - ?? ??
								{
									"name":"MOV_Label", "type":"window", "x":50, "y":33 - 25, "width":50, "height":20,
									"children" :
									(
										{ "name":"MSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## ASPD - ?? ??
								{
									"name":"ASPD_Label", "type":"window", "x":50, "y":64 - 25, "width":50, "height":20,
									"children" :
									(
										{ "name":"ASPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"ASPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## CSPD - ?? ??
								{
									"name":"CSPD_Label", "type":"window", "x":50, "y":95 - 25, "width":50, "height":20,
									"children" :
									(
										{ "name":"CSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"CSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## MATT - ?? ???
								{
									"name":"MATT_Label", "type":"window", "x":148, "y":33 - 25, "width":50, "height":20,
									"children" :
									(
										{ "name":"MATT_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MATT_Value", "type":"text", "x":26, "y":3, "text":"999-999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## MDEF - ?? ???
								{
									"name":"MDEF_Label", "type":"window", "x":148, "y":64 - 25, "width":50, "height":20,
									"children" :
									(
										{ "name":"MDEF_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MDEF_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## ???
								{
									"name":"ER_Label", "type":"window", "x":148, "y":95 - 25, "width":50, "height":20,
									"children" :
									(
										{ "name":"ER_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"ER_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

							),
						},
					],
				},
				{
					"name" : "Skill_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 250,
					"height" : 350,

					"children" :
					(

						{
							"name":"Skill_Active_Title_Bar", "type":"horizontalbar", "x":15, "y":9, "width":223,

							"children" :
							(
								{
									"name":"Active_Skill_Point_Label",
									"type":"image",
									"x":180,
									"y":3,
									"image":ROOT_PATH+"char_info_status_plus_img.sub",
									"children" :
									(
										{ "name":"Active_Skill_Plus_Img", "type":"image", "x":13, "y":0, "image":ROOT_PATH+"char_info_status_value_img.sub", },
										{ "name":"Active_Skill_Point_Value", "type":"text", "x":25, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},

								## Group Button
								{
									"name" : "Skill_Group_Button_1",
									"type" : "radio_button",

									"x" : 5,
									"y" : 2,

									"text" : "Group1",
									"text_color" : 0xFFFFE3AD,

									"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
								},

								{
									"name" : "Skill_Group_Button_2",
									"type" : "radio_button",

									"x" : 50,
									"y" : 2,

									"text" : "Group2",
									"text_color" : 0xFFFFE3AD,

									"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
								},

								{
									"name" : "Active_Skill_Group_Name",
									"type" : "text",

									"x" : 7,
									"y" : 1,
									"text" : "Active",

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"color" : 0xFFFFE3AD,
								},

							),
						},

						{
							"name":"Skill_ETC_Title_Bar", "type":"horizontalbar", "x":15, "y":200+22, "width":223,
							"children" :
							(
								## Support_skill_Tooltip_icon
								## ?? ?? ??
								{
									"name":"Support_Skill_Point_Label",
									"type":"image",
									"x":180,
									"y":3,
									"image":ROOT_PATH+"char_info_status_plus_img.sub",
									"children" :
									(
										{ "name":"Support_Skill_Plus_Img", "type":"image", "x":13, "y":0, "image":ROOT_PATH+"char_info_status_value_img.sub", },
										{ "name":"Support_Skill_Point_Value", "type":"text", "x":25, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},
								## ???? ??
								{ "name":"Support_Skill_ToolTip", "type":"image", "x":3, "y":3, "image":ROOT_PATH+"support_skill_bar_icon.sub", },
							),
						},

						{ "name":"Skill_Board", "type":"image", "x":13, "y":30, "image":"d:/ymir work/ui/game/windows/skill_board.sub", },
						{ "name":"Skill_Board_expanded", "type":"image", "x":13, "y":179, "image":"d:/ymir work/ui/game/windows/skill_board_expanded.sub", },

						## Active Slot
						{
							"name" : "Skill_Active_Slot",
							"type" : "slot",

							"x" : 0 + 16,
							"y" : 0 + 15 + 15,

							"width" : 223,
							"height" : 190,
							"image" : ICON_SLOT_FILE,

							"slot" :	(
											{"index": 1, "x": 1, "y":  4, "width":32, "height":32},
											{"index":21, "x":38, "y":  4, "width":32, "height":32},
											{"index":41, "x":75, "y":  4, "width":32, "height":32},

											{"index": 3, "x": 1, "y": 40, "width":32, "height":32},
											{"index":23, "x":38, "y": 40, "width":32, "height":32},
											{"index":43, "x":75, "y": 40, "width":32, "height":32},

											{"index": 5, "x": 1, "y": 76, "width":32, "height":32},
											{"index":25, "x":38, "y": 76, "width":32, "height":32},
											{"index":45, "x":75, "y": 76, "width":32, "height":32},

											{"index": 7, "x": 1, "y":112, "width":32, "height":32},
											{"index":27, "x":38, "y":112, "width":32, "height":32},
											{"index":47, "x":75, "y":112, "width":32, "height":32},

											{"index": 9, "x": 1, "y":151, "width":32, "height":32},
											{"index":29, "x":38, "y":151, "width":32, "height":32},
											{"index":49, "x":75, "y":151, "width":32, "height":32},

											####

											{"index": 2, "x":113, "y":  4, "width":32, "height":32},
											{"index":22, "x":150, "y":  4, "width":32, "height":32},
											{"index":42, "x":187, "y":  4, "width":32, "height":32},

											{"index": 4, "x":113, "y": 40, "width":32, "height":32},
											{"index":24, "x":150, "y": 40, "width":32, "height":32},
											{"index":44, "x":187, "y": 40, "width":32, "height":32},

											{"index": 6, "x":113, "y": 76, "width":32, "height":32},
											{"index":26, "x":150, "y": 76, "width":32, "height":32},
											{"index":46, "x":187, "y": 76, "width":32, "height":32},

											{"index": 8, "x":113, "y":112, "width":32, "height":32},
											{"index":28, "x":150, "y":112, "width":32, "height":32},
											{"index":48, "x":187, "y":112, "width":32, "height":32},
										),
						},

						## ETC Slot
						{
							"name" : "Skill_ETC_Slot",
							"type" : "grid_table",
							"x" : 18,
							"y" : 221 + 22,
							"start_index" : 101,
							"x_count" : 6,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 5,
							"y_blank" : 4,
							"image" : ICON_SLOT_FILE,
						},

					),
				},
			],
		},
	),
}

window["children"][0]["children"] = window["children"][0]["children"] + [
{
	"name" : "Quest_Page",
	"type" : "window",
	"style" : ("attach",),

	"x" : 0,
	"y" : 24,

	"width" : 250,
	"height" : QUEST_BOARD_WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "Quest_Slot",
			"type" : "grid_table",
			"x" : 18,
			"y" : 20,
			"start_index" : 0,
			"x_count" : 1,
			"y_count" : 5,
			"x_step" : 32,
			"y_step" : 32,
			"y_blank" : 28,
			"image" : QUEST_ICON_BACKGROUND,
		},

		{
			"name" : "Quest_ScrollBar",
			"type" : "scrollbar",

			"x" : 25,
			"y" : 12,
			"size" : 290,
			"horizontal_align" : "right",
		},

		{ "name" : "Quest_Name_00", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 14 },
		{ "name" : "Quest_LastTime_00", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 30 },
		{ "name" : "Quest_LastCount_00", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 46 },

		{ "name" : "Quest_Name_01", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 74 },
		{ "name" : "Quest_LastTime_01", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 90 },
		{ "name" : "Quest_LastCount_01", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 106 },

		{ "name" : "Quest_Name_02", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 134 },
		{ "name" : "Quest_LastTime_02", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 150 },
		{ "name" : "Quest_LastCount_02", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 166 },

		{ "name" : "Quest_Name_03", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 194 },
		{ "name" : "Quest_LastTime_03", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 210 },
		{ "name" : "Quest_LastCount_03", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 226 },

		{ "name" : "Quest_Name_04", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 254 },
		{ "name" : "Quest_LastTime_04", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 270 },
		{ "name" : "Quest_LastCount_04", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 286 },
	),
},]

window["children"][0]["children"] = window["children"][0]["children"] + [
{
	"name" : "Emoticon_Page",
	"type" : "window",
	"style" : ("attach",),

	"x" : 0,
	"y" : 24,

	"width" : 250,
	"height" : 350,

	"children" :
	[
		## ?? ?? ??
		{ "name":"Action_Bar", "type":"horizontalbar", "x":12, "y":11+7, "width":223, },
		{ "name":"Action_Bar_Img", "type":"image", "x":15, "y":19, "image":ROOT_PATH+"action_bar_img.sub", },

		## Basis Action Slot
		{
			"name" : "SoloEmotionSlot",
			"type" : "grid_table",
			"x" : 15,
			"y" : 33+7,
			"horizontal_align" : "center",
			"start_index" : 1,
			"x_count" : 6,
			"y_count" : 3,
			"x_step" : 32,
			"y_step" : 32,
			"x_blank" : 5,
			"y_blank" : 10,
			"image" : ICON_SLOT_FILE,
		},

		## ?? ?? ??
		{ "name":"Reaction_Bar", "type":"horizontalbar", "x":12, "y":8+130+26, "width":223, },
		{ "name":"Reaction_Bar_Img", "type":"image", "x":15, "y":10+130+25, "image":ROOT_PATH+"reaction_bar_img.sub", },

		## ?? ?? ??
		{
			"name" : "DualEmotionSlot",
			"type" : "grid_table",
			"x" : 15,
			"y" : 160+25,
			"start_index" : 51,
			"x_count" : 6,
			"y_count" : 1,
			"x_step" : 32,
			"y_step" : 32,
			"x_blank" : 5,
			"y_blank" : 10,
			"image" : ICON_SLOT_FILE,
		},

		## ?? ?? ??
		{ "name":"Special_Action_Bar", "type":"horizontalbar", "x":12, "y":8+190+25, "width":223, },
		{ "name":"Special_Action_Bar_Img", "type":"image", "x":15, "y":10+190+24, "image":ROOT_PATH+"special_action_bar_img.sub", },

		## ?? ?? ??
		{
			"name" : "SpecialEmotionSlot",
			"type" : "grid_table",

			"x" : 15,
			"y" : 220+25,
			"start_index" : 0,#app.SPECIAL_ACTION_START_INDEX,
			"x_count" : 6,
			"y_count" : 2,
			"x_step" : 32,
			"y_step" : 32,
			"x_blank" : 5,
			"y_blank" : 10,
			"image" : ICON_SLOT_FILE,
		},
	],
},]