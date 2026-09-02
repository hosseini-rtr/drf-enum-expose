from django.core.management.base import BaseCommand
from src.registry import registry

class Command(BaseCommand):
    help = 'Check registered enums and their status'

    def handle(self, *args, **options):
        enums = registry.get_all_enums()
        self.stdout.write(self.style.SUCCESS('Registered Enums: '))
        self.stdout.write("=" * 50)

        for name , choices in enums.items():
            self.stdout.write(f"\n {name}:")
            self.stdout.write(f"   Values:{len(choices)}")

            for choice in choices:
                self.stdout.write(f'    - {choice['value']} : {choice["label"]}')
                self.stdout.write("\n" + "=" * 50)
        
        self.stdout.write(
            self.style.SUCCESS(f"✅ Total: {len(enums)} enums registered")
        )
