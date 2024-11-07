class MyDistribution:
    def __init__(self, program_manager):
        self.pm = program_manager

    def setup(self):
        print("Setting up MyDistribution...")
        self.pm.load_program("my_program.py")  # Замените на реальный файл
        self.pm.create_process("MyProcess")
