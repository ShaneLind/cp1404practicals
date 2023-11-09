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
        self.message = str(self.get_validated_miles())
        self.handle_conversion()

    def handle_conversion(self):
        """Handle conversion of miles to km"""
        result = self.get_validated_miles() * 1.609344
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value):
        """Handle press of up and down button"""
        try:
            new_value = self.get_validated_miles() + value
            self.root.ids.input_number.text = str(new_value)
            self.handle_conversion()
        except ValueError:
            self.message = 0.0
        except AttributeError:
            self.message = 0.0

    def get_validated_miles(self):
        """check if user input miles is valid"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0


ConvertMilesKm().run()
