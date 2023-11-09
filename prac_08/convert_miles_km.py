"""
CP1404 Week 8 Practical
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKm(App):
    """ ConvertMilesKm is a Kivy App for converting miles to km """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.root.ids.user_input.text

    def handle_conversion(self, value):
        """Handle conversion of miles to km"""
        try:
            result = float(value) * 1.609344
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


ConvertMilesKm().run()
