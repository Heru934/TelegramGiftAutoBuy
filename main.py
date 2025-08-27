import asyncio
import traceback

from pyrogram import Client

from app.core.banner import display_title, get_app_info, set_window_title
from app.core.callbacks import process_gift
from app.core import gift_check  
from app.notifications import send_start_message
from app.utils.detector import gift_monitoring
from app.utils.logger import info, error
from data.config import config, t, get_language_display

app_info = get_app_info()


class Application:
    @staticmethod
    async def run() -> None:
        set_window_title(app_info)
        display_title(app_info, get_language_display(config.LANGUAGE))

        async with Client(
                name=config.SESSION,
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                phone_number=config.PHONE_NUMBER,
                workdir="data",   
        ) as client:
            await send_start_message(client)
            await gift_check.start(client)
            await gift_monitoring(client, process_gift)

    @staticmethod
    def main() -> None:
        try:
            asyncio.run(Application.run())
        except KeyboardInterrupt:
            info(t("console.terminated"))
        except Exception:
            error(t("console.unexpected_error"))
            traceback.print_exc()


Application.main() if __name__ == "__main__" else None
