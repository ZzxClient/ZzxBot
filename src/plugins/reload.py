import time
from nonebot import on_startswith
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Event

from zzxbot import init as init_bot, load_config

reload_cmd = on_startswith("/reload")

def get_admins():
    """获取最新的管理员列表"""
    config = load_config()
    return config["zzxbot"]["admins"]

@reload_cmd.handle()
async def reload_handle(bot: Bot, event: Event, state: T_State):
    """reload the bot"""
    uid = event.get_user_id()
    if uid not in get_admins():
        await reload_cmd.send("[Reload] 你没有使用权限")
        return
    t = time.time()
    try:
        init_bot()
    except Exception as e:
        await reload_cmd.send("[Reload] 重新加载Bot失败, 错误类型: {}\n详细信息请查看console".format(type(e)))
    else:
        await reload_cmd.send("[Reload] Bot重新加载成功, 耗时: {}s".format(time.time() - t))
