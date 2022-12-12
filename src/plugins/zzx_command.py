from nonebot import on_command, on_startswith, on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

import os

zzx_cmd = on_startswith("/zzx")

# config_file = os.path.join

def parser_args(args: str):
    if len(args) == 1:
        return "github com / chenmy1903 / LunarClient-CN / wiki / 乐子\n使用用法见/zzx help"
    elif args[1] == "help":
        return "/zzx - 获得乐子的信息\n| /zzy获得乐子信息集合"


@zzx_cmd.handle()
async def handle_zzx(bot: Bot, event: Event, state: T_State):
    msg = parser_args(event.get_plaintext())
    await zzx_cmd.send(Message(msg))
