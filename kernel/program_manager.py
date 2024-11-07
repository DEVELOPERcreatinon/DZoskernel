from kernel import Kernel

class ProgramManager:
    def __init__(self, kernel):
        self.kernel = kernel

    def load_program(self, filepath):
        if filepath.endswith('.DZos'):
            self.kernel.load_dzos_file(filepath)
        else:
            self.kernel.load_program_from_file(filepath)

    def run_program(self, filename):
        self.kernel.run_program(filename)

    def list_loaded_programs(self):
        print("Loaded programs:")
        for filename in self.kernel.file_system.files.keys():
            print(f"- {filename}")

    def create_process(self, name):
        self.kernel.create_process(name)

    def create_user(self, username):
        self.kernel.create_user(username)

    def run(self):
        self.kernel.run()
