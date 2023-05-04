#!/bin/python3.10
"""
A simple Program to calculate the monthly cost for a house.
"""
from calc import HouseProperties
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView


def main():
    VanDeCalc().run()


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class VanDeCalc(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pr = HouseProperties()

    def error_handler(self, value):
        try:
            value = float(value)
            return value
        except ValueError as e:
            print(e)
            return 0

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("app.kv")


if __name__ == "__main__":
    main()
