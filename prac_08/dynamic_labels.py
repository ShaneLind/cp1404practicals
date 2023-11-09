"""
CP1404 Week 8 Practical
"""

from kivy.app import App
from kivy.lang import Builder

NAMES = ["name1", "name2", "name3", "name4"]


class DynamicLabels(App):
    """ DynamicLabels is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        return self.root

    def create_label(self):
        """Create labels from data and add them to the GUI."""
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
