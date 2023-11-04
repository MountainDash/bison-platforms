from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.platform import platform_manager

from .platform import Rss
from .config import Config

__plugin_meta__ = PluginMetadata(
    "nonebot-bison-platform-rss",
    description="Rss platform for nonebot-bison",
    usage="pip install nonebot-bison-platform-rss",
    type="library",
    homepage="https://github.com/MountainDash/bison-platforms/rss",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

# TODO: Register your platform here
platform_manager.register(Rss)  # type: ignore
