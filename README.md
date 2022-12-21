# Zzx bot

我们大蛇的Bot太厉害了!

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
5. `/toggle <ModuleId>` | 切换模块状态 (无ModuleId)
6. 戳一戳 (ModuleId: poke)
7. 自动`呵呵` (ModuleId: autohh)
8. `/acc` | 小号机 (ModuleId: freeacc)
9. `/reload` | 刷新bot配置 (无ModuleId)

## 配置文件

每日人品 -> `./zzxtemp/jrrp.json`

Bot设置 -> `./zzx_config/config.json`

小号机小号(一行一个) -> `./zzxtemp/accounts.txt`

## 如何配置入群欢迎

1. 打开Bot配置文件
2. 找到`autowlc`
3. 找到`groups`, 然后添加`"群号": "欢迎内容"`
4. 如果配置无问题, autowlc就已经生效了

## 如何配置自动审核

1. 打开Bot配置文件
2. 找到`autoaccept`
3. 找到`groups`
4. 添加信息: `"群号": {"type": "模式", "message": "reject模式的信息", "bili_id": bili_check模式的bili验证目标uid}`

> 各种模式见[此处](#自动审核模式)

### 自动审核模式

#### reject

自动拒绝模式, 使用后会自动拒绝加群者的请求, 自定义消息为`message`

#### bili_check

自动检测bilibili关注模式, bili_id为受关注者的uid (int形式)
