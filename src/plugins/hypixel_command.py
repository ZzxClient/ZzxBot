from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

from zzxbot import API_TOKEN

import requests

hyp_cmd = on_startswith("/hyp")

__version__ = "1.0.0"

base_url = f"https://api.hypixel.net"
help_message = f"""/hyp <player> [args]
| 查询玩家的Hypixel信息 v{__version__}
"""

def get_player(player):
    url = base_url + "/player" + f"?key={API_TOKEN}&name=" + player
    try:
        raw_list = requests.get(url).content
    except:
        raw_list = 'Get player info error (In work)'
    return raw_list # In work (?)

def parser_args(msg: str):
    args = msg.split(" ")
    if len(args) == 0:
        return help_message
    elif len(args) == 1:
        return str(get_player(args[1]))
    else:
        return "[Hypixel] 参数错误, 请使用/hyp help查看用法!"
    

@hyp_cmd.handle()
async def hyp_handle(bot: Bot, event: Event, state: T_State):
    msg = parser_args(event.get_plaintext())
    await hyp_cmd.send(msg)
