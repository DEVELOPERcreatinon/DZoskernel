import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, program_manager):
        self.pm = program_manager
        self.root = tk.Tk()
        self.root.title("OS Simulation")

        self.label = tk.Label(self.root, text="Welcome to OS Simulation")
        self.label.pack()

        self.load_button = tk.Button(self.root, text="Load Program", command=self.load_program)
        self.load_button.pack()

        self.run_button = tk.Button(self.root, text="Run Program", command=self.run_program)
        self.run_button.pack()

        self.process_button = tk.Button(self.root, text="Create Process", command=self.create_process)
        self.process_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

    def load_program(self):
        # Здесь можно добавить логику для загрузки программы
        program_name = "example_program.py"  # Замените на реальный ввод
        self.pm.load_program(program_name)
        messagebox.showinfo("Info", f"Loaded program: {program_name}")

    def run_program(self):
        # Здесь можно добавить логику для запуска программы
        program_name = "example_program.py"  # Замените на реальный ввод
        self.pm.run_program(program_name)
        messagebox.showinfo("Info", f"Running program: {program_name}")

    def create_process(self):
        # Здесь можно добавить логику для создания процесса
        process_name = "NewProcess"  # Замените на реальный ввод
        self.pm.create_process(process_name)
        messagebox.showinfo("Info", f"Created process: {process_name}")

    def run(self):
        self.root.mainloop()
