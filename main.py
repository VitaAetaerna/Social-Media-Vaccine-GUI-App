from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton
from kivymd.uix.button import MDIconButton
import random
Window.size = (300, 500)
#https://gitlab.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py#L4
#https://kivymd.readthedocs.io/en/latest/
tbar = ''' 
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "green"
        text_color_active: "white"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Groups'
            icon: 'group'
            badge_icon: "numeric-1"

            
            MDIconButton:
                icon: "account-switch"
                pos: 250, 380
                md_bg_color: app.theme_cls.primary_color
                
                
            MDFillRoundFlatIconButton:
                text: "                           Your Groups                             "
                icon: "human-greeting"
                pos: 0, 285
                size_hint_y: 0.15
                width:300
                height: 250

            MDFillRoundFlatIconButton:
                text: "                           Private | Personal                    "
                icon: "information"
                pos: 0, 205
                size_hint_y: 0.15
                width:300
                height: 250

            MDFillRoundFlatIconButton:
                text: "                                Public | School                     "
                icon: "school"
                pos: 0, 125
                size_hint_y: 0.15
                width:300
                height: 250

            MDFillRoundFlatIconButton:
                text: "                           Public | Festival                       "
                icon: "microphone"
                pos: 0, 35
                size_hint_y: 0.15
                width:300
                height: 250

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Join Group'
            icon: 'reply'


            MDFillRoundFlatIconButton:
                text: "          Create New Group                          "
                icon: "creation"
                pos: 10, 300
                size_hint_y: 0.1

            MDFillRoundFlatIconButton:
                text: "          Delete Group                                     "
                icon: "delete-sweep"
                pos: 10, 235
                size_hint_y: 0.1
            
            MDTextField:
                mode: "round"
                max_text_length: 4
                line_color_focus: "green"
                helper_text: "Enter a Code to join a Group"
                helper_text_mode: "persistent"
                hint_text: "Enter Group Code "
                icon_right: "key"
                icon_right_color: app.theme_cls.primary_color
                pos: 0, 175
                size_hint_x:None
                width:300

            MDFillRoundFlatIconButton:
                text: "          join          "
                icon: "inbox"
                pos: 85, 110
                size_hint_y: 0.1



        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Settings'
            icon: 'account-settings'

            MDTextField:
                mode: "round"
                max_text_length: 15
                line_color_focus: "green"
                helper_text: "Username"
                helper_text_mode: "persistent"
                hint_text: "Enter new Name"
                icon_right: "account"
                icon_right_color: app.theme_cls.primary_color
                pos: 0, 200
                size_hint_x:None
                width:300

            MDTextField:
                mode: "round"
                max_text_length: 15
                line_color_focus: "green"
                helper_text: "Password"
                helper_text_mode: "persistent"
                hint_text: "Enter new Password"
                icon_right: "key"
                icon_right_color: app.theme_cls.primary_color
                pos: 0, 135
                size_hint_x:None
                width:300

            MDFillRoundFlatIconButton:
                text: "        Delete Account                                    "
                md_bg_color: "red"
                icon: "delete-forever"
                pos: 10, 15
                size_hint_y: 0.1
                on_press: app.stop()

            MDFillRoundFlatIconButton:
                text: "        Dark/Light Mode                                 "
                icon: "theme-light-dark"
                icon_color: "white"
                pos: 10, 265
                size_hint_y: 0.1
                md_bg_color: "black"
                theme_text_color: "Custom"
                text_color: "white"
                on_release: self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
            

                
            MDFillRoundFlatIconButton:
                text: "        Read AGB                                                "
                icon: "book-open"
                pos: 10, 345 
                size_hint_y: 0.1

            MDFillRoundFlatIconButton:
                text: "        Clear My Data                                       "
                md_bg_color: "red"
                icon: "database"
                pos: 10, 70
                size_hint_y: 0.1
        
'''


#END



class VaccineApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = '300'
        screen = Screen()




        self.Toolb = Builder.load_string(tbar)
        screen.add_widget(self.Toolb)
        

        return screen


VaccineApp().run()
