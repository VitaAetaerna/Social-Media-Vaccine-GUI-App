from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from plyer import notification
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton
from kivymd.uix.button import MDIconButton
Window.size = (300, 500)

#ICONS https://gitlab.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py#L4

#KV FILE



Personal = '''
MDFillRoundFlatIconButton:
    text: "                           Private | Personal                    "
    icon: "information"
    pos: 0, 260
    size_hint_y: 0.15
    width:300
    height: 250
'''

School = '''
MDFillRoundFlatIconButton:
    text: "                                Public | School                     "
    icon: "school"
    pos: 0, 180
    size_hint_y: 0.15
    width:300
    height: 250
'''
Festival = '''
MDFillRoundFlatIconButton:
    text: "                           Public | Festival                       "
    icon: "microphone"
    pos: 0, 100
    size_hint_y: 0.15
    width:300
    height: 250
'''



#END

#DESIGN  (KV)
tbar = """
Screen:
    BoxLayout:
        MDBottomAppBar:
            MDTopAppBar:
                icon: "home"
                type: "bottom"
                left_action_items: [["human-male-female", lambda y: y]]
                right_action_items: [["account-settings", lambda y:y]]

"""


#END



class SaveItForLaterApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = '300'
        screen = Screen()


#TXT FIELDS
        self.school = Builder.load_string(School)
        self.festival = Builder.load_string(Festival)
        self.personal = Builder.load_string(Personal)
        self.Toolb = Builder.load_string(tbar)
#ADD TO WIDGETS
        screen.add_widget(self.school)
        screen.add_widget(self.festival)
        screen.add_widget(self.personal)

        screen.add_widget(self.Toolb)


        return screen

SaveItForLaterApp().run()
