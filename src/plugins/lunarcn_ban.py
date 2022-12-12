from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

import requests

from zzxbot import get_module_state

lunarcn_ban_cmd = on_startswith("/lunarcnban")

ban_url = "https://chenmy1903.github.io/LunarClient-CN/blacklist"

msg_start = "[LunarCN Ban] 已封禁{ban_len}人"
msg_ban = "{id}: {reason}"

def get_banlist():
    """Get zzx"""
    msg_list = []
    try:
        banlist = eval(requests.get(ban_url))
        print(banlist)
    except:
        banlist = []
    long_banlist = len(banlist)
    msg_list.append(msg_start.format(ban_len=long_banlist))
    loser: dict
    for loser in banlist:
        loser_id = list(loser.keys())[0]
        loser_info = list(loser.values())[0]
        loser_reason = loser_info["reason"]
        msg_list.append(msg_ban.format(id=loser_id, reason=loser_reason))
    return "\n".join(msg_list)

@lunarcn_ban_cmd.handle()
async def handle_lunarcn_ban(bot: Bot, event: Event, state: T_State):
    if not get_module_state("lunarcn_ban"):
        return
    ban_list = get_banlist()
    await lunarcn_ban_cmd.send(ban_list)
