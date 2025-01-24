import os
import django
import requests
from time import sleep
from django.db import transaction
from plugn_app.models import Plugin  # Django ORM modeli

class WordPressPluginAPI:
    """
    WordPress.org Plugin API bilan ishlash uchun sinf.
    """
    def __init__(self):
        self.base_url = "https://api.wordpress.org/plugins/info/1.2/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; CustomPluginFetcher/1.0)",
            "Accept": "application/json"
        }

    def get_plugins_list(self, page: int = 1, per_page: int = 100, browse: str = "popular") -> dict:
        """
        Sahifa bo'yicha plaginlar ro'yxatini olish.
        """
        params = {
            "action": "query_plugins",
            "request": {
                "page": page,
                "per_page": min(per_page, 100),
                "browse": browse,
                "fields": {
                    "name": True,
                    "slug": True,
                    "download_link": True,
                    "screenshot_url": True,
                    "owner": True,
                    "downloaded": True,
                    "rating": True,
                    "last_updated": True,
                    "homepage": True,
                }
            }
        }

        response = requests.post(self.base_url, headers=self.headers, json=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API so'rovi xatosi: {response.status_code}")

    def fetch_and_save_plugins(self, browse: str = "popular", max_pages: int = 5):
        """
        Plaginlarni olish va bazaga saqlash.
        """
        page = 1
        while page <= max_pages:
            try:
                data = self.get_plugins_list(page=page, browse=browse)
                plugins = data.get('plugins', [])

                if not plugins:
                    print(f"Sahifa {page}: Plaginlar topilmadi!")
                    break

                with transaction.atomic():
                    for plugin in plugins:
                        Plugin.objects.update_or_create(
                            slug=plugin["slug"],
                            defaults={
                                "url": plugin.get("homepage"),
                                "name": plugin.get("name"),
                                "zipfile": plugin.get("download_link"),
                                "screenshot": bool(plugin.get("screenshot_url")),
                                "elements": False,  # API ma'lumotida yo'q
                                "html": None,  # API ma'lumotida yo'q
                                "owner_name": plugin.get("owner"),
                                "unused": None,  # API ma'lumotida yo'q
                                "fivestars": plugin.get("rating"),
                                "last_updated": plugin.get("last_updated"),
                            }
                        )

                print(f"Sahifa {page}: {len(plugins)} ta plagin saqlandi.")
                page += 1
                sleep(1)  # API ni haddan tashqari yuklamaslik uchun

            except Exception as e:
                print(f"Sahifa {page} uchun xatolik: {e}")
                break

if __name__ == "__main__":
    from django.core.wsgi import get_wsgi_application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_wp_plugns.settings')
    django.setup()

    # API orqali ma'lumotlarni olish va saqlash
    api = WordPressPluginAPI()
    api.fetch_and_save_plugins(browse="popular", max_pages=10)  # 10 sahifa uchun