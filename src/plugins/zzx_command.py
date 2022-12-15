from datetime import datetime
from nonebot import on_command, on_startswith, on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

import os

import zzxbot as zzxbot

from zzxbot import ADMIN_LIST, ZZX_TEMP, get_module_state
from .jrrp import load_jrrp, save_jrrp

zzx_cmd = on_startswith("/zzx")

def parser_args(args: str, uid: str):
    if len(args) == 1:
        return "ZzxBot - v{ver}\n开源: {source}\n此命令用法使用用法见/zzx help".format(ver=zzxbot.__version__, source=zzxbot.SOURCE_URL)
    elif args[1] == "help":
        return "/zzx - 获取Bot信息\n| /zzx info获得乐子信息集合\n| /zzx jrrp <uid> <value>修改某人的jrrp数据 (需要管理权限)"
    elif args[1] == "info":
        return "More info -> github (.) com / chenmy1903 / LunarClient-CN / wiki / 乐子"
    elif args[1] == "jrrp":
        if len(args) != 4:
            return "[Zzx Admin] 使用方法错误!\n正确方法: /zzx jrrp <uid> <value>"
        if uid not in ADMIN_LIST:
            return "[Zzx Admin] 你没有权限使用本命令"
        uid = args[2]
        try:
            int(uid)
        except:
            return "错误的uid"
        jrrp = load_jrrp()
        if uid not in jrrp:
            return "[Zzx Admin] {}未使用过此命令!".format(uid)
        info = jrrp[uid]
        format_date = f"{datetime.now().year}, {datetime.now().month}, {datetime.now().day}"
        info = {"luck": args[3], "usetime": format_date}
        jrrp[uid] = info
        save_jrrp(jrrp)
        return "[Zzx Admin] 操作成功执行"



@zzx_cmd.handle()
async def handle_zzx(bot: Bot, event: Event, state: T_State):
    if not get_module_state("zzx"):
        return
    msg = parser_args(event.get_plaintext().split(" "), event.get_user_id())
    await zzx_cmd.send(msg)
