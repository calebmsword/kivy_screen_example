from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.modules import inspector
from kivy.properties import ColorProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

WHITE = 1, 1, 1, 1
BLACK = 0, 0, 0, 1


Builder.load_string(f"""
#: import NoTransition kivy.uix.screenmanager.NoTransition

<RootWidget>:
    transition: NoTransition()
    FirstScreen:
    SecondScreen:
    
        
<FirstScreen>:
    name: "first"
    BoxLayout:
        orientation: "vertical"
        padding: "40dp"
        spacing: "40dp"
        ColoredLabel:
            background_color: {WHITE}
            text_color: {BLACK}
            text: "First screen"
        Button:
            text: "Switch screens"
            on_release: root.manager.switch_screen(root)
    

<SecondScreen>:
    name: "second"
    BoxLayout:
        orientation: "vertical"
        padding: "40dp"
        spacing: "40dp"
        ColoredLabel:
            background_color: {WHITE}
            text_color: {BLACK}
            text: "Second screen"
        Button:
            text: "Switch screens"
            on_release: root.manager.switch_screen(root)
    
    
<ColoredLabel>:
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
    color: self.text_color
""")


class RootWidget(ScreenManager):
    def switch_screen(self, screen):
        if screen.name == "first":
            self.current = "second"
        if screen.name == "second":
            self.current = "first"


class ColoredLabel(Label):
    background_color = ColorProperty(WHITE)
    text_color = ColorProperty(BLACK)


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class ScreenManagerTest(App):

    def build(self):
        root = RootWidget()
        Window.size = (800, 600)

        inspector.create_inspector(Window, root)
        return root


if __name__ == '__main__':
    ScreenManagerTest().run()
