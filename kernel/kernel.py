import random
import time
import threading
from queue import Queue
import os

class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.state = 'ready'
        self.priority = random.randint(1, 10)
        self.execution_time = random.randint(1, 5)
        self.memory_size = random.randint(1, 10)
        self.memory_address = None

    def run(self):
        self.state = 'running'
        print(f'Running: {self.name} (PID: {self.pid}) for {self.execution_time} seconds.')
        time.sleep(self.execution_time)
        self.state = 'terminated'
        print(f'Finished: {self.name} (PID: {self.pid})')

class MemoryManager:
    def __init__(self, size=100):
        self.memory = [None] * size

    def allocate(self, process):
        for i in range(len(self.memory)):
            if self.memory[i] is None and all(self.memory[j] is None for j in range(i, i + process.memory_size)):
                for j in range(i, i + process.memory_size):
                    self.memory[j] = process.pid
                process.memory_address = i
                return True
        return False

    def deallocate(self, process):
        if process.memory_address is not None:
            for j in range(process.memory_address, process.memory_address + process.memory_size):
                self.memory[j] = None

class Scheduler:
    def __init__(self):
        self.ready_queue = Queue()

    def add_process(self, process):
        self.ready_queue.put(process)

    def schedule(self):
        if not self.ready_queue.empty():
            return self.ready_queue.get()
        return None

class FileSystem:
    def __init__(self):
        self.files = {}
        self.directories = {}

    def load_program(self, filename):
        return self.files.get(filename, None)

    def add_file(self, filename, content):
        self.files[filename] = content

    def create_directory(self, dirname):
        if dirname not in self.directories:
            self.directories[dirname] = []
            print(f"Directory created: {dirname}")
        else:
            print(f"Directory {dirname} already exists.")

    def list_files(self, dirname):
        return self.directories.get(dirname, [])

class User:
    def __init__(self, username):
        self.username = username

class Kernel:
    def __init__(self):
        self.processes = []
        self.memory_manager = MemoryManager()
        self.scheduler = Scheduler()
        self.file_system = FileSystem()
        self.lock = threading.Lock()
        self.users = {}

    def create_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            print(f"User {username} created.")
        else:
            print(f"User {username} already exists.")

    def create_process(self, name):
        pid = len(self.processes) + 1
        process = Process(pid, name)
        self.processes.append(process)
        if self.memory_manager.allocate(process):
            self.scheduler.add_process(process)

    def run_program(self, filename):
        program = self.file_system.load_program(filename)
        if program:
            print(f"Executing program: {filename}")
            exec(program)  # Запуск программы
        else:
            print("Failed to run program.")

    def load_program_from_file(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                content = file.read()
                filename = os.path.basename(filepath)
                self.file_system.add_file(filename, content)
                print(f"Loaded program: {filename}")
        else:
            print(f"File {filepath} not found.")

    def load_dzos_file(self, filepath):
        if os.path.exists(filepath) and filepath.endswith('.DZos'):
            with open(filepath, 'r') as file:
                content = file.read()
                filename = os.path.basename(filepath)
                self.file_system.add_file(filename, content)
                print(f"Loaded DZos program: {filename}")
        else:
            print(f"File {filepath} not found or not a DZos file.")

    def run(self):
        while True:
            with self.lock:
                process = self.scheduler.schedule()
                if process:
                    process.run()
                    self.memory_manager.deallocate(process)
                else:
                    print('No ready processes to schedule.')
            time.sleep(1)
