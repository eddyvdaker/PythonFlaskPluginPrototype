from abc import ABC, abstractmethod


class BaseTask(ABC):
    name: str

    @staticmethod
    def register(task_manager, task):
        task_manager.add_task(task)

    @abstractmethod
    def run(self):
        pass
