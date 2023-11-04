from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.platform import platform_manager

from .config import Config
from .platform import FF14

__plugin_meta__ = PluginMetadata(
    "nonebot-bison-platform-ff14",
    description="FF14 platform for nonebot-bison",
    usage="pip install nonebot-bison-platform-ff14",
    type="library",
    homepage="https://github.com/MountainDash/bison-platforms/ff14",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

# TODO: Register your platform here
platform_manager.register(FF14)  # type: ignore
