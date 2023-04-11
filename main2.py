from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.pickers import MDTimePicker


class MyApp(MDApp):
    def build(self):
        self.screen_menu = ScreenManager()
        self.screen_menu.add_widget(Builder.load_file("home.kv"))
        self.screen_menu.add_widget(Builder.load_file("login.kv"))
        self.screen_menu.add_widget(Builder.load_file("signup.kv"))
        self.screen_menu.add_widget(Builder.load_file("inf_trip.kv"))
        self.screen_menu.add_widget(Builder.load_file("photo.kv"))
        self.screen_menu.add_widget(Builder.load_file("main.kv"))
        self.screen_menu.add_widget(Builder.load_file("Reviews.kv"))
        self.screen_menu.add_widget(Builder.load_file("ProfileScreen.kv"))
        return self.screen_menu

    def clear(self):
        self.root.ids.tel.text = ""
        self.root.ids.password.text = ""

    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()

    def get_time(self, instance, time):
        print(time)

    def schedule(self, *args):
        pass

MyApp().run()
