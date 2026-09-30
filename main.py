from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class HeeraApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=40,
            spacing=30
        )

        title = Label(
            text="Heera",
            font_size=42
        )

        message = Label(
            text="Assalamualaikum Faarmaan Khan\nMain Heera hoon",
            font_size=24
        )

        mic_button = Button(
            text="🎙️  Boliye",
            font_size=28,
            size_hint=(1, 0.25)
        )

        layout.add_widget(title)
        layout.add_widget(message)
        layout.add_widget(mic_button)

        return layout


if __name__ == "__main__":
    HeeraApp().run()
