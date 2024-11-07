from gui import App

class GUIDistribution:
    def __init__(self, program_manager):
        self.pm = program_manager

    def setup(self):
        print("Setting up GUI Distribution...")
        app = App(self.pm)
        app.run()
