from typing import Optional, Tuple

from pyrogram import Client


class UserHelper:
    @staticmethod
    async def get_user_balance(client: Client) -> int:
        try:
            return await client.get_stars_balance()
        except Exception:
            return 0

    @staticmethod
    async def get_recipient_info(app: Client, chat_id: int) -> Tuple[str, str]:
        try:
            user = await app.get_chat(chat_id)
            username = user.username or ""

            format_rules = {
                'with_username': {
                    'condition': lambda: bool(username),
                    'formatter': lambda: f"@{username.strip()}"
                },
                'numeric_id': {
                    'condition': lambda: isinstance(chat_id, int) or str(chat_id).isdigit(),
                    'formatter': lambda: str(chat_id)
                },
                'string_fallback': {
                    'condition': lambda: True,
                    'formatter': lambda: f"@{chat_id}"
                }
            }

            recipient_info = next(
                (rule['formatter']() for rule in format_rules.values() if rule['condition']()),
                str(chat_id)
            )

            return recipient_info, username
        except Exception:
            return str(chat_id), ""

    @staticmethod
    def format_user_reference(user_id: int, username: Optional[str] = None) -> str:
        reference_rules = {
            'with_username': {
                'condition': lambda: bool(username),
                'formatter': lambda: f"@{username} | <code>{user_id}</code>"
            },
            'numeric_user': {
                'condition': lambda: isinstance(user_id, int) or (isinstance(user_id, str) and user_id.isdigit()),
                'formatter': lambda: f'<a href="tg://user?id={user_id}">{user_id}</a>'
            },
            'string_fallback': {
                'condition': lambda: True,
                'formatter': lambda: f"@{user_id}" if isinstance(user_id, str) else str(user_id)
            }
        }

        return next(
            (rule['formatter']() for rule in reference_rules.values() if rule['condition']()),
            str(user_id)
        )


get_user_balance = UserHelper.get_user_balance
get_recipient_info = UserHelper.get_recipient_info
format_user_reference = UserHelper.format_user_reference
