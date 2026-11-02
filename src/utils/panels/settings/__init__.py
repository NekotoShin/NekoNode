"""
Copyright (C) 2024  猫戸シン

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from typing import List

import interactions

from ...const import PLACEHOLDER_EMOJI
from ...embed import Embed
from .guild import (
    CountingSettings,
    DvcSettings,
    GuildFunSettings,
    GuildGeneralSettings,
    GuildPreferencesSettings,
    GuildSafetySettings,
    GuildSettings,
    MessageSafetySettings,
)
from .personal import PersonalSettings

__all__ = (
    "CountingSettings",
    "DvcSettings",
    "GuildFunSettings",
    "GuildGeneralSettings",
    "GuildPreferencesSettings",
    "GuildSafetySettings",
    "GuildSettings",
    "MessageSafetySettings",
    "PersonalSettings",
    "Settings",
)


class Settings:
    """
    This class contains methods to generate embed responses and components for the settings command.
    """

    @classmethod
    def embed(cls) -> Embed:
        """
        Create a default settings embed.
        """
        return Embed("你可以在這裡設定機器人的各種功能或個人化選項。")

    @staticmethod
    def components(ctx: interactions.BaseContext) -> list[interactions.ActionRow]:
        """
        Generate components for the settings command.

        :param ctx: The context.
        :type ctx: interactions.BaseContext

        :return: The components.
        :rtype: List[interactions.ActionRow]
        """
        options = [
            interactions.StringSelectOption(
                label="NekoOS • 系統設定",
                value="placeholder",
                emoji=PLACEHOLDER_EMOJI,
                default=True,
            ),
        ]
        if ctx.guild:
            options.append(
                interactions.StringSelectOption(
                    label="伺服器設定", value="guild", description="管理伺服器的設定選項", emoji="🛠️"
                )
            )
        options.append(
            interactions.StringSelectOption(
                label="個人化選項", value="personal", description="修改你的專屬設定", emoji="👤"
            )
        )
        return [
            interactions.ActionRow(
                interactions.StringSelectMenu(
                    *options,
                    custom_id="settings:type_select",
                ),
            ),
        ]
