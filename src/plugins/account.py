from datetime import datetime
import os

from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent
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
    format_date = f"{datetime.now().year}, {datetime.now().month}, {datetime.now().day}"
    if not get_module_state("freeacc"):
        return
    acc_list = get_acc_list()
    if len(acc_list) == 0:
        await acc_cmd.send("小号获取失败, 还剩0个账号!")
    user = str(event.get_user_id())
    mod_settings = get_module_settings("freeacc")
    if "coins" not in mod_settings:
        mod_settings["coins"] = 200
        set_module_settings("freeacc", mod_settings)
    if "users" not in mod_settings:
        mod_settings["users"] = {}
        set_module_settings("freeacc", mod_settings)
    if "can-use-day" not in mod_settings:
        mod_settings["can-use-day"] = 3
        set_module_settings("freeacc", mod_settings)
    coins = get_module_settings("freeacc")["coins"]
    activate_users: dict = get_module_settings("freeacc")["users"]
    if user not in activate_users:
        await acc_cmd.send("[Account] 你没有购买小号机, 请联系管理员购买.")
        return
    user_info = activate_users[user]
    if "admin" not in user_info:
        user_info["admin"] = False
    if "coins" not in user_info:
        user_info["coins"] = 0
    u_coins = user_info["coins"]
    activate_users[user] = user_info
    mod_settings["users"] = activate_users
    set_module_settings("freeacc", mod_settings)
    if "daily-use" not in user_info or format_date != user_info["daily-use"][1]:
        user_info["daily-use"] = [mod_settings["can-use-day"], format_date]
    daily_use = user_info["daily-use"]
    daily_use[1] = format_date
    if daily_use[0] - 1 >= 0:
        u_coins += coins
        if daily_use > 0:
            daily_use[0] -= 1
    if u_coins - coins < 0 and not user_info["admin"]:
        await acc_cmd.send("[Account] 你的次数/硬币不足.")
        return
    r_coins = u_coins if user_info["admin"] else u_coins - coins
    user_info["coins"] = r_coins
    user_info["daily-use"] = daily_use
    activate_users[user] = user_info
    mod_settings["users"] = activate_users
    set_module_settings("freeacc", mod_settings)
    acc = acc_list.pop()
    save_acc_list(acc_list)
    await acc_cmd.send("[Account] 获取成功,消耗{coins}硬币, 账号信息: ".format(coins=coins) + acc + "\n还剩{al}张小号".format(al=len(acc_list)))
