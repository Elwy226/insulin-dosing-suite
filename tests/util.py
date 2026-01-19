import importlib.util
import sys


def import_module(module_path):
    module_name = str(module_path).split('\\')[-1].replace('.py','')
    
    print(f"module_path: {module_path}")
    print(f"module_name: {module_name}")

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    print(f"spec: {spec}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    print(f"module: {module}")

    sys.modules[module_name] = module

    return module