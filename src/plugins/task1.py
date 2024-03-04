from src.task import BaseTask


class Task1(BaseTask):
    name = "task1"

    def run(self):
        print("Task1 running")