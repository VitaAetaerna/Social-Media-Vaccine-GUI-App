from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatIconButton, MDIconButton
from kivymd.app import MDApp
Window.size = (300,500)

#ICONS https://gitlab.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py#L4

TaskField1 = """
MDTextField:
    hint_text: "Enter task 3"
    icon_right: "calendar-clock"
    icon_right_color: app.theme_cls.primary_color
    pos: 0, 300
    size_hint_x:None
    width:300
"""

BottomBar = '''
MDBoxLayout:
    md_bg_color: "#1E1E15"

    # Will always be at the bottom of the screen.
    MDBottomAppBar:
        MDTopAppBar:
            icon: "home"
            type: "bottom"
            left_action_items: [["human-male-female", lambda y: y]]
            right_action_items: [["account-settings", lambda y:y]]

'''




class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.field1 = Builder.load_string(TaskField1)
        screen.add_widget(self.field1)
        
        self.bbar = Builder.load_string(BottomBar)
        screen.add_widget(self.bbar)

        return screen
Example().run()
