# bison-themes

[Nonebot-Bison](https://github.com/MountainDash/nonebot-bison) 的平台仓库。

## 使用方法

安装对应的平台插件

```shell
pip install nonebot-bison-platform-<platform-name>
```

> [!NOTE]
> 请将 `<platform-name>` 替换为你想要安装的平台名称。
> 例如 `bilibili`, 则安装命令为 `pip install nonebot-bison-theme-bilibili`

在 `pyproject.toml` 中启用

```toml
[tool.nonebot]
plugin = [
    "nonebot_bison_platform_<platform-name>",
    # ...
]
```

> [!NOTE]
> bison 初始不会安装任何平台插件，需要手动安装。
> 或者使用 `nonebot-bison[all]` 安装所有平台插件。

## 平台一览

- arknights
- bilibili
- ceobecanteen
- ff14
- mcbbsnews
- ncm
- rss
- weibo
