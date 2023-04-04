from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.modules import inspector
from kivy.properties import ColorProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

Builder.load_file("kivy_screen_example.kv")


class Manager(ScreenManager):
    def switch_screen(self, screen):
        if screen.name == "first":
            self.current = "second"
        if screen.name == "second":
            self.current = "first"


WHITE = 1, 1, 1, 1
BLACK = 0, 0, 0, 1


class ColoredLabel(Label):
    background_color = ColorProperty(WHITE)
    text_color = ColorProperty(BLACK)


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class KivyScreenExampleApp(App):

    def build(self):
        root = Manager()
        Window.size = (800, 600)

        inspector.create_inspector(Window, root)
        return root


if __name__ == '__main__':
    KivyScreenExampleApp().run()
