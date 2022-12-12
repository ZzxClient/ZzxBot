from datetime import datetime
from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent
from nonebot.adapters.onebot.v11 import Message

from zzxbot import get_module_state, get_module_settings, set_module_settings

wlc = on_notice()

module_id = "autowlc"

def get_wlc_message(group: str, uid: str):
    cq_uid = "[CQ:at,qq={}] ".format(uid)
    if group in get_module_settings(module_id)["groups"]:
        return cq_uid + get_module_settings(module_id)["groups"][group]
    return None

@wlc.handle()
async def member_join(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    """Member join event"""
    if not get_module_state(module_id):
        return
    if "groups" not in get_module_settings(module_id):
        set_module_settings(module_id, {"state": True, "groups": {}})
    uid = event.get_user_id()
    group = str(event.group_id)
    msg = get_wlc_message(group, uid)
    if msg:
        await wlc.send(msg)

@wlc.handle()
async def member_leave(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    """Member leave event"""
    if not get_module_state(module_id):
        return
    await wlc.send("有人悄悄离开了.....")

get_module_state(module_id)
