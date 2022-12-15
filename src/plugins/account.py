import os

from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.onebot.v11 import Message

from zzxbot import ADMIN_LIST, ZZX_TEMP, get_module_settings, get_module_state, set_module_settings

from .jrrp import load_jrrp, save_jrrp

acc_file = os.path.join(ZZX_TEMP, "accounts.txt")

acc_cmd = on_startswith("/acc")

def get_acc_list():
    acc_list = []
    if not os.path.isfile(acc_file):
        with open(acc_file, "w", encoding="utf-8") as f:
            acc_list = []
    with open(acc_file, "r", encoding="utf-8") as f:
        for line in f.read().replace("\r", "").split("\n"):
            if line.strip():
                acc_list.append(line)
    return acc_list

def save_acc_list(acc_list):
    with open(acc_file, "w", encoding="utf-8") as f:
        f.write("\n".join(acc_list))


@acc_cmd.handle()
async def on_handle(bot: Bot, event: Event, state: T_State):
    if not get_module_state("freeacc"):
        return
    acc_list = get_acc_list()
    if len(acc_list) == 0:
        await acc_cmd.send("小号获取失败, 还剩0个账号!")
    user = event.get_user_id()
    mod_settings = get_module_settings("freeacc")
    if "coins" not in mod_settings:
        mod_settings["coins"] = 200
        set_module_settings("freeacc", mod_settings)
    coins = get_module_settings("freeacc")["coins"]
    jrrp = load_jrrp()
    if user not in jrrp:
        u_coins = 0
    else:
        u_coins = jrrp[user]["coins"]
    if u_coins - coins < 0 and (user not in ADMIN_LIST):
        await acc_cmd.send("[Account] 你的硬币不足, 快去使用jrrp进行签到")
        return
    r_coins = u_coins - coins
    jrrp_info = jrrp[user]
    jrrp_info["coins"] = r_coins
    jrrp[user] = jrrp_info
    save_jrrp(jrrp)
    acc = acc_list.pop()
    save_acc_list(acc_list)
    await acc_cmd.send("[Account] 获取成功,消耗{coins}硬币, 账号信息: ".format(coins=coins) + acc + "\n还剩{al}张小号".format(al=len(acc_list)))
    
