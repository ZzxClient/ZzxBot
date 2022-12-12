# Zzx bot

我们张子曦大蛇的Bot太厉害了!

## 部署方法

下载python使用以下pip命令

```bat
pip install nonebot2 requests nb-cli
```

Clone此项目

切换到项目的目录并输入以下指令

```bat
nb run
```

## Bot功能

1. `/zzx [args]`查看Bot版本信息 (ModuleId: zzx)
2. 自动欢迎 (ModuleId: autowlc)
3. `/hyp <player> [args]` | hypixel查询(没做完) (ModuleId: hypixel)
4. `jrrp` | 每日人品 (ModuleId: jrrp)
5. `/lunarcnban` | LunarCN封禁获取(没做完) (ModuleId: lunarcn_ban)
6. `/toggle <ModuleId>` | 切换模块状态 (无ModuleId)
7. 戳一戳 (ModuleId: poke)
8. 自动`呵呵` (ModuleId: autohh)

## 配置文件

每日人品 -> `./zzxtemp/jrrp.json`

Bot设置 -> `./zzx_config/config.json`
