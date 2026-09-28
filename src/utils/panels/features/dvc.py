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

import interactions

from src.utils.embed import Embed

from ...const import PLACEHOLDER_EMOJI
from ...discord import snowflake_time

__all__ = ("DvcPanel",)


class DvcPanel:
    """
    This class contains methods to generate embed responses and components for the dynamic voice channel panel.
    """

    @staticmethod
    def embed(owner_id: int, channel_id: int) -> Embed:
        """
        Create a default dynamic voice channel panel embed.
        """
        embed = Embed("你可以在這裡控制這個動態語音頻道。")
        embed.add_field(
            name="詳細資料",
            value=f"擁有者: <@{owner_id}>\n開啟時間: <t:{int(snowflake_time(channel_id))}:F>",
            inline=True,
        )
        return embed

    @staticmethod
    def components() -> list[interactions.ActionRow]:
        """
        Create components for the dynamic voice channel panel.
        """
        return [
            interactions.ActionRow(
                interactions.StringSelectMenu(
                    interactions.StringSelectOption(
                        label="NekoOS • 控制面板",
                        value="placeholder",
                        emoji=PLACEHOLDER_EMOJI,
                        default=True,
                    ),
                    interactions.StringSelectOption(
                        label="修改語音頻道名稱",
                        value="name",
                        emoji="📝",
                    ),
                    interactions.StringSelectOption(
                        label="修改語音頻道位元率",
                        value="bitrate",
                        emoji="🎙️",
                    ),
                    interactions.StringSelectOption(
                        label="修改語音頻道人數上限",
                        value="limit",
                        emoji="👤",
                    ),
                    interactions.StringSelectOption(
                        label="轉移語音頻道擁有權",
                        value="transfer",
                        emoji="🔄",
                    ),
                    interactions.StringSelectOption(
                        label="關閉語音頻道",
                        value="close",
                        emoji="🗑️",
                    ),
                    custom_id="dvc_panel:select",
                )
            )
        ]

    @staticmethod
    def name_modal(current: str) -> interactions.Modal:
        """
        Create a modal for the dynamic voice channel name settings.
        """
        return interactions.Modal(
            interactions.InputText(
                label="動態語音頻道 - 名稱",
                style=interactions.TextStyles.SHORT,
                placeholder="請輸入新的語音頻道名稱",
                value=current,
                custom_id="name",
                min_length=1,
                max_length=100,
            ),
            title="動態語音頻道 - 名稱",
            custom_id="dvc_panel:name",
        )

    @staticmethod
    def bitrate_modal(current: int, boost: int) -> interactions.Modal:
        """
        Create a modal for the dynamic voice channel bitrate settings.
        """
        max_bitrate = [96, 128, 256, 384][boost]
        return interactions.Modal(
            interactions.InputText(
                label=f"位元率 (8-{max_bitrate}kbps)",
                style=interactions.TextStyles.SHORT,
                placeholder="請輸入新的語音頻道位元率 (預設: 64kbps)",
                value=str(current // 1000),
                custom_id="bitrate",
                min_length=1,
                max_length=3,
            ),
            title="動態語音頻道 - 位元率",
            custom_id="dvc_panel:bitrate",
        )

    @staticmethod
    def limit_modal(current: int) -> interactions.Modal:
        """
        Create a modal for the dynamic voice channel limit settings.
        """
        return interactions.Modal(
            interactions.InputText(
                label="上限 (0-99, 0: 無上限)",
                style=interactions.TextStyles.SHORT,
                placeholder="請輸入新的語音頻道人數上限 (預設: 0)",
                value=str(current),
                custom_id="limit",
                min_length=1,
                max_length=2,
            ),
            title="動態語音頻道 - 人數上限",
            custom_id="dvc_panel:limit",
        )

    @staticmethod
    def transfer_embed() -> Embed:
        """
        Create an embed for the dynamic voice channel transfer settings.
        """
        return Embed("請選擇一個新的語音頻道擁有者。")

    @staticmethod
    def transfer_components(ori: int) -> list[interactions.ActionRow]:
        """
        Create components for the dynamic voice channel transfer settings.
        """
        return [
            interactions.ActionRow(
                interactions.UserSelectMenu(
                    custom_id=f"dvc_panel:transfer_select:{ori}",
                    placeholder="👤｜請選擇使用者",
                )
            ),
        ]
