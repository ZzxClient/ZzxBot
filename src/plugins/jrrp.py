from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

import os

from datetime import datetime

import json

import random

from zzxbot import ZZX_TEMP

jrrp_cmd = on_startswith("jrrp")

jrrp_file = os.path.join(ZZX_TEMP, "jrrp.json")

if not os.path.isfile(jrrp_file):
    with open(jrrp_file, "w") as f:
        f.write("{}")

def load_jrrp():
    """Load jrrp from file"""
    with open(jrrp_file) as f:
        return json.load(f)

def save_jrrp(jrrp_data):
    """Dump jrrp to the file"""
    with open(jrrp_file, "w") as f:
        json.dump(jrrp_data, f)

def parser_args(msg: str, user_id: str):
    jrrp = load_jrrp()
    format_date = f"{datetime.now().year}, {datetime.now().month}, {datetime.now().day}"
    if user_id in jrrp and format_date == jrrp[user_id]["usetime"]:
        return f"[CQ:at,qq={user_id}] 你已经获取过人品值了!\n你的人品值是: {jrrp[user_id]['luck']}\n*仅供娱乐"
    luck = random.randint(0, 100)
    temp_msg = "[CQ:at,qq={uid}] 你的人品值是: {luck}\n*仅供娱乐"
    msg = temp_msg.format(uid = user_id, luck = luck)
    jrrp[user_id] = {"luck": luck, "usetime": format_date}
    save_jrrp(jrrp)
    return msg

@jrrp_cmd.handle()
async def handle_jrrp(bot: Bot, event: Event, state: T_State):
    msg = parser_args(event.get_plaintext(), event.get_user_id())
    await jrrp_cmd.send(Message(msg))
