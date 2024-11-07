import importlib
import os
from kernel import Kernel
from program_manager import ProgramManager

def load_distribution(pm, distribution_name):
    try:
        module = importlib.import_module(f'distributions.{distribution_name}')
        distribution_class = getattr(module, distribution_name.capitalize())
        distribution = distribution_class(pm)
        distribution.setup()
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading distribution: {e}")

def main():
    kernel = Kernel()
    program_manager = ProgramManager(kernel)

    # Создание пользователей
    program_manager.create_user("user1")
    program_manager.create_user("user2")

    # Загрузка дистрибутивов
    load_distribution(program_manager, "my_distribution")
    load_distribution(program_manager, "another_distribution")

    # Запуск менеджера программ
    program_manager.run()

if __name__ == "__main__":
    main()
