import os

basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = "Plugin Prototype"
SECRET_KEY = "secret"

PLUGIN_FOLDER = os.path.join(basedir, "plugins")
if not os.path.exists(PLUGIN_FOLDER):
    os.makedirs(PLUGIN_FOLDER)
    if not os.path.exists(os.path.join(PLUGIN_FOLDER, "__init__.py")):
        with open(os.path.join(PLUGIN_FOLDER, "__init__.py"), "w") as f:
            f.write("")
