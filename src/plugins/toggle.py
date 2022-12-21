"""切换模块启用状态
/toggle <module> <state>
"""
from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

from zzxbot import ADMIN_LIST, BotArgError, BotModuleNotFoundError, get_module_state, load_config, set_module_state

toggle_cmd = on_startswith("/toggle")

msg_temp = "[Toggle] Module {module} -> {state}"
msg_error_temp = "[Toggle] {error_message}"

def parser_cmd(arg: list):
    """解析参数"""
    if len(arg) == 2:
        module = arg[1]
        if module not in load_config():
            return None, BotModuleNotFoundError("Module {} not found".format(module))
        if "state" not in load_config()["module"]:
            return None, BotArgError("模块{}确实存在, 但是它无法被关闭.".format(module))
        state = get_module_state(module)
        set_module_state(module, (not state))
        return module, get_module_state(module)
    else:
        return None, BotArgError("Wrong use -> /toggle <module>")


@toggle_cmd.handle()
async def toggle(bot: Bot, event: Event, state: T_State):
    if event.get_user_id() not in ADMIN_LIST:
        await toggle_cmd.send("[Toggle] 你没有使用权限")
        return
    module, module_state = parser_cmd(event.get_plaintext().split(" "))
    if module:
        await toggle_cmd.send(msg_temp.format(module=module, state="开启" if module_state else "关闭"))
    else:
        await toggle_cmd.send(msg_error_temp.format(error_message=module_state.message))
