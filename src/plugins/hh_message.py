from nonebot import on_command, on_startswith, on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

import random

from zzxbot import ADMIN_LIST, get_module_state

module_name = "autohh"

hh_msg_6 = on_keyword("6")
hh_msg_9 = on_keyword("9")

@hh_msg_6.handle()
async def handle_hh_6(bot: Bot, event: Event, state: T_State):
    cq = "[CQ:image,file=b979a4711a0797e02a3aa685f425fa82.image,subType=1]"
    if get_module_state("autohh"):
        await hh_msg_6.send(Message(cq))

@hh_msg_9.handle()
async def handle_hh_9(bot: Bot, event: Event, state: T_State):
    cq = "[CQ:image,file=3ef8d95631e8ebd2711dd674f353f451.image,subType=0,url=https://gchat.qpic.cn/gchatpic_new/2834886052/1169712675-2255751708-3EF8D95631E8EBD2711DD674F353F451/0?term=3&amp;is_origin=0]"
    if get_module_state("autohh"):
        await hh_msg_9.send(Message(cq))
