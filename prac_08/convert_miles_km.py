from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRES = 1.60934


class ConvertMilesToKilometres(App):
    """ConvertMilesToKilometres is a Kivy app to convert miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Enter distance"
        return self.root

    def handle_conversion(self, value):
        """Handle conversion miles to km."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        """Get valid text input, cast to float, if error return 0."""
        try:
            value = float(self.root.ids.user_input.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        """Increment miles text input up or down by 1"""
        value = self.get_valid_miles() + change
        self.root.ids.user_input.text = str(value)
        self.handle_conversion(value)


ConvertMilesToKilometres().run()
