from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MDLabel(text="Welcome to WSCube Tech", halign="center")

# Corrected if statement with proper indentation
if __name__ == '__main__':
    Main_App().run()
