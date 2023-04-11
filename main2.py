from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFloatingActionButton, MDIconButton, MDTextButton
from kivymd.uix.expansionpanel import MDExpansionPanelThreeLine
from kivymd.uix import scrollview
from kivymd.uix import gridlayout
from kivy.uix.button import Button
from kivymd.uix.floatlayout import MDFloatLayout


class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("home.kv"))
        my_button1 = Button(size_hint=[.66, .065], pos_hint={"center_x": .5, "center_y": .19},
                            background_color=[0, 0, 0, 0])
        my_button2 = Button(size_hint=[.66, .065], pos_hint={"center_x": .5, "center_y": .09},
                            background_color=[0, 0, 0, 0])

        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)

        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'Login'

    def changer2(self, *args):
        self.manager.current = 'SignUp'


class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("login.kv"))
        my_button1 = Button(size_hint=[.66, .065], pos_hint={"center_x": .5, "center_y": .34},
                            background_color=[0, 0, 0, 0])
        my_button2 = MDTextButton(font_size="11sp", pos_hint={"center_x": .68, "center_y": .04},
                                  color=[52, 0, 231, 255])
        my_button3 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        screen1.add_widget(my_button3)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'MainWindow'

    def changer2(self, *args):
        self.manager.current = 'SignUp'

    def changer3(self, *args):
        self.manager.current = 'Home'


class SignUp(Screen):
    def __init__(self, **kwargs):
        super(SignUp, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("SignUp.kv"))
        my_button1 = Button(size_hint=[.66, .065], pos_hint={"center_x": .5, "center_y": .34},
                            background_color=[0, 0, 0, 0])
        my_button2 = MDTextButton(font_size="11sp", pos_hint={"center_x": .64, "center_y": .04})
        my_button3 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        screen1.add_widget(my_button3)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'MainWindow'

    def changer2(self, *args):
        self.manager.current = 'Login'

    def changer3(self, *args):
        self.manager.current = 'Home'


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("main.kv"))
        my_button1 = MDFloatingActionButton(icon="git", elevation_normal=12, pos_hint={"center_x": .9, "center_y": .95},
                                            size_hint=(None, None), segment_panel_height="56dp")

        my_button2 = MDFloatingActionButton(icon="plus", elevation_normal=12, pos_hint={"center_x": .5, "center_y": .1})

        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)

        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'ProfileWindow'

    def changer2(self, *args):
        self.manager.current = 'AddTrip'


class AddTrip(Screen):
    def __init__(self, **kwargs):
        super(AddTrip, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("add_trip.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer)
        screen1.add_widget(my_button1)
        self.add_widget(screen1)

    def changer(self, *args):
        self.manager.current = 'MainWindow'


class ProfileWindow(Screen):
    def __init__(self, **kwargs):
        super(ProfileWindow, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("ProfileScreen.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  theme_text_color="Custom", text_color=[50, 0, 255, 255])
        my_button1.bind(on_press=self.changer1)
        my_button2 = Button(
            text="Мои отзывы",
            font_size="24sp",
            size_hint=[.90, .1],
            pos_hint={"center_x": .5, "center_y": .43},
            background_color=[0, 0, 0, 0], )
        my_button2.bind(on_press=self.changer2)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'MainWindow'

    def changer2(self, *args):
        self.manager.current = 'Reviews'


class Reviews(Screen):
    def __init__(self, **kwargs):
        super(Reviews, self).__init__(**kwargs)
        screen1 = Screen()
        widget_grid_layout = scrollview.MDScrollView(gridlayout.MDGridLayout(id="box", cols=1, adaptive_height=True))
        for i in range(10):
            widget_grid_layout.ids.box.add_widget(MDExpansionPanelThreeLine(
                text="Text",
                secondary_text="Secondary text",
                tertiary_text="Tertiary text",
            ))
        screen1.add_widget(widget_grid_layout)
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer)
        screen1.add_widget(my_button1)
        self.add_widget(screen1)

    def changer(self, *args):
        self.manager.current = 'ProfileWindow'


class MyApp(MDApp):
    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = Home(name='Home')
        screen2 = Login(name='Login')
        screen3 = SignUp(name='SignUp')
        screen4 = MainWindow(name='MainWindow')
        screen5 = ProfileWindow(name='ProfileWindow')
        screen6 = Reviews(name='Reviews')
        screen7 = AddTrip(name='AddTrip')

        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        my_screenmanager.add_widget(screen3)
        my_screenmanager.add_widget(screen4)
        my_screenmanager.add_widget(screen5)
        my_screenmanager.add_widget(screen6)
        my_screenmanager.add_widget(screen7)
        return my_screenmanager


MyApp().run()
