from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.six import text_type
from compressor.cache import get_offline_manifest, write_offline_manifest

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('engine', nargs='+', type=text_type)
    
    def handle(self, *args, **options):
        manifest = {}
        for engine in options['engine']:
            call_command("compress", engine=engine)
            manifest.update(get_offline_manifest())
        write_offline_manifest(manifest)
