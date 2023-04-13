from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFloatingActionButton, MDIconButton, MDTextButton
from kivymd.uix.expansionpanel import MDExpansionPanelThreeLine, MDExpansionPanelTwoLine
from kivymd.uix import scrollview
from kivymd.uix import gridlayout
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
import os
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivymd.toast import toast

from server.client import Client

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
        self.manager.transition.direction = "left"
        self.manager.current = 'Login'

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = 'SignUp'


class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("login.kv"))
        self.screen1 = Builder.load_file("login.kv")
        my_button1 = Button(size_hint=[.66, .065], pos_hint={"center_x": .5, "center_y": .34},
                            background_color=[0, 0, 0, 0])
        my_button2 = MDTextButton(font_size="11sp", pos_hint={"center_x": .68, "center_y": .04},
                                  color=[52, 0, 231, 255])
        my_button3 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button4 = MDTextButton(font_size="12sp", pos_hint={"center_x": .5, "center_y": .28})
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.screen1.add_widget(my_button3)
        self.screen1.add_widget(my_button4)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        user = client.login(
            self.screen1.ids.phone.text,
            self.screen1.ids.password.text
        )
        # self.screen1.ids.phone.text = ''
        # self.screen1.ids.password.text = ''
        print(self.screen1.ids.phone.text)
        print(self.screen1.ids.password.text)

        if user:
            global USER
            USER = user
            scrMan.add_widget(MainWindow(name="MainWindow"))
            scrMan.remove_widget(self)
        else:
            self.screen1.ids.phone.text = ''
            self.screen1.ids.password.text = ''

    def changer2(self, *args):
        self.manager.current = 'SignUp'

    def changer3(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Home(name="Home"))
        scrMan.remove_widget(self)


