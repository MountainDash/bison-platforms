from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.platform import platform_manager

from .config import Config
from .platform import CeobeCanteen

__plugin_meta__ = PluginMetadata(
    "nonebot-bison-platform-ceobecanteen",
    description="CeobeCanteen platform for nonebot-bison",
    usage="pip install nonebot-bison-platform-ceobecanteen",
    type="library",
    homepage="https://github.com/MountainDash/bison-platforms/ceobecanteen",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

# TODO: Register your platform here
platform_manager.register(CeobeCanteen)  # type: ignore
