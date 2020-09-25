from django.core.management.base import BaseCommand

from Shoes.models import ShoeType, ShoeColor


class Command(BaseCommand):
    help = "Pre-populate DB with initial values."

    def handle(self, *args, **options):

        ShoeType.objects.bulk_create([
        ShoeType(style='sneaker'),
        ShoeType(style='boot'),
        ShoeType(style='sandal'),
        ShoeType(style='dress'),
        ShoeType(style='other'),
        ])

        ShoeColor.objects.bulk_create([
        ShoeColor(color_name='RED'),
        ShoeColor(color_name='ORANGE'),
        ShoeColor(color_name='YELLOW'),
        ShoeColor(color_name='GREEN'),
        ShoeColor(color_name='BLUE'),
        ShoeColor(color_name='INDIGO'),
        ShoeColor(color_name='VIOLET'),
        ShoeColor(color_name='BLACK'),
        ShoeColor(color_name='WHITE')
        ])
        
        # ShoeColor.objects.bulk_create(shoe_colors)
        # ShoeType.objects.bulk_create(shoe_types)
        self.stdout.write(self.style.SUCCESS('Shoe records saved successfully.'))