import json
import os

import pyfiglet


class BannerManager:
    @staticmethod
    def get_app_info(file_path="data/json/app.json"):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def create_banner(app_name: str) -> str:
        return pyfiglet.figlet_format(app_name, font="slant")

    @staticmethod
    def display_title(app_info: dict, language: str):
        banner = BannerManager.create_banner(app_info["title"])
        separator = "-" * 80
        description = (
            f"Language: \033[1m{language}\033[0m | "
            f"Build: \033[92mv{app_info['version']}\033[0m | "
            f"DEV: @{app_info['publisher']['contact']['telegram'][13:]}"
        )

        centered_banner = "\n".join([line.center(80) for line in banner.splitlines()])

        print(separator)
        print(centered_banner)
        print(separator)
        print(f"{description}".center(95))
        print(separator)

    @staticmethod
    def set_window_title(app_info: dict):
        title_text = f"{app_info['title']} by @{app_info['publisher']['contact']['telegram'][13:]}"
        os.name == 'nt' and os.system(f"title {title_text}")


get_app_info = BannerManager.get_app_info
display_title = BannerManager.display_title
set_window_title = BannerManager.set_window_title
