import json
from django.core.management.base import BaseCommand

from items.models import Tovar, ClientTovar, MatchedTovar


class Command(BaseCommand):
    help = 'Import tovar and client_tovar data from json and match them'

    def handle(self, *args, **kwargs):
        with open('json_data/tovar.json', 'r', encoding='utf-8') as f:
            tovar_data = json.load(f)
        with open('json_data/client_tovar.json', 'r', encoding='utf-8') as f:
            client_tovar_data = json.load(f)
        Tovar.objects.all().delete()
        ClientTovar.objects.all().delete()
        MatchedTovar.objects.all().delete()
        for item in tovar_data:
            Tovar.objects.create(name_prep=item['name_prep'], ean13=item['ean13'])
        for item in client_tovar_data:
            ClientTovar.objects.create(name_prep=item['name_prep'], ean13=item['ean13'])
        for tovar in Tovar.objects.all():
            matched_clients = ClientTovar.objects.filter(ean13=tovar.ean13)
            if matched_clients.exists():
                matched = MatchedTovar.objects.create(tovar=tovar, quantity=matched_clients.count())
                matched.client_tovars.add(*matched_clients)
        self.stdout.write(self.style.SUCCESS('Import and matching completed'))
