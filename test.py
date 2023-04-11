from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager
KV = '''
MDScreen:



    MDCard:
        MDLabel:
            size_hint: None,1
            width: 200
            text: 'Gender'

        MDSegmentedControl:
            adaptive_width: True
            pos_hint: {"center_x": .5, "center_y": .5}

            MDSegmentedControlItem:
                text: "Male"

            MDSegmentedControlItem:
                text: "Female"


'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


Example().run()