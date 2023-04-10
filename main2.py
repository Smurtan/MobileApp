from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy_garden.mapview import MapView
from kivy.core.window import Window
Window.size = (310,580)

class MyApp(MDApp):
    def build(self):
        self.screen = Builder.load_file("main.kv")
        self.screen = Builder.load_file("profileuser.kv")
        self.screen = Builder.load_file("reviews.kv")
        return self.screen


MyApp().run()