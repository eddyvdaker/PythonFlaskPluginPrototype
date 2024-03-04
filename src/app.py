from __future__ import annotations
import importlib
import inspect
import os
from flask import Flask, Blueprint, current_app
from typing import Dict, Optional, List

from src.task import BaseTask

bp = Blueprint("main", __name__)


class TaskManager:
    tasks: Dict[str: BaseTask] = {}

    def get_task(self, name: str) -> Optional[BaseTask]:
        return self.tasks.get(name)

    def add_task(self, task: BaseTask, name: Optional[str] = None, overwrite: bool = False):
        if name is None:
            name = task.name
        if name in self.tasks and not overwrite:
            raise ValueError(f"Task {name} already exists")
        self.tasks[name] = task

    def get_task_list(self) -> List[str]:
        return list(self.tasks.keys())

    def load_tasks_from_folder(self, folder: str):
        for file in os.listdir(folder):
            if file.endswith(".py"):
                module = importlib.import_module(f"src.plugins.{file[:-3]}")
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, BaseTask) and obj != BaseTask:
                        print(f"registering task - {name}: {obj}")
                        self.add_task(obj(), overwrite=True)


task_manager = TaskManager()


def create_app(config_obj: str = "src.config") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    app.register_blueprint(bp)

    task_manager.load_tasks_from_folder(app.config["PLUGIN_FOLDER"])

    return app


@bp.route("/")
def index():
    return "Hi"


@bp.route("/tasks")
def tasks():
    return {"tasks": task_manager.get_task_list()}


@bp.route("/run/<task>")
def run_task(task):
    t = task_manager.get_task(task)
    if t is None:
        return {"error": f"Task {task} not found"}, 404
    t.run()
    return {"status": "ok"}


@bp.route("/tasks/scan")
def scan_tasks():
    # Run to reload the plugins
    task_manager.load_tasks_from_folder(current_app.config["PLUGIN_FOLDER"])
    return {"status": "ok"}
