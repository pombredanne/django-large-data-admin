import importlib

def get_model(model_str):
    model = model_str.split(".")
    class_name = model[-1]
    module_name = ".".join(model[:-1])
    module = importlib.import_module(module_name)
    return getattr(module, class_name)
