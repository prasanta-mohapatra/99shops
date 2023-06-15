import os
import sys
from glob import glob
from importlib import import_module

from sqlmodel import SQLModel

# Add the parent directory to the sys path to allow imports from app
sys.path.append("..")  # Assuming the models folder is one level up

# Get the current directory (assuming __init__.py is in the models folder)
current_dir = os.path.dirname(__file__)
models_dir = os.path.abspath(os.path.join(current_dir, "..", "models"))

# Import all model files dynamically
model_files = glob(os.path.join(models_dir, "*.py"))
for file_path in model_files:
    file_name = os.path.basename(file_path)
    if file_name != "__init__.py":
        module_name = file_name[:-3]  # Remove the '.py' extension
        module_path = f"app.infrastructure.models.{module_name}"
        module = import_module(module_path)
        model_classes = [
            cls
            for cls in module.__dict__.values()
            if isinstance(cls, type) and issubclass(cls, SQLModel)
        ]

        # Do something with the model class, such as registering it or using it for migrations

# Get the target metadata
metadata = SQLModel.metadata
