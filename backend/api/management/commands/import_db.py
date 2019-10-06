from django.core.management.base import BaseCommand, CommandError
from xlrd import open_workbook

from api.models import Fork


class Command(BaseCommand):
    help = 'Imports database from excel sheet'

    # def add_arguments(self, parser):
    #     parser.add_argument('dupa', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        book = open_workbook('/app/Bike-parts.xlsx')
        sheet = book.sheet_by_index(0)

        r = [sheet.cell(1, col_index).value for col_index in range(sheet.ncols)]
        
        fork = Fork(
            brand=r[0], model=r[1], price=r[2], application=r[3], 
            wheel_size=r[4], suspension_type=r[5], travel=r[6], 
            steerer_tube_diameter=r[7], axle_type=r[8], brake_mount=r[9], 
            weight=r[10], color=r[11])
        fork.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully imported database'))
        