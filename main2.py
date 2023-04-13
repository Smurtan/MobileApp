import requests
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy_garden.mapview import MapView, MapSource, MapMarkerPopup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFloatingActionButton, MDIconButton, MDTextButton, MDFlatButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.expansionpanel import MDExpansionPanelThreeLine, MDExpansionPanelTwoLine
from kivymd.uix import scrollview
from kivymd.uix import gridlayout
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
import os
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivymd.toast import toast

from geopy.geocoders import Nominatim

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
        scrMan.add_widget(Login(name="Login"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(SignUp(name="SignUp"))
        scrMan.remove_widget(self)


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
        my_button4 = MDTextButton(text="Очистить", font_size="12sp", pos_hint={"center_x": .5, "center_y": .28},
                                  color=[68, 78, 132, 255])

        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        my_button4.bind(on_press=self.changer4)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.screen1.add_widget(my_button3)
        self.screen1.add_widget(my_button4)
        self.add_widget(self.screen1)

    def create_dialog(self):
        close_btn = MDFlatButton(text="Закрыть", on_release=self.close_dialog)
        self.dialogscr = MDDialog(title='Логин, или пароль не верный',
                                  text='Попробуйте снова',
                                  size_hint=(0.5, 1),
                                  buttons=[close_btn])
        self.dialogscr.open()

    def close_dialog(self, *args):
        self.dialogscr.dismiss()

    def changer1(self, *args):
        user = client.login(
            self.screen1.ids.phone.text,
            self.screen1.ids.password.text
        )
        print(self.screen1.ids.phone.text)
        print(self.screen1.ids.password.text)

        if user:
            global USER
            USER = user
            scrMan.add_widget(MainWindow(name="MainWindow"))
            scrMan.remove_widget(self)
        else:
            self.create_dialog()
            self.screen1.ids.phone.text = ''
            self.screen1.ids.password.text = ''

    def changer2(self, *args):
        scrMan.add_widget(SignUp(name="SignUp"))
        scrMan.remove_widget(self)

    def changer3(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Home(name="Home"))
        scrMan.remove_widget(self)

    def changer4(self, *args):
        self.screen1.ids.password.text = ''
        self.screen1.ids.phone.text = ''


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
        self.screen1.ids.password.text = ''
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

        if CONDITION == 'pas':
            self.my_button4 = MDRoundFlatButton(
                text="Водитель",
                size_hint=[.3, .055],
                md_bg_color="white",
                pos_hint={"center_x": .25, "center_y": .1})
            self.my_button5 = MDRoundFlatButton(
                text="Пассажир",
                size_hint=[.3, .055],
                md_bg_color="blue",
                text_color="white",
                pos_hint={"center_x": .75, "center_y": .1})
        else:
            self.my_button4 = MDRoundFlatButton(
                text="Водитель",
                size_hint=[.3, .055],
                md_bg_color="blue",
                text_color="white",
                pos_hint={"center_x": .25, "center_y": .1})
            self.my_button5 = MDRoundFlatButton(
                text="Пассажир",
                size_hint=[.3, .055],
                md_bg_color="white",
                pos_hint={"center_x": .75, "center_y": .1})

        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        my_button3.bind(on_press=self.changer3)
        self.my_button4.bind(on_press=self.changer4)
        self.my_button5.bind(on_press=self.changer5)

        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.screen1.add_widget(my_button3)
        self.screen1.add_widget(self.my_button4)
        self.screen1.add_widget(self.my_button5)
        self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "left"
        scrMan.add_widget(ProfileWindow(name="ProfileWindow"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"
        global CONDITION
        if CONDITION == 'vod':
            scrMan.add_widget(TripFrom(name="TripFrom"))
            scrMan.remove_widget(self)
        else:
            scrMan.add_widget(TripFromPas(name="TripFromPas"))
            scrMan.remove_widget(self)

    def changer3(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(Burger(name="Burger"))
        scrMan.remove_widget(self)

    def changer4(self, *args):
        global CONDITION
        self.my_button4.md_bg_color = 'blue'
        self.my_button4.text_color = 'white'
        self.my_button5.md_bg_color = 'white'
        self.my_button5.text_color = 'blue'
        CONDITION = 'vod'

    def changer5(self, *args):
        global CONDITION
        self.my_button5.md_bg_color = 'blue'
        self.my_button5.text_color = 'white'
        self.my_button4.md_bg_color = 'white'
        self.my_button4.text_color = 'blue'
        CONDITION = 'pas'


class TripFrom(Screen):
    def __init__(self, **kwargs):
        super(TripFrom, self).__init__(**kwargs)
        self.screen1 = Screen()

        # self.map = MapView(map_source=MapSource(url="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"), lat=58.08,
        #                    lon=38.8,
        #                    zoom=10)
        # self.screen1.add_widget(self.map)
        # c = self.screen1.on_touch_up

        self.screen1.add_widget(Builder.load_file("add_trip.kv"))
        self.screen1 = Builder.load_file("add_trip.kv")
        self.my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        self.my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                                 background_color=[0, 0, 0, 0])
        self.my_button1.bind(on_press=self.changer1)
        self.screen1.add_widget(self.my_button1)
        self.screen1.add_widget(self.my_button2)
        self.m = MDLabel(text="Где собираемся?", font_size="20", pos_hint={"center_y": .97}, halign="center",
                         color=[34, 34, 34, 255])
        self.screen1.add_widget(self.m)
        self.add_widget(self.screen1)
        self.my_button2.bind(on_press=self.changer2)


        self.f = False

    # def get_addres(self, coors):
    #     return Nominatim(user_agent="my_application").reverse(coors).address.split(',')[1]

    # def on_touch_up(self, touch):
    #     print(touch.pos, touch.spos)
    #
    #     print(self.map.get_latlon_at(touch.spos[0], touch.spos[1])[0],
    #           self.map.get_latlon_at(touch.pos[0], touch.spos[1])[1])
    #     if not self.f:
    #         self.a = MapMarkerPopup(lat=self.map.get_latlon_at(touch.pos[0], touch.pos[1])[0],
    #                            lon=self.map.get_latlon_at(touch.pos[0], touch.spos[1])[1], popup_size=[230, 130])
    #
    #         self.screen1.ids.city.text = self.get_addres((self.map.get_latlon_at(touch.pos[0], touch.pos[1])[0],
    #                                                       self.map.get_latlon_at(touch.pos[0], touch.spos[1])[
    #                                                           1]))
    #
    #         self.screen1.add_widget(self.a)
    #         self.f = True
    #     else:
    #         self.screen1.ids.city.text = self.get_addres((self.map.get_latlon_at(touch.pos[0], touch.pos[1])[0],
    #                                                           self.map.get_latlon_at(touch.pos[0], touch.spos[1])[1]))
    #         self.screen1.remove_widget(self.a)
    #         self.a.lat = self.map.get_latlon_at(touch.pos[0], touch.pos[1])[0]
    #         self.a.lon = self.map.get_latlon_at(touch.pos[0], touch.spos[1])[1]
    #         self.screen1.add_widget(self.a)

            # self.screen1.remove_widget(self.my_button1)
            # self.screen1.remove_widget(self.my_button2)
            # self.screen1.add_widget(self.my_button1)
            # self.screen1.add_widget(self.my_button2)
            #self.add_widget(self.screen1)

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"

        try:
            from_coordinates = Coordinaty(self.screen1.ids.city.text)
            print(from_coordinates.get_coordinates())
            scrMan.add_widget(TripTo(from_coordinates.get_coordinates(), name="TripTo"))
            scrMan.remove_widget(self)
        except IndexError as e:
            pass


class TripTo(Screen):
    def __init__(self, From, **kwargs):
        self.From = From
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

        try:
            from_coordinates = Coordinaty(self.screen1.ids.city.text)
            print(from_coordinates.get_coordinates())
            scrMan.add_widget(InputTripInformation(self.From, from_coordinates.get_coordinates(), name="InputTripInformation"))
            scrMan.remove_widget(self)
        except(IndexError) as e:
            pass


class InputTripInformation(Screen):
    def __init__(self, From, To, **kwargs):
        self.From = From
        self.To = To
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

        print(self.screen1.ids.date.text, self.screen1.ids.time.text, self.screen1.ids.number.text,
              self.screen1.ids.prise.text)

    def create_dialog(self):
        close_btn = MDFlatButton(text="Закрыть", on_release=self.close_dialog)
        self.dialogscr = MDDialog(title='Ура!',
                                  text='Поездка успешно добавлена.',
                                  size_hint=(0.5, 1),
                                  buttons=[close_btn])
        self.dialogscr.open()

    def close_dialog(self, *args):
        self.dialogscr.dismiss()

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(TripTo(name="TripTo"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        print(self.screen1.ids.date.text, self.screen1.ids.time.text, self.screen1.ids.number.text,
              self.screen1.ids.prise.text)
        data = client.addTravel(USER, self.From, self.To, self.screen1.ids.date.text, self.screen1.ids.time.text, self.screen1.ids.prise.text, self.screen1.ids.number.text)


        if data:
            fellows = client.loadFellow(self.From, self.To, self.screen1.ids.date.text)

            # if fellows[0]:
            #     scrMan.add_widget(FellowWindow(fellows, name="FellowWindow"))
            #     scrMan.remove_widget(self)
            # else:
            self.create_dialog()

        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)


class FellowWindow(Screen):
    pass
# СЕРЁГА


class TripFromPas(Screen):
    def __init__(self, **kwargs):
        super(TripFromPas, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("add_trip.kv"))
        self.screen1 = Builder.load_file("add_trip.kv")
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        self.my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                                 background_color=[0, 0, 0, 0])
        my_button1.bind(on_press=self.changer1)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(self.my_button2)
        self.a = MDLabel(text="Откуда держим путь?", font_size="20", pos_hint={"center_y": .97}, halign="center",
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

        try:
            from_coordinates = Coordinaty(self.screen1.ids.city.text)
            print(from_coordinates.get_coordinates())
            scrMan.add_widget(TripToPas(from_coordinates.get_coordinates(), name="TripToPas"))
            scrMan.remove_widget(self)
        except IndexError as e:
            pass


class TripToPas(Screen):
    def __init__(self, From, **kwargs):
        self.From = From
        super(TripToPas, self).__init__(**kwargs)
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
        scrMan.add_widget(TripFromPas(name="TripFromPas"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        self.manager.transition.direction = "left"

        try:
            from_coordinates = Coordinaty(self.screen1.ids.city.text)
            print(from_coordinates.get_coordinates())
            scrMan.add_widget(InputTripInformationPas(self.From, from_coordinates.get_coordinates(), name="InputTripInformationPas"))
            scrMan.remove_widget(self)
        except(IndexError) as e:
            pass


class InputTripInformationPas(Screen):
    def __init__(self, From, To, **kwargs):
        self.From = From
        self.To = To
        super(InputTripInformationPas, self).__init__(**kwargs)
        self.screen1 = Screen()
        self.screen1.add_widget(Builder.load_file("inf_trip_pas.kv"))
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, user_font_size="30sp")
        my_button1.bind(on_press=self.changer1)
        my_button2 = Button(font_size="20sp", size_hint=[.3, .05], pos_hint={"center_x": .8, "center_y": .1},
                            background_color=[0, 0, 0, 0])
        my_button2.bind(on_press=self.changer2)
        self.screen1.add_widget(my_button1)
        self.screen1.add_widget(my_button2)
        self.add_widget(self.screen1)

    def create_suc_dialog(self):
        close_btn = MDFlatButton(text="Закрыть", on_release=self.close_dialog)
        self.dialogscr = MDDialog(title='Ура!',
                                  text='Запрос на поездку создан.',
                                  size_hint=(0.5, 1),
                                  buttons=[close_btn])
        self.dialogscr.open()

    def create_unsuc_dialog(self):
        close_btn = MDFlatButton(text="Закрыть", on_release=self.close_dialog)
        self.dialogscr = MDDialog(title='Неудача',
                                  text='Запрос был создан не верно.',
                                  size_hint=(0.5, 1),
                                  buttons=[close_btn])
        self.dialogscr.open()

    def close_dialog(self, *args):
        self.dialogscr.dismiss()

    def changer1(self, *args):
        self.manager.transition.direction = "right"
        scrMan.add_widget(TripToPas(name="TripToPas"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        global USER
        data = client.addRequest(USER, self.From, self.To, self.screen1.ids.date.text)
        if data:
            self.create_suc_dialog()
        else:
            self.create_unsuc_dialog()

        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)


class Coordinaty:
    def __init__(self, city):
        self.city = city

    def get_coordinates(self):
        get_url = 'http://api.opencagedata.com/geocode/v1/json?q={}&key=5ab8e108b0dc43a985c263009996f26e'.format(
            self.city)
        response = requests.get(get_url).json()

        self.latitude = response['results'][0]['geometry']['lat']
        self.longitude = response['results'][0]['geometry']['lng']
        return self.latitude, self.longitude


class ProfileWindow(Screen):
    def __init__(self, **kwargs):
        super(ProfileWindow, self).__init__(**kwargs)
        global USER
        data = client.watchProfile(USER)
        screen1 = Screen()
        screen1.add_widget(Builder.load_file("ProfileScreen.kv"))
        name = MDLabel(text=str(data[1]), font_size="48sp", pos_hint={"center_y": .7},
                       halign="center", color=[34, 34, 34, 255])
        rating = MDLabel(text=f'Рейтинг: {str(data[0])}/5.00', font_size="24sp", pos_hint={"center_y": .6},
                         halign="center", color=[34, 34, 34, 255])
        screen1.add_widget(name)
        screen1.add_widget(rating)
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
        print(reviews)
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
        global USER
        trips = client.loadStoryTravel(USER)
        screen1 = Screen()
        widget_grid_layout = scrollview.MDScrollView(gridlayout.MDGridLayout(id="box", cols=1, adaptive_height=True))
        print(trips)
        if trips:
            for trip in trips:
                widget_grid_layout.ids.box.add_widget(MDExpansionPanelTwoLine(
                    text=f'{trip[0]} -> {trip[1]}',
                    secondary_text=f'{trip[2]} {trip[3]}'
                ))
        else:
            widget_grid_layout.ids.box.add_widget(MDExpansionPanelTwoLine(
                text="Вы ещё небыли ни в одной поездке",
                secondary_text=""
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
        scrMan.add_widget(
            Travel(self.screen1.ids.from_.text, self.screen1.ids.to_.text, self.screen1.ids.date.text, name="Travel"))
        scrMan.remove_widget(self)


class Travel(Screen):
    def __init__(self, From, To, date, **kwargs):
        self.From = From
        self.To = To
        self.date = date.split('/')
        self.date = f'{self.date[2]}-{self.date[1]}-{self.date[0]}'
        super(Travel, self).__init__(**kwargs)
        travels = client.loadTravels(self.From, self.To, self.date)
        print(travels) # [[4, 400, '8:30:00', 'Artem']]
        screen1 = Screen()
        layout = gridlayout.MDGridLayout(cols=1, padding=20, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.buttons = []
        if travels:
            for trip in travels:
                layout.add_widget(Widget())
                btn = Button(text=f'{trip[3]}        {trip[2]}         {trip[1]}₽', size_hint_y=None, width=200, height=50, background_color="blue")

                btn.bind(on_press=lambda *args: self.changer1(trip[0], trip[3], trip[2], trip[1], trip[4]))
                self.buttons.append(btn)
                layout.add_widget(btn)
                layout.add_widget(Widget())
        layout.bind(minimum_height=layout.setter('height'))
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

    def changer1(self, *args):
        print(args[0])
        scrMan.add_widget(Bron(args[0], self.From, self.To, args[1], self.date, args[2], args[3], args[4],  name="Bron"))
        scrMan.remove_widget(self)

class Bron(Screen):
    def __init__(self, travel, From, To, driver, date, time, prise, num_pas, **kwargs):
        super(Bron, self).__init__(**kwargs)
        self.travel = travel
        screen1 = Screen()
        my_button1 = MDIconButton(icon="arrow-left", pos_hint={"center_y": .95}, font_size="30sp")
        my_button2 = Button(text= "Забронировать", font_size="16sp", size_hint=( .35, .075), pos_hint={"center_x": .8,"center_y": .1})
        text_from = MDLabel(text=f"Откуда: {From}", font_size="48", pos_hint={"left_x": .1, "center_y": .85},
        halign="center", color=[34, 34, 34, 255])
        text_to = MDLabel(text=f"Куда: {To}", font_size="48", pos_hint={"left_x": .1, "center_y": .8},
        halign="center", color=[34, 34, 34, 255])
        text_driver = MDLabel(text=f"Водитель: {driver}", font_size="48", pos_hint={"left_x": .1, "center_y": .75},
                          halign="center", color=[34, 34, 34, 255])
        text_date = MDLabel(text=f"Дата: {date}", font_size="48", pos_hint={"left_x": .1, "center_y": .7},
                          halign="center", color=[34, 34, 34, 255])
        text_time = MDLabel(text=f"Время: {time}", font_size="48", pos_hint={"left_x": .1, "center_y": .65},
                            halign="center", color=[34, 34, 34, 255])
        text_price = MDLabel(text=f"Цена: {prise}", font_size="48", pos_hint={"left_x": .1, "center_y": .6}, halign="center", color=[34, 34, 34, 255])
        name_pass = MDLabel(text=f"Количество пассажиров: {num_pas}", font_size="48", pos_hint={"left_x": .1, "center_y": .55},
        halign="center", color=[34, 34, 34, 255])


        my_button1.bind(on_press=self.changer1)
        my_button2.bind(on_press=self.changer2)
        screen1.add_widget(my_button1)
        screen1.add_widget(my_button2)
        screen1.add_widget(text_from)
        screen1.add_widget(text_to)
        screen1.add_widget(text_driver)
        screen1.add_widget(text_date)
        screen1.add_widget(text_time)
        screen1.add_widget(text_price)
        screen1.add_widget(name_pass)
        self.add_widget(screen1)

    def create_suc_dialog(self):
        close_btn = MDFlatButton(text="Закрыть", on_release=self.close_dialog)
        self.dialogscr = MDDialog(title='Ура!',
                                  text='Поездка забронирована.',
                                  size_hint=(0.5, 1),
                                  buttons=[close_btn])
        self.dialogscr.open()

    def create_unsuc_dialog(self):
        close_btn = MDFlatButton(text="Закрыть", on_release=self.close_dialog)
        self.dialogscr = MDDialog(title='Неудача',
                                  text='К сожалению, бронирование не удалось.',
                                  size_hint=(0.5, 1),
                                  buttons=[close_btn])
        self.dialogscr.open()

    def close_dialog(self, *args):
        self.dialogscr.dismiss()

    def changer1(self, *args):
        scrMan.add_widget(Burger(name="Burger"))
        scrMan.remove_widget(self)

    def changer2(self, *args):
        print(1)
        global USER
        print(self.travel)
        data = client.addPassager(USER, self.travel)
        if data:
            self.create_suc_dialog()
        else:
            self.create_unsuc_dialog()
        scrMan.add_widget(MainWindow(name="MainWindow"))
        scrMan.remove_widget(self)



client = Client('192.168.0.84', 8888)
client.connect()

USER = None
CONDITION = 'pas'

scrMan = None


class MyApp(MDApp):
    def build(self):
        self.my_screenmanager = ScreenManager()
        self.screen1 = Home(name='Home')
        self.my_screenmanager.add_widget(self.screen1)

        global scrMan
        scrMan = self.my_screenmanager
        return self.my_screenmanager


MyApp().run()
