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

from .....const import PLACEHOLDER_EMOJI
from .....embed import Embed
from ...utils import return_option
from .message import MessageSafetySettings

__all__ = ("GuildSafetySettings", "MessageSafetySettings")


class GuildSafetySettings:
    """
    This class contains methods to generate embed responses and components for the settings command.
    """

    @classmethod
    def embed(cls) -> Embed:
        """
        Create a safety settings embed.
        """
        return Embed("你可以在這裡為這個伺服器設定安全功能。")

    @staticmethod
    def components(ctx: interactions.ComponentContext) -> list[interactions.ActionRow]:
        """
        Generate components for the safety settings.

        :param ctx: The component context.
        :type ctx: interactions.ComponentContext

        :return: The components.
        :rtype: List[interactions.ActionRow]
        """
        return [
            interactions.ActionRow(
                interactions.StringSelectMenu(
                    interactions.StringSelectOption(
                        label="NekoOS • 安全功能設定",
                        value="placeholder",
                        emoji=PLACEHOLDER_EMOJI,
                        default=True,
                    ),
                    interactions.StringSelectOption(
                        label="訊息掃描",
                        value="message",
                        description="管理伺服器的訊息掃描設定",
                        emoji="🔍",
                    ),
                    return_option(),
                    custom_id="settings:safety_select",
                )
            )
        ]
