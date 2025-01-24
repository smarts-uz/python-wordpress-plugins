import requests

class WordPressPluginAPI:
    def __init__(self):
        self.base_url = "https://api.wordpress.org/plugins/info/1.2/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; CustomPluginFetcher/1.0)",
            "Accept": "application/json"
        }

    def get_plugins_list(self, page=1, per_page=100, browse="popular"):
        params = {
            "action": "query_plugins",
            "request": {
                "page": page,
                "per_page": per_page,
                "browse": browse,
                "fields": {
                    "description": True,
                    "tested": True,
                    "requires": True,
                    "rating": True,
                    "ratings": True,
                    "downloaded": True,
                    "download_link": True,
                    "last_updated": True,
                    "homepage": True,
                    "tags": True
                }
            }
        }
        response = requests.post(self.base_url, headers=self.headers, json=params)
        if response.status_code == 200:
            return response.json().get('plugins', [])
        else:
            raise Exception(f"API request failed with status code: {response.status_code}")