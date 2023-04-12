from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFloatingActionButton, MDIconButton, MDTextButton
from kivymd.uix.expansionpanel import MDExpansionPanelThreeLine
from kivymd.uix import scrollview
from kivymd.uix import gridlayout
from kivy.uix.button import Button
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


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
        i = 2
        print(i)
        self.manager.current = 'ProfileWindow'

    def changer2(self, *args):
        i = 1
        print(i)
        self.manager.current = 'TripFrom'


class TripFrom(Screen):
    def __init__(self, **kwargs):
        super(TripFrom, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("add_trip.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        self.my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                                 background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        screen1.add_widget(my_button1)
        screen1.add_widget(self.my_button2)
        self.a = MDLabel(text="Где собираемся?", font_size="20", pos_hint={"center_y": .97}, halign="center",
                         color=[34, 34, 34, 255])
        screen1.add_widget(self.a)
        self.add_widget(screen1)
        self.screen = screen1
        self.my_button2.bind(on_press=self.changer2)

    def changer1(self, *args):
        self.manager.current = 'MainWindow'

    def changer2(self, *args):
        self.manager.current = 'TripTo'


class TripTo(Screen):
    def __init__(self, **kwargs):
        super(TripTo, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("add_trip.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        self.my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                                 background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        screen1.add_widget(my_button1)
        screen1.add_widget(self.my_button2)
        self.a = MDLabel(text="Куда едем?", font_size="20", pos_hint={"center_y": .97}, halign="center",
                         color=[34, 34, 34, 255])
        screen1.add_widget(self.a)
        self.add_widget(screen1)
        self.my_button2.bind(on_press=self.changer2)

    def changer1(self, *args):
        self.manager.current = 'TripFrom'

    def changer2(self, *args):
        self.manager.current = 'InputTripInformation'


class InputTripInformation(Screen):
    def __init__(self, **kwargs):
        super(InputTripInformation, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("inf_trip.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer1)
        my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                            background_color=[0, 0, 0, 0])
        my_button2.bind(on_press=self.changer2)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'TripTo'

    def changer2(self, *args):
        self.manager.current = 'MainWindow'


class ProfileWindow(Screen):
    def __init__(self, **kwargs):
        super(ProfileWindow, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("ProfileScreen.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  theme_text_color="Custom", text_color=[50, 0, 255, 255])
        my_button2 = Button(
            text="Мои отзывы",
            font_size="24sp",
            size_hint=[.90, .1],
            pos_hint={"center_x": .5, "center_y": .43},
            background_color=[0, 0, 0, 0], )
        my_button4 = Button(font_size="24sp", size_hint=[.90, .1], pos_hint={"center_x": .5, "center_y": .17},
                            background_color=[0, 0, 0, 0])
        my_button3 = Button(font_size="24sp", size_hint=[.90, .1], pos_hint={"center_x": .5, "center_y": .30},
                            background_color=[0, 0, 0, 0])
        my_button5 = Button(font_size="24sp", size_hint=[.12, .15], pos_hint={"center_x": .5, "center_y": .85},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        my_button4.bind(on_press=self.changer4)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        screen1.add_widget(my_button3)
        screen1.add_widget(my_button4)
        screen1.add_widget(my_button5)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'MainWindow'

    def changer2(self, *args):
        self.manager.current = 'Reviews'

    def changer3(self, *args):
        self.manager.current = 'HistoryTrip'

    def changer4(self, *args):
        self.manager.current = "Settings"


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


class HistoryTrip(Screen):
    def __init__(self, **kwargs):
        super(HistoryTrip, self).__init__(**kwargs)
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


class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("setings.kv"))
        my_button1 = Button(font_size="24sp", size_hint=[.90, .1], pos_hint={"center_x": .5, "center_y": .43},
                            background_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp",
                            size_hint=[.90, .1],
                            pos_hint={"center_x": .5, "center_y": .3},
                            background_color=[0, 0, 0, 0])
        my_button3 = Button(font_size="24sp",
                            size_hint=[.3, .07],
                            pos_hint={"center_x": .5, "center_y": .17},
                            background_color=[0, 0, 0, 0])
        my_button4 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        my_button4.bind(on_press=self.changer4)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        screen1.add_widget(my_button3)
        screen1.add_widget(my_button4)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'DataChange'

    def changer2(self, *args):
        self.manager.current = 'PasswordChange'

    def changer3(self, *args):
        self.manager.current = 'MainWindow'

    def changer4(self, *args):
        self.manager.current = 'ProfileWindow'


class DataChange(Screen):
    def __init__(self, **kwargs):
        super(DataChange, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("dan.kv"))
        my_button1 = Button(font_size="24sp", size_hint=[.90, .1], pos_hint={"center_x": .5, "center_y": .43},
                            background_color=[0, 0, 0, 0])
        # my_button1.bind(on_press=self.changer1)
        my_button2 = Button(font_size="24sp", size_hint=[.90, .1], pos_hint={"center_x": .5, "center_y": .3},
                            background_color=[0, 0, 0, 0])
        my_button3 = Button(font_size="24sp", size_hint=[.90, .1], pos_hint={"center_x": .5, "center_y": .17},
                            background_color=[0, 0, 0, 0])
        my_button4 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        my_button4.bind(on_press=self.changer4)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        screen1.add_widget(my_button3)
        screen1.add_widget(my_button4)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'DataChange'

    def changer2(self, *args):
        self.manager.current = 'PhoneChange'

    def changer3(self, *args):
        self.manager.current = 'NameChange'

    def changer4(self, *args):
        self.manager.current = 'Settings'


class PasswordChange(Screen):
    def __init__(self, **kwargs):
        super(PasswordChange, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("password.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp", size_hint=[.1, .05],
                            pos_hint={"center_x": .5, "center_y": .05},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'Settings'

    def changer2(self, *args):
        self.manager.current = 'Settings'


class PhoneChange(Screen):
    def __init__(self, **kwargs):
        super(PhoneChange, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("phonenumber.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp", size_hint=[.1, .05],
                            pos_hint={"center_x": .5, "center_y": .05},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'DataChange'

    def changer2(self, *args):
        self.manager.current = 'DataChange'


class NameChange(Screen):
    def __init__(self, **kwargs):
        super(NameChange, self).__init__(**kwargs)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("name.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp", size_hint=[.1, .05],
                            pos_hint={"center_x": .5, "center_y": .05},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'DataChange'

    def changer2(self, *args):
        self.manager.current = 'DataChange'


class MyApp(MDApp):
    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = Home(name='Home')
        screen2 = Login(name='Login')
        screen3 = SignUp(name='SignUp')
        screen4 = MainWindow(name='MainWindow')
        screen5 = ProfileWindow(name='ProfileWindow')
        screen6 = Reviews(name='Reviews')
        screen7 = TripFrom(name='TripFrom')
        screen8 = TripTo(name='TripTo')
        screen9 = Settings(name='Settings')
        screen10 = DataChange(name='DataChange')
        screen11 = PasswordChange(name='PasswordChange')
        screen12 = HistoryTrip(name='HistoryTrip')
        screen13 = PhoneChange(name='PhoneChange')
        screen14 = NameChange(name='NameChange')
        screen15 = InputTripInformation(name='InputTripInformation')

        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        my_screenmanager.add_widget(screen3)
        my_screenmanager.add_widget(screen4)
        my_screenmanager.add_widget(screen5)
        my_screenmanager.add_widget(screen6)
        my_screenmanager.add_widget(screen7)
        my_screenmanager.add_widget(screen8)
        my_screenmanager.add_widget(screen9)
        my_screenmanager.add_widget(screen10)
        my_screenmanager.add_widget(screen11)
        my_screenmanager.add_widget(screen12)
        my_screenmanager.add_widget(screen13)
        my_screenmanager.add_widget(screen14)
        my_screenmanager.add_widget(screen15)

        return my_screenmanager


MyApp().run()
