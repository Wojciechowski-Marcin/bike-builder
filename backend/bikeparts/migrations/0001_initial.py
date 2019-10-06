# Generated by Django 2.2.1 on 2019-10-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('brake_type', models.CharField(choices=[('DISC', 'Disc'), ('RIM', 'Rim')], max_length=4)),
                ('mount_type', models.CharField(choices=[('IS', 'IS'), ('PM', 'PM'), ('P', 'Pivots')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrakeLever',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('brake_type', models.CharField(choices=[('DISC', 'Disc'), ('RIM', 'Rim')], max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cassette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('gradiation', models.CharField(max_length=35)),
                ('speed_compatibility', models.CharField(choices=[('3x6', '3x6'), ('3x7', '3x7'), ('3x8', '3x8'), ('3x9', '3x9'), ('3x10', '3x10'), ('3x11', '3x11'), ('2x8', '2x8'), ('2x9', '2x9'), ('2x10', '2x10'), ('2x11', '2x11'), ('2x12', '2x12'), ('1x10', '1x10'), ('1x11', '1x11'), ('1x12', '1x12')], max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Crankset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('gradiation', models.CharField(max_length=8)),
                ('speed_compatibility', models.CharField(choices=[('3x6', '3x6'), ('3x7', '3x7'), ('3x8', '3x8'), ('3x9', '3x9'), ('3x10', '3x10'), ('3x11', '3x11'), ('2x8', '2x8'), ('2x9', '2x9'), ('2x10', '2x10'), ('2x11', '2x11'), ('2x12', '2x12'), ('1x10', '1x10'), ('1x11', '1x11'), ('1x12', '1x12')], max_length=4)),
                ('bottom_bracket_size', models.DecimalField(choices=[(68, '68mm'), (73, '73mm')], decimal_places=0, max_digits=2)),
                ('arm_length', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DerailleurLever',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('speed_compatibility', models.CharField(choices=[('3x6', '3x6'), ('3x7', '3x7'), ('3x8', '3x8'), ('3x9', '3x9'), ('3x10', '3x10'), ('3x11', '3x11'), ('2x8', '2x8'), ('2x9', '2x9'), ('2x10', '2x10'), ('2x11', '2x11'), ('2x12', '2x12'), ('1x10', '1x10'), ('1x11', '1x11'), ('1x12', '1x12')], max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('wheel_size', models.DecimalField(choices=[(20, '20"'), (24, '24"'), (26, '26"'), (27.5, '27.5"'), (29, '29"')], decimal_places=1, max_digits=3)),
                ('suspension_type', models.CharField(choices=[('AIR', 'Air'), ('OIL', 'Oil Spring')], max_length=16)),
                ('travel', models.DecimalField(decimal_places=0, max_digits=3)),
                ('steerer_tube_diameter', models.CharField(choices=[('1 1/8 - 1 1/2', '1 1/8 - 1 1/4"'), ('1 1/8 - 1 1/2', '1 1/8 - 1 1/2"'), ('1 1/8', '1 1/8"'), ('1 1/4', '1 1/4"'), ('1 1/3', '1 1/3"'), ('1 1/2', '1 1/2"')], max_length=16)),
                ('axle_type', models.CharField(choices=[('9x100', '9x100'), ('15x100', '15x100'), ('15x110', '15x110')], max_length=16)),
                ('brake_mount_type', models.CharField(choices=[('IS', 'IS'), ('PM', 'PM'), ('P', 'Pivots')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('size', models.DecimalField(decimal_places=1, max_digits=2)),
                ('wheel_size', models.DecimalField(choices=[(20, '20"'), (24, '24"'), (26, '26"'), (27.5, '27.5"'), (29, '29"')], decimal_places=1, max_digits=2)),
                ('headtube_type', models.CharField(choices=[('TP', 'Tapered'), ('ECT', 'Conventional Threaded'), ('EC', 'Conventional Threadless'), ('ZS', 'ZeroStack'), ('IS', 'Integrated')], max_length=3)),
                ('headtube_diameter', models.CharField(choices=[('1 1/8 - 1 1/2', '1 1/8 - 1 1/4"'), ('1 1/8 - 1 1/2', '1 1/8 - 1 1/2"'), ('1 1/8', '1 1/8"'), ('1 1/4', '1 1/4"'), ('1 1/3', '1 1/3"'), ('1 1/2', '1 1/2"')], max_length=13)),
                ('seatclamp_size', models.DecimalField(choices=[(28.6, '28.6mm'), (30.0, '30.0mm'), (31.8, '31.8mm'), (34.9, '34.9mm'), (36.4, '36.4mm')], decimal_places=1, max_digits=3)),
                ('bottom_bracket_size', models.DecimalField(choices=[(68, '68mm'), (73, '73mm')], decimal_places=0, max_digits=2)),
                ('brake_mount_type', models.CharField(choices=[('IS', 'IS'), ('PM', 'PM'), ('P', 'Pivots')], max_length=2)),
                ('rear_derailleur_mount_type', models.CharField(choices=[('H', 'Hanger'), ('B', 'Bolt-on')], max_length=1, null=True)),
                ('front_derailleur_mount_type', models.CharField(choices=[('CL', 'Clamp'), ('DM', 'Direct Mount')], max_length=2, null=True)),
                ('max_rotor_size', models.DecimalField(choices=[(140, '140mm'), (160, '160mm'), (180, '180mm'), (200, '200mm')], decimal_places=0, max_digits=3, null=True)),
                ('recommended_fork_travel', models.DecimalField(decimal_places=0, max_digits=3, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FrontDerailleur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('speed_compatibility', models.CharField(choices=[('3x6', '3x6'), ('3x7', '3x7'), ('3x8', '3x8'), ('3x9', '3x9'), ('3x10', '3x10'), ('3x11', '3x11'), ('2x8', '2x8'), ('2x9', '2x9'), ('2x10', '2x10'), ('2x11', '2x11'), ('2x12', '2x12'), ('1x10', '1x10'), ('1x11', '1x11'), ('1x12', '1x12')], max_length=4)),
                ('mount_type', models.CharField(choices=[('CL', 'Clamp'), ('DM', 'Direct Mount')], max_length=2, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Handlebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('width', models.DecimalField(decimal_places=0, max_digits=3)),
                ('diameter', models.DecimalField(choices=[(25.4, '25.4'), (31.8, '31.8')], decimal_places=1, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RearDerailleur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('speed_compatibility', models.CharField(choices=[('3x6', '3x6'), ('3x7', '3x7'), ('3x8', '3x8'), ('3x9', '3x9'), ('3x10', '3x10'), ('3x11', '3x11'), ('2x8', '2x8'), ('2x9', '2x9'), ('2x10', '2x10'), ('2x11', '2x11'), ('2x12', '2x12'), ('1x10', '1x10'), ('1x11', '1x11'), ('1x12', '1x12')], max_length=4)),
                ('mount_type', models.CharField(choices=[('H', 'Hanger'), ('B', 'Bolt-on')], max_length=1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rotor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('size', models.DecimalField(choices=[(140, '140mm'), (160, '160mm'), (180, '180mm'), (200, '200mm')], decimal_places=0, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Saddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('length', models.DecimalField(decimal_places=0, max_digits=3)),
                ('width', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seatpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('length', models.DecimalField(decimal_places=0, max_digits=3)),
                ('diameter', models.DecimalField(decimal_places=1, max_digits=3)),
                ('travel', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('length', models.DecimalField(decimal_places=0, max_digits=3)),
                ('angle', models.DecimalField(decimal_places=0, max_digits=3)),
                ('headtube_diameter', models.CharField(choices=[('1 1/8 - 1 1/2', '1 1/8 - 1 1/4"'), ('1 1/8 - 1 1/2', '1 1/8 - 1 1/2"'), ('1 1/8', '1 1/8"'), ('1 1/4', '1 1/4"'), ('1 1/3', '1 1/3"'), ('1 1/2', '1 1/2"')], max_length=13)),
                ('handlebar_diameter', models.DecimalField(choices=[(25.4, '25.4'), (31.8, '31.8')], decimal_places=1, max_digits=3)),
                ('mount', models.CharField(choices=[('TP', 'Tapered'), ('ECT', 'Conventional Threaded'), ('EC', 'Conventional Threadless'), ('ZS', 'ZeroStack'), ('IS', 'Integrated')], max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wheels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('group', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('material', models.CharField(max_length=32, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('application', models.CharField(choices=[('CITY', 'City'), ('ROAD', 'Road'), ('TREKKING', 'Trekking'), ('MTB', 'All Mountain'), ('XC', 'Cross Country'), ('DH', 'Downhill'), ('ENDURO', 'Enduro')], max_length=32)),
                ('size', models.DecimalField(choices=[(20, '20"'), (24, '24"'), (26, '26"'), (27.5, '27.5"'), (29, '29"')], decimal_places=1, max_digits=3)),
                ('brake_type', models.CharField(choices=[('DISC', 'Disc'), ('RIM', 'Rim')], max_length=4)),
                ('hub', models.CharField(choices=[('CASETTE', 'Casette'), ('FREEWHEEL', 'Freewheel')], max_length=9)),
            ],
            options={
                'verbose_name_plural': 'Wheels',
            },
        ),
    ]