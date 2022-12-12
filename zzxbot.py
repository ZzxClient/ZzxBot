# zzxBot main
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZZX_TEMP = os.path.join(BASE_DIR, "zzxtemp")
ZZX_CONFIG = os.path.join(BASE_DIR, "zzx_config", "config.json")

ADMIN_LIST = ["674764353", "2834886052", "120721645", "2394439039",
              "2214646206", "691365317", "2932749515", "3454176276"]


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
    with open(ZZX_CONFIG, "r") as f:
        config = json.load(f)
    if module in config:
        if "state" not in config[module]:
            set_module_state(module, True)
        return config[module]["state"]

def set_module_state(module: str, state: bool):
    """设置组件状态"""
    with open(ZZX_CONFIG, "r") as f:
        config = json.load(f)
    if module not in config:
        module_info = {"state": True}
        config[module] = module_info
    else:
        module_info = config[module]
        module_info["state"] = True
    config[module] = module_info
# def end
