# zzxBot main
import os
import json

__version__ = "1.0.0"
SOURCE_URL = "https: // github (.) com / ZzxClient / ZzxBot"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZZX_TEMP = os.path.join(BASE_DIR, "zzxtemp")
ZZX_CONFIG = os.path.join(BASE_DIR, "zzx_config", "config.json")

ADMIN_LIST = ["674764353", "2834886052", "120721645", "2394439039",
              "2214646206", "691365317", "2932749515", "3454176276", "3562992533"]


API_TOKEN = "13742eba-eb71-4e60-be55-7ce6e4eb1382"

# init start
if not os.path.isdir(ZZX_TEMP):
    os.makedirs(ZZX_TEMP)
if not os.path.isdir(os.path.dirname(ZZX_CONFIG)):
    os.makedirs(os.path.dirname(ZZX_CONFIG))
if not os.path.isfile(ZZX_CONFIG):
    with open(ZZX_CONFIG, "w") as f:
        f.write("{}")
# init end

# def start
def get_module_state(module: str):
    """获取组件的启用状态"""
    config = load_config()
    if module in config:
        if "state" not in config[module]:
            set_module_state(module, True)
        return config[module]["state"]
    else:
        init_module(module)
        return True

def init_module(module: str):
    """初始化模块"""
    config = load_config()
    config[module] = {"state": True}
    save_config(config)

def set_module_state(module: str, state: bool):
    """设置组件状态"""
    config = load_config()
    if module not in config:
        module_info = {"state": True}
        config[module] = module_info
    else:
        module_info = config[module]
        module_info["state"] = state
    config[module] = module_info
    save_config(config)

def get_module_settings(module: str):
    config = load_config()
    return config[module]

def set_module_settings(module: str, settings: dict):
    config = load_config()
    config[module] = settings
    save_config(config)

def save_config(config: dict):
    with open(ZZX_CONFIG, "w", encoding="utf-8") as f:
        json.dump(config, f)

def load_config() -> dict:
    with open(ZZX_CONFIG, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config
# def end

# Exception start
class BotModuleError(Exception):
    """模块错误"""
    message: message = ""

    def __init__(self, *args):
        self.message = "\n".join(args)

class BotModuleNotFoundError(BotModuleError):
    """无法找到模块错误"""
    pass

class BotModuleValueError(BotModuleError):
    """模块参数错误"""
    pass

class BotArgError(BotModuleError):
    """参数错误"""
    pass
# Exception end