class SignUp(Screen):
    def __init__(self, **kwargs):
        super(SignUp, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("SignUp.kv"))
        self.screen1 = Builder.load_file("SignUp.kv")
        my_button1 = Button(size_hint=[.66, .065], pos_hint={"center_x": .5, "center_y": .18},
                            background_color=[0, 0, 0, 0])
        my_button2 = MDTextButton(font_size="11sp", pos_hint={"center_x": .64, "center_y": .04})
        my_button3 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button4 = MDTextButton(font_size="12sp", pos_hint={"center_x": .5, "center_y": .12})
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        my_button4.bind(on_press=self.changer4)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.screen1.add_widget(my_button3)
        self.screen1.add_widget(my_button4)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        user = client.registration(
            self.screen1.ids.surname.text,
            self.screen1.ids.name.text,
            self.screen1.ids.second_name.text,
            self.screen1.ids.password.text,
            self.screen1.ids.phone.text
        )
        # self.screen1.ids.surname.text = ''
        # self.screen1.ids.name.text = ''
        # self.screen1.ids.second_name.text = ''
        # self.screen1.ids.phone.text = ''
        # self.screen1.ids.password.text = ''
        print(self.screen1.ids.surname.text)
        print(self.screen1.ids.name.text)
        print(self.screen1.ids.second_name.text)
        print(self.screen1.ids.phone.text)
        print(self.screen1.ids.password.text)
        global USER
        USER = user
        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        scrMan.add_widget(Login(name="Login"))
        scrMan.remove_widget(self)

    def changer3(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Home(name="Home"))
        scrMan.remove_widget(self)

    def changer4(self, *args):
        self.screen1.ids.password.text=''
        self.screen1.ids.name.text = ''
        self.screen1.ids.second_name.text = ''
        self.screen1.ids.phone.text = ''
        self.screen1.ids.surname.text = ''

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("main.kv"))
        my_button1 = MDFloatingActionButton(icon="git", elevation_normal=12, pos_hint={"center_x": .9, "center_y": .95},
                                            size_hint=(None, None), segment_panel_height="56dp")

        my_button2 = MDFloatingActionButton(icon="plus", elevation_normal=12, pos_hint={"center_x": .5, "center_y": .1})

        my_button3 = MDFloatingActionButton(
            icon="instagram", elevation_normal=0,
            pos_hint={"center_x": .1, "center_y": .95},
            size_hint=(None, None))
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)

        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.screen1.add_widget(my_button3)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(ProfileWindow(name="ProfileWindow"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(TripFrom(name="TripFrom"))
        scrMan.remove_widget(self)

    def changer3(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Burger(name="Burger"))
        scrMan.remove_widget(self)


class TripFrom(Screen):
    def __init__(self, **kwargs):
        super(TripFrom, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("add_trip.kv"))
        self.screen1 = Builder.load_file("add_trip.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        self.my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                                 background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(self.my_button2)
        self.a = MDLabel(text="Где собираемся?", font_size="20", pos_hint={"center_y": .97}, halign="center",
                         color=[34, 34, 34, 255])
        self.screen1.add_widget(self.a)
        self.add_widget(self.screen1)
        self.my_button2.bind(on_press=self.changer2)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(TripTo(name="TripTo"))
        scrMan.remove_widget(self)


class TripTo(Screen):
    def __init__(self, **kwargs):
        super(TripTo, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("add_trip.kv"))
        self.screen1 = Builder.load_file("add_trip.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        self.my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                                 background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(self.my_button2)
        self.a = MDLabel(text="Куда едем?", font_size="20", pos_hint={"center_y": .97}, halign="center",
                         color=[34, 34, 34, 255])
        self.screen1.add_widget(self.a)
        self.add_widget(self.screen1)
        self.my_button2.bind(on_press=self.changer2)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(TripFrom(name="TripFrom"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(InputTripInformation(name="InputTripInformation"))
        scrMan.remove_widget(self)


class InputTripInformation(Screen):
    def __init__(self, **kwargs):
        super(InputTripInformation, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("inf_trip.kv"))
        self.screen1 = Builder.load_file("inf_trip.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer1)
        my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                            background_color=[0, 0, 0, 0])
        my_button2.bind(on_press=self.changer2)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(TripTo(name="TripTo"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        print(self.screen1.ids.date.text, self.screen1.ids.time.text, self.screen1.ids.number.text)
        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)


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
        my_button5.bind(on_press=self.file_manager_open)
        self.manager_open = False
        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path)

        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        screen1.add_widget(my_button3)
        screen1.add_widget(my_button4)
        screen1.add_widget(my_button5)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(Reviews(name="Reviews"))
        scrMan.remove_widget(self)

    def changer3(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(HistoryTrip(name="HistoryTrip"))
        scrMan.remove_widget(self)

    def changer4(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(Settings(name="Settings"))
        scrMan.remove_widget(self)

    def file_manager_open(self, *args):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def select_path(self, path: str):
        self.exit_manager()
        toast(path)
        print(path)
        # im1 = Image.open(path)
        # im1 = im1.save(r"C:\Users\Пользователь\PycharmProjects\MobileApp\sereza\myphoto.png")

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


class Reviews(Screen):
    def __init__(self, **kwargs):
        super(Reviews, self).__init__(**kwargs)
        screen1 = Screen()
        reviews = client.watchReview(USER)
        widget_grid_layout = scrollview.MDScrollView(gridlayout.MDGridLayout(id="box", cols=1, adaptive_height=True))
        if reviews:
            for review in reviews:
                widget_grid_layout.ids.box.add_widget(MDExpansionPanelThreeLine(
                    text=str(review[2]),
                    secondary_text=str(review[1]),
                    tertiary_text=str(review[0])
                ))
        else:
            widget_grid_layout.ids.box.add_widget(MDExpansionPanelThreeLine(
                text='Отзывов нет!',
                secondary_text='',
                tertiary_text='')
            )
        screen1.add_widget(widget_grid_layout)
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer)
        screen1.add_widget(my_button1)
        self.add_widget(screen1)

    def changer(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(ProfileWindow(name="ProfileWindow"))
        scrMan.remove_widget(self)


class HistoryTrip(Screen):
    def __init__(self, **kwargs):
        super(HistoryTrip, self).__init__(**kwargs)
        trips = client.loadStoryTravel(USER)
        print(trips)
        screen1 = Screen()
        widget_grid_layout = scrollview.MDScrollView(gridlayout.MDGridLayout(id="box", cols=1, adaptive_height=True))
        for i in range(10):
            widget_grid_layout.ids.box.add_widget(MDExpansionPanelTwoLine(
                text="Text",
                secondary_text="Secondary text",
            ))
        screen1.add_widget(widget_grid_layout)
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer)
        screen1.add_widget(my_button1)
        self.add_widget(screen1)

    def changer(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(ProfileWindow(name="ProfileWindow"))
        scrMan.remove_widget(self)


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
        self.manager.transition.direction = "left"
        scrMan.add_widget(DataChange(name="DataChange"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(PasswordChange(name="PasswordChange"))
        scrMan.remove_widget(self)

    def changer3(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Home(name="Home"))
        scrMan.remove_widget(self)

    def changer4(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(ProfileWindow(name="ProfileWindow"))
        scrMan.remove_widget(self)


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
        self.manager.transition.direction = "left"
        scrMan.add_widget(DataChange(name="DataChange"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(PhoneChange(name="PhoneChange"))
        scrMan.remove_widget(self)

    def changer3(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(NameChange(name="NameChange"))
        scrMan.remove_widget(self)

    def changer4(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Settings(name="Settings"))
        scrMan.remove_widget(self)


class PasswordChange(Screen):
    def __init__(self, **kwargs):
        super(PasswordChange, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("password.kv"))
        self.screen1 = Builder.load_file("password.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp", size_hint=[.1, .05],
                            pos_hint={"center_x": .5, "center_y": .05},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Settings(name="Settings"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "right"
        print(self.screen1.ids.password.text, self.screen1.ids.password.text, self.screen1.ids.password.text)
        scrMan.add_widget(Settings(name="Settings"))
        scrMan.remove_widget(self)


class PhoneChange(Screen):
    def __init__(self, **kwargs):
        super(PhoneChange, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("phonenumber.kv"))
        self.screen1 = Builder.load_file("phonenumber.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp", size_hint=[.1, .05],
                            pos_hint={"center_x": .5, "center_y": .05},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(DataChange(name="DataChange"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "right"
        print(self.screen1.ids.phone.text)
        scrMan.add_widget(DataChange(name="DataChange"))
        scrMan.remove_widget(self)


class NameChange(Screen):
    def __init__(self, **kwargs):
        super(NameChange, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("name.kv"))
        self.screen1 = Builder.load_file("name.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp", size_hint=[.1, .05],
                            pos_hint={"center_x": .5, "center_y": .05},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(DataChange(name="DataChange"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "right"
        print(self.screen1.ids.fam.text, self.screen1.ids.name.text, self.screen1.ids.otch.text)
        scrMan.add_widget(DataChange(name="DataChange"))
        scrMan.remove_widget(self)


class StrangeProfile(Screen):
    def __init__(self, **kwargs):
        super(StrangeProfile, self).__init__(**kwargs)
        screen1 = Screen()
        my_button1 = MDIconButton(icon="plus", pos_hint={"center_y": .8},
                                  text_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        name_profile = MDLabel(text="Имя", font_size="48", pos_hint={"center_y": .7},
                               halign="center",
                               color=[34, 34, 34, 255])
        rating_profile = MDLabel(text="Рейтинг: 3.5/5",
                                 font_size="24", pos_hint={"center_y": .6},
                                 halign="center",
                                 color=[34, 34, 34, 255])
        text_review = MDLabel(text="Отзывы:",
                              font_size="24", pos_hint={"center_y": .6},
                              halign="center",
                              color=[34, 34, 34, 255])
        scroll = scrollview.MDScrollView(
            gridlayout.MDGridLayout(id="box", cols=1, adaptive_height=True, spacing="50dp", padding="10dp"))
        scroll_reviews = gridlayout.MDGridLayout(cols=1, adaptive_height=True)
        scroll.ids.box.add_widget(name_profile)
        scroll.ids.box.add_widget(rating_profile)
        scroll.ids.box.add_widget(text_review)
        for i in range(10):
            scroll_reviews.add_widget(MDExpansionPanelTwoLine(
                text=str(i + 1),
                secondary_text="asdasdsadjansdjnajsdnadjsnasdjda",
            ))
        scroll.ids.box.add_widget(scroll_reviews)
        screen1.add_widget(scroll)
        screen1.add_widget(my_button1)
        self.add_widget(screen1)

    def changer1(self, *args):
        self.manager.current = 'comment'


class Coment(Screen):
    def __init__(self, **kwargs):
        super(Coment, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("comment.kv"))
        self.screen1 = Builder.load_file("comment.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer1)
        my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                            background_color=[0, 0, 0, 0])
        my_button2.bind(on_press=self.changer2)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        self.manager.current = 'StrangeProfile'
    def changer2(self, *args):
        self.manager.transition.direction = "right"
        self.manager.current = 'StrangeProfile'
        print(self.screen1.ids.com.text)

class Burger(Screen):

    def __init__(self, **kwargs):
        super(Burger, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("burger.kv"))
        self.screen1 = Builder.load_file("burger.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp",
                                  text_color=[0, 0, 0, 0])
        my_button2 = Button(font_size="24sp", size_hint=[.2, .05],
                            pos_hint={"center_x": .5, "center_y": .05},
                            background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        print(self.screen1.ids.from_.text, self.screen1.ids.to_.text, self.screen1.ids.date.text)
        scrMan.add_widget(Travel(name="Travel"))
        scrMan.remove_widget(self)

class Travel(Screen):
    def __init__(self, **kwargs):
        super(Travel, self).__init__(**kwargs)
        screen1 = Screen()
        layout = gridlayout.MDGridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(10):
            btn = Button(text="Ебать карточка", size_hint_y=None, height=50, background_color="blue")
            layout.add_widget(btn)
        a = scrollview.MDScrollView(size_hint=[1, .9], size=[Window.width, Window.height])
        a.add_widget(layout)
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer)
        screen1.add_widget(my_button1)
        screen1.add_widget(a)
        self.add_widget(screen1)

    def changer(self, *args):
        scrMan.add_widget(Burger(name="Burger"))
        scrMan.remove_widget(self)

client = Client('192.168.0.84', 8888)
client.connect()

USER = None

scrMan = None

class MyApp(MDApp):
    def build(self):
        self.my_screenmanager = ScreenManager()
        self.screen1 = Home(name='Home')
        # screen2 = Login(name='Login')
        # screen3 = SignUp(name='SignUp')
        # screen4 = MainWindow(name='MainWindow')
        # screen5 = ProfileWindow(name='ProfileWindow')
        # screen6 = Reviews(name='Reviews')
        # screen7 = TripFrom(name='TripFrom')
        # screen8 = TripTo(name='TripTo')
        # screen9 = Settings(name='Settings')
        # screen10 = DataChange(name='DataChange')
        # screen11 = PasswordChange(name='PasswordChange')
        # screen12 = HistoryTrip(name='HistoryTrip')
        # screen13 = PhoneChange(name='PhoneChange')
        # screen14 = NameChange(name='NameChange')
        # screen15 = InputTripInformation(name='InputTripInformation')
        # screen16 = StrangeProfile(name='StrangeProfile')
        # screen17 = Burger(name='Burger')
        # screen18 = Travel(name='Travel')
        self.my_screenmanager.add_widget(self.screen1)
        # self.my_screenmanager.add_widget(screen2)
        # self.my_screenmanager.add_widget(screen3)
        # self.my_screenmanager.add_widget(screen4)
        # self.my_screenmanager.add_widget(screen5)
        # self.my_screenmanager.add_widget(screen6)
        # self.my_screenmanager.add_widget(screen7)
        # self.my_screenmanager.add_widget(screen8)
        # self.my_screenmanager.add_widget(screen9)
        # self.my_screenmanager.add_widget(screen10)
        # self.my_screenmanager.add_widget(screen11)
        # self.my_screenmanager.add_widget(screen12)
        # self.my_screenmanager.add_widget(screen13)
        # self.my_screenmanager.add_widget(screen14)
        # self.my_screenmanager.add_widget(screen15)
        # self.my_screenmanager.add_widget(screen16)
        # self.my_screenmanager.add_widget(screen17)
        # self.my_screenmanager.add_widget(screen18)

        global scrMan
        scrMan = self.my_screenmanager
        return self.my_screenmanager


MyApp().run()
