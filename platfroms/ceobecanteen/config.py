from nonebot import get_driver
from pydantic import BaseModel


class PlatformConfig(BaseModel):
    pass


class Config(BaseModel):
    bison_platforms: PlatformConfig


global_config = get_driver().config
platform_config = Config.parse_obj(global_config).bison_platforms
