from typing import Any
from functools import partial

from httpx import AsyncClient
from bs4 import BeautifulSoup as bs

from nonebot_bison.post import Post
from nonebot_bison.types import Target, RawPost, Category
from nonebot_bison.platform.platform import NewMessage, StatusChange
from nonebot_bison.utils.scheduler_config import SchedulerConfig


class ArknightsSchedConf(SchedulerConfig):
    name = "arknights"
    schedule_type = "interval"
    schedule_setting = {"seconds": 30}


class Arknights(NewMessage):
    categories = {1: "游戏公告"}
    platform_name = "arknights"
    name = "明日方舟游戏信息"
    enable_tag = False
    enabled = True
    is_common = False
    scheduler = ArknightsSchedConf
    has_target = False
    default_theme = "arknights"

    @classmethod
    async def get_target_name(cls, client: AsyncClient, target: Target) -> str | None:
        return "明日方舟游戏信息"

    async def get_sub_list(self, _) -> list[RawPost]:
        raw_data = await self.client.get("https://ak-webview.hypergryph.com/api/game/bulletinList?target=IOS")
        return raw_data.json()["data"]["list"]

    def get_id(self, post: RawPost) -> Any:
        return post["cid"]

    def get_date(self, _: RawPost) -> Any:
        return None

    def get_category(self, _) -> Category:
        return Category(1)

    async def parse(self, raw_post: RawPost) -> Post:
        raw_data = await self.client.get(
            f"https://ak-webview.hypergryph.com/api/game/bulletin/{self.get_id(post=raw_post)}"
        )
        raw_data = raw_data.json()["data"]

        announce_title = raw_data.get("header") if raw_data.get("header") != "" else raw_data.get("title")
        content = raw_data.get("content")
        banner_image_url = raw_data.get("bannerImageUrl")

        return Post(
            self,
            content,
            title=announce_title,
            nickname="明日方舟游戏内公告",
            images=[banner_image_url],
            compress=True,
        )


class AkVersion(StatusChange):
    categories = {2: "更新信息"}
    platform_name = "arknights"
    name = "明日方舟游戏信息"
    enable_tag = False
    enabled = True
    is_common = False
    scheduler = ArknightsSchedConf
    has_target = False
    default_theme = "brief"

    @classmethod
    async def get_target_name(cls, client: AsyncClient, target: Target) -> str | None:
        return "明日方舟游戏信息"

    async def get_status(self, _):
        res_ver = await self.client.get("https://ak-conf.hypergryph.com/config/prod/official/IOS/version")
        res_preanounce = await self.client.get(
            "https://ak-conf.hypergryph.com/config/prod/announce_meta/IOS/preannouncement.meta.json"
        )
        res = res_ver.json()
        res.update(res_preanounce.json())
        return res

    def compare_status(self, _, old_status, new_status):
        res = []
        ArkUpdatePost = partial(Post, self, "", nickname="明日方舟更新信息")
        if old_status.get("preAnnounceType") == 2 and new_status.get("preAnnounceType") == 0:
            res.append(ArkUpdatePost(title="登录界面维护公告上线（大概是开始维护了)"))
        elif old_status.get("preAnnounceType") == 0 and new_status.get("preAnnounceType") == 2:
            res.append(ArkUpdatePost(title="登录界面维护公告下线（大概是开服了，冲！）"))
        if old_status.get("clientVersion") != new_status.get("clientVersion"):
            res.append(ArkUpdatePost(title="游戏本体更新（大更新）"))
        if old_status.get("resVersion") != new_status.get("resVersion"):
            res.append(ArkUpdatePost(title="游戏资源更新（小更新）"))
        return res

    def get_category(self, _):
        return Category(2)

    async def parse(self, raw_post):
        return raw_post


class MonsterSiren(NewMessage):
    categories = {3: "塞壬唱片新闻"}
    platform_name = "arknights"
    name = "明日方舟游戏信息"
    enable_tag = False
    enabled = True
    is_common = False
    scheduler = ArknightsSchedConf
    has_target = False

    @classmethod
    async def get_target_name(cls, client: AsyncClient, target: Target) -> str | None:
        return "明日方舟游戏信息"

    async def get_sub_list(self, _) -> list[RawPost]:
        raw_data = await self.client.get("https://monster-siren.hypergryph.com/api/news")
        return raw_data.json()["data"]["list"]

    def get_id(self, post: RawPost) -> Any:
        return post["cid"]

    def get_date(self, _) -> None:
        return None

    def get_category(self, _) -> Category:
        return Category(3)

    async def parse(self, raw_post: RawPost) -> Post:
        url = f'https://monster-siren.hypergryph.com/info/{raw_post["cid"]}'
        res = await self.client.get(f'https://monster-siren.hypergryph.com/api/news/{raw_post["cid"]}')
        raw_data = res.json()
        content = raw_data["data"]["content"]
        content = content.replace("</p>", "</p>\n")
        soup = bs(content, "html.parser")
        imgs = [x["src"] for x in soup("img")]
        text = f'{raw_post["title"]}\n{soup.text.strip()}'
        return Post(
            self,
            text,
            images=imgs,
            url=url,
            nickname="塞壬唱片新闻",
            compress=True,
        )


class TerraHistoricusComic(NewMessage):
    categories = {4: "泰拉记事社漫画"}
    platform_name = "arknights"
    name = "明日方舟游戏信息"
    enable_tag = False
    enabled = True
    is_common = False
    scheduler = ArknightsSchedConf
    has_target = False
    default_theme = "brief"

    @classmethod
    async def get_target_name(cls, client: AsyncClient, target: Target) -> str | None:
        return "明日方舟游戏信息"

    async def get_sub_list(self, _) -> list[RawPost]:
        raw_data = await self.client.get("https://terra-historicus.hypergryph.com/api/recentUpdate")
        return raw_data.json()["data"]

    def get_id(self, post: RawPost) -> Any:
        return f'{post["comicCid"]}/{post["episodeCid"]}'

    def get_date(self, _) -> None:
        return None

    def get_category(self, _) -> Category:
        return Category(4)

    async def parse(self, raw_post: RawPost) -> Post:
        url = f'https://terra-historicus.hypergryph.com/comic/{raw_post["comicCid"]}/episode/{raw_post["episodeCid"]}'
        return Post(
            self,
            raw_post["subtitle"],
            title=f'{raw_post["title"]} - {raw_post["episodeShortTitle"]}',
            images=[raw_post["coverUrl"]],
            url=url,
            nickname="泰拉记事社漫画",
            compress=True,
        )
