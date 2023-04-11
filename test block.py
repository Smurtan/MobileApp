from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
     pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('test.kv')


class MyApp(MDApp):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()
