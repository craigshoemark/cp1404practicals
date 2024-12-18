from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Get text input, print greeting, clear and reset inputs."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle text state on button press."""
        print("Greet")
        self.root.ids.greet_button.text = "Hello :)"

        print("Test")
        self.root.ids.output_label.text = "Hello"

        print("Label test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_fields(self):
        """Clear text input, button and label text, return to original text."""
        self.root.ids.input_name.text = " "
        self.root.ids.greet_button.text = "Greet"
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
