from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (310, 580)

class Slope(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        return screen_manager

if __name__=="__main__":
    Slope().run()
    # LabelBase.register(name="MPoppins", fn_regular="C:\\Users\\Пользователь\\PycharmProjects\\MobileApp"
    #                    "-Medium.ttf")
    # LabelBase.register(name="BPoppins", fn_regular="C:\\Users\\Пользователь\\PycharmProjects\\MobileApp"
    #                    "-SemiBold.ttf")
