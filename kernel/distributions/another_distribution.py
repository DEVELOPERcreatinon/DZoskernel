class AnotherDistribution:
    def __init__(self, program_manager):
        self.pm = program_manager

    def setup(self):
        print("Setting up AnotherDistribution...")
        self.pm.load_program("another_program.py")  # Замените на реальный файл
        self.pm.create_process("AnotherProcess")
