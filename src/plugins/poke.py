"""戳一戳事件"""
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Message, PokeNotifyEvent
from nonebot.matcher import Matcher
from nonebot.adapters.cqhttp import Bot
from nonebot.rule import to_me

from zzxbot import get_module_state

import random

poke = on_notice(rule=to_me())

event_list = ["qwq", "28pot"]

@poke.handle()
async def poke(bot: Bot, matcher: Matcher, event: PokeNotifyEvent):
    if not get_module_state("poke"):
        return
    poke_event = random.choice(event_list)
    if poke_event == "qwq":
        # bot.set_group_ban(group_id=event.group_id, user_id=event.get_user_id(), duration=60)
        await matcher.finish(Message("[CQ:at,qq={}] qwq?".format(event.get_user_id())))
    elif poke_event == "28pot":
        await matcher.finish(Message("[CQ:at,qq={}] 主播小心我28pot你".format(event.get_user_id())))
