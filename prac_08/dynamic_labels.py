"""
Dynamic labels Kivy exercise
create separate labels dynamically for each name in list.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabels(App):
    """Kivy app to dynamically create labels for the names in a list."""
    new_label = StringProperty

    def __init__(self):
        """Constructs main app."""
        super().__init__()
        self.names = ['John', 'Adam', 'Mary', 'Michael']

    def build(self):
        """Build Kivy app GUI."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        """Dynamically create the labels for the app."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
