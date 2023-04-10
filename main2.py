from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy_garden.mapview import MapView

from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.utils import asynckivy

KV = '''
#:import MapSource kivy_garden.mapview.MapSource
#:import asynckivy kivymd.utils.asynckivy


<TypeMapElement>
    orientation: "vertical"
    adaptive_height: True
    spacing: "8dp"

    MDIconButton:
        id: icon
        icon: root.icon
        md_bg_color: "#EDF1F9" if not root.selected else app.theme_cls.primary_color
        pos_hint: {"center_x": .5}
        theme_icon_color: "Custom"
        icon_color: "white" if root.selected else "black"
        on_release: app.set_active_element(root, root.title.lower())

    MDLabel:
        font_size: "14sp"
        text: root.title
        pos_hint: {"center_x": .5}
        halign: "center"
        adaptive_height: True


MDScreen:

    CustomMapView:
        bottom_sheet: bottom_sheet
        map_source: MapSource(url=app.map_sources[app.current_map])
        lat: 46.5124
        lon: 47.9812
        zoom: 12

    MDBottomSheet:
        id: bottom_sheet
        elevation: 2
        shadow_softness: 6
        bg_color: "white"
        type: "standard"
        max_opening_height: self.height
        default_opening_height: self.max_opening_height
        adaptive_height: True
        on_open: asynckivy.start(app.generate_content())

        MDBottomSheetDragHandle:
            drag_handle_color: "grey"

            MDBottomSheetDragHandleTitle:
                text: "Select type map"
                adaptive_height: True
                bold: True
                pos_hint: {"center_y": .5}

            MDBottomSheetDragHandleButton:
                icon: "close"
                _no_ripple_effect: True
                on_release: bottom_sheet.dismiss()

        MDBottomSheetContent:
            id: content_container
            padding: 0, 0, 0, "16dp"
'''


class TypeMapElement(MDBoxLayout):
    selected = BooleanProperty(False)
    icon = StringProperty()
    title = StringProperty()


class CustomMapView(MapView, TouchBehavior):
    bottom_sheet = ObjectProperty()

    def on_double_tap(self, touch, *args):
        if self.bottom_sheet:
            self.bottom_sheet.open()


class Example(MDApp):
    map_sources = {
        "street": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        "sputnik": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
        "hybrid": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    }
    current_map = StringProperty("street")

    async def generate_content(self):
        icons = {
            "street": "google-street-view",
            "sputnik": "space-station",
            "hybrid": "map-legend",
        }
        if not self.root.ids.content_container.children:
            for i, title in enumerate(self.map_sources.keys()):
                await asynckivy.sleep(0)
                self.root.ids.content_container.add_widget(
                    TypeMapElement(
                        title=title.capitalize(),
                        icon=icons[title],
                        selected=not i,
                    )
                )

    def set_active_element(self, instance, type_map):
        for element in self.root.ids.content_container.children:
            if instance == element:
                element.selected = True
                self.current_map = type_map
            else:
                element.selected = False

    def build(self):
        return Builder.load_string(KV)


Example().run()