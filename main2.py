from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager


class MyApp(MDApp):
    def build(self):
        self.screen_menu = ScreenManager()
        self.screen_menu.add_widget(Builder.load_file("home.kv"))
        self.screen_menu.add_widget(Builder.load_file("login.kv"))
        self.screen_menu.add_widget(Builder.load_file("signup.kv"))
        self.screen_menu.add_widget(Builder.load_file("main.kv"))
        self.screen_menu.add_widget(Builder.load_file("Reviews.kv"))
        self.screen_menu.add_widget(Builder.load_file("ProfileScreen.kv"))
        return self.screen_menu


MyApp().run()
