from django.core.management.base import BaseCommand

from wp_plugns.wordpresOrg.utils import WordPressPluginAPI
from wp_plugns.wordpresOrg.models import wordpres_org


class Command(BaseCommand):
    help = "Fetch plugins from WordPress.org and save them to the database"

    def handle(self, *args, **kwargs):
        api = WordPressPluginAPI()
        plugins = api.get_plugins_list(per_page=100)  # max 100 plugins per request

        for plugin_data in plugins:
            slug = plugin_data.get('slug')
            try:
                plugin, created = wordpres_org.objects.get_or_create(
                    slug=slug,
                    defaults={
                        'name': plugin_data.get('name'),
                        'description': plugin_data.get('description'),
                        'url': plugin_data.get('homepage'),
                        'zipfile': plugin_data.get('download_link'),
                        'screenshot': plugin_data.get('screenshot_url'),
                        'fivestars': plugin_data.get('rating'),
                        'last_updated': plugin_data.get('last_updated'),
                        'tested': plugin_data.get('tested'),
                        'requires': plugin_data.get('requires'),
                        'ratings': plugin_data.get('ratings'),
                        'downloaded': plugin_data.get('downloaded'),
                        'tags': plugin_data.get('tags')
                    }
                )
                if created:
                    self.stdout.write(f"Added new plugin: {plugin.name}")
                else:
                    self.stdout.write(f"Plugin already exists: {plugin.name}")
            except Exception as e:
                self.stderr.write(f"Failed to save plugin {slug}: {e}")