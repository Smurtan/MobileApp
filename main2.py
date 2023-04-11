from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView
from kivymd.uix.button import MDRaisedButton


class MainWindow(Screen):
    pass


# class ProfileWindow(Screen):
#     pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('main.kv')


class MyApp(MDApp):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()
