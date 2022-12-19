from nonebot import on_request
from nonebot.adapters.onebot.v11 import GroupRequestEvent, Event
from nonebot.adapters.cqhttp import Bot

import bilibili_api as bili

import nest_asyncio

import json
from .auto_welcome import get_black_list

from zzxbot import get_module_settings, get_module_state, set_module_settings

nest_asyncio.apply()

module_id = "autoaccept"

def on_crack(event: Event):
    return isinstance(event, GroupRequestEvent)

request = on_request(on_crack)

def get_accept_type(group):
    if group in get_module_settings(module_id)["groups"]:
        return get_module_settings(module_id)["groups"][group]["type"]
    return None

def bili_check(message: str, group: str):
    u = bili.user.User(get_module_settings(module_id)["groups"][group]["bili_id"])
    fans = bili.sync(u.get_followers())
    for fan in fans["list"]:
        if str(fan['mid']) in message:
            return True

@request.handle()
async def on_handle(bot: Bot, event: GroupRequestEvent):
    if not get_module_state(module_id):
        return
    if "groups" not in get_module_settings(module_id):
        set_module_settings(module_id, {"state": True, "groups": {}})
    group = str(event.group_id)
    user = event.get_user_id()
    accept_type = get_accept_type(group)
    raw = json.loads(event.json())
    comment = raw['comment']
    flag = raw['flag']
    sub_type = raw['sub_type']
    if sub_type != "add":
        return
    bl = get_black_list()
    if user in bl:
        await bot.set_group_add_request(
            flag=flag,
            sub_type=sub_type,
            approve=False,
            reason="退群了就不要再进来了L"
        )
    if accept_type == "bili_check":
        await bot.set_group_add_request(
            flag=flag,
            sub_type=sub_type,
            approve=bili_check(comment, group),
            reason="你没有关注[Bot]"
        )
