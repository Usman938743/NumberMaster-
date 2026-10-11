import random

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Window.clearcolor = (0.04, 0.07, 0.16, 1)


class GuessGame(App):

    def build(self):
        self.new_game()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(24),
            spacing=dp(14)
        )

        title = Label(
            text="NUMBER MASTER",
            font_size=sp(28),
            bold=True,
            color=(0.3, 0.9, 1, 1),
            size_hint_y=None,
            height=dp(65)
        )

        subtitle = Label(
            text="Guess a number from 1 to 10",
            font_size=sp(17),
            size_hint_y=None,
            height=dp(45)
        )

        self.message = Label(
            text="Ready to play?",
            font_size=sp(21),
            color=(1, 0.85, 0.25, 1)
        )

        self.attempt_label = Label(
            text="Attempts left: 5",
            font_size=sp(17),
            size_hint_y=None,
            height=dp(40)
        )

        self.number = TextInput(
            hint_text="Enter your guess",
            multiline=False,
            input_filter="int",
            halign="center",
            font_size=sp(24),
            size_hint_y=None,
            height=dp(55)
        )

        self.guess_button = Button(
            text="GUESS!",
            font_size=sp(20),
            bold=True,
            size_hint_y=None,
            height=dp(58),
            background_normal="",
            background_color=(0.05, 0.65, 0.45, 1)
        )
        self.guess_button.bind(
            on_press=self.check_guess
        )

        self.again_button = Button(
            text="PLAY AGAIN",
            font_size=sp(18),
            size_hint_y=None,
            height=dp(52),
            background_normal="",
            background_color=(0.25, 0.35, 0.75, 1)
        )
        self.again_button.bind(
            on_press=self.restart
        )

        root.add_widget(title)
        root.add_widget(subtitle)
        root.add_widget(self.message)
        root.add_widget(self.attempt_label)
        root.add_widget(self.number)
        root.add_widget(self.guess_button)
        root.add_widget(self.again_button)

        return root

    def new_game(self):
        self.secret = random.randint(1, 10)
        self.attempts = 5
        self.finished = False

    def check_guess(self, instance):
        if self.finished:
            return

        if not self.number.text:
            self.message.text = "Enter a number first!"
            return

        guess = int(self.number.text)
        self.number.text = ""

        if guess < 1 or guess > 10:
            self.message.text = "Choose 1 to 10!"
            return

        self.attempts -= 1
        self.attempt_label.text = (
            f"Attempts left: {self.attempts}"
        )

        if guess == self.secret:
            self.message.text = "YOU WIN!"
            self.message.color = (0.2, 1, 0.5, 1)
            self.finish_game()

        elif self.attempts == 0:
            self.message.text = (
                f"YOU LOSE! Number: {self.secret}"
            )
            self.message.color = (1, 0.3, 0.3, 1)
            self.finish_game()

        elif guess < self.secret:
            self.message.text = "Too LOW! Try higher."

        else:
            self.message.text = "Too HIGH! Try lower."

    def finish_game(self):
        self.finished = True
        self.guess_button.disabled = True

    def restart(self, instance):
        self.new_game()
        self.message.text = "New game! Good luck!"
        self.message.color = (1, 0.85, 0.25, 1)
        self.attempt_label.text = "Attempts left: 5"
        self.guess_button.disabled = False
        self.number.text = ""


GuessGame().run()
