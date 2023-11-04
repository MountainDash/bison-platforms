from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.platform import platform_manager

from .config import Config
from .platform import NewPlatform

__plugin_meta__ = PluginMetadata(
    "<platform_name>",
    description="<platform_description>",
    usage="<theme_usage>",
    type="library",
    homepage="https://github.com/MountainDash/bison-platforms/<platform_name>",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

# TODO: Register your platform here
platform_manager.register(NewPlatform)  # type: ignore
