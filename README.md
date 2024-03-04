# Plugin Prototype
This repository contains a small prototype for implementing a plugin system in a Python Flask application. This is done by using the importlib to dynamically import all modules from a given folder. Then register all subclasses of a given base class.


To add a new plugin, simply add a .py file to the plugins folder and add the following:
```python
from src.plugin import BaseTask

class MyTask(BaseTask):
    name = "MyTask"
    
    def run(self):
        pass    # YOUR CODE HERE

```
