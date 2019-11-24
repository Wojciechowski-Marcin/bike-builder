from django.core.management.base import BaseCommand, CommandError

from bikeparts.models import *
from bikeproperties.models import *

from random import randint, choice, choices
from string import ascii_letters


build_parts = [
    Crankset,
    Cassette,
    FrontDerailleur,
    RearDerailleur,
    Brake,
    BrakeLever,
    DerailleurLever,

    Frame,
    Fork,
    Rotor,
    Stem,
    Handlebar,
    Seatpost,
    Wheels,
    Shock
]


class Command(BaseCommand):
    help = 'Imports database from excel sheet'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?')
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete models before creating',
        )

    def get_speed_compatibilities(self, exclude=""):

        speed_compatibility_count = SpeedCompatibility.objects.count()
        speed_compatibility = SpeedCompatibility.objects.all()[
            randint(0, speed_compatibility_count-1)]
        if speed_compatibility.speed_compatibility[0] == "1":
            if exclude == "1":
                speed_compatibilities = [SpeedCompatibility.objects.get(
                    speed_compatibility="2x" +
                    speed_compatibility.speed_compatibility[-2:]
                )]
            else:
                speed_compatibilities = SpeedCompatibility.objects.filter(
                    speed_compatibility__startswith="1")
        elif speed_compatibility.speed_compatibility == '2x7'\
                or speed_compatibility.speed_compatibility == '2x8':

            speed_compatibilities = SpeedCompatibility.objects.filter(
                speed_compatibility__in=["2x7", '2x8'])
        elif speed_compatibility.speed_compatibility == '2x9'\
                or speed_compatibility.speed_compatibility == '2x10':

            speed_compatibilities = SpeedCompatibility.objects.filter(
                speed_compatibility__in=["2x9", '2x10'])
        elif speed_compatibility.speed_compatibility == '3x7'\
            or speed_compatibility.speed_compatibility == '3x8'\
                or speed_compatibility.speed_compatibility == '3x6':

            speed_compatibilities = SpeedCompatibility.objects.filter(
                speed_compatibility__in=["3x6", '3x7', '3x8'])
        elif speed_compatibility.speed_compatibility == '3x9'\
                or speed_compatibility.speed_compatibility == '3x10':

            speed_compatibilities = SpeedCompatibility.objects.filter(
                speed_compatibility__in=["3x9", '3x10'])
        else:
            speed_compatibilities = [speed_compatibility]
        return speed_compatibilities

    def handle(self, *args, **kwargs):
        obj_index = 0

        count = kwargs['count'] or 100

        if kwargs['delete']:
            for cls in build_parts:
                cls.objects.all().delete()

        for i in range(count*(len(build_parts))-1):

            obj = build_parts[obj_index]
            if i % 100 == 99:
                obj_index = obj_index + 1 \
                    if obj_index < len(build_parts)-1 else len(build_parts)-1

            brand_count = Brand.objects.count()
            random_brand = Brand.objects.all()[randint(0, brand_count-1)]

            group_count = Group.objects.count()
            random_group = Group.objects.all()[randint(0, group_count-1)] \
                if not obj_index >= 7 else None

            model_name = ''.join(choice(ascii_letters).upper() for _ in range(2)) \
                if not random_group else random_group.name[0:2].upper()
            model_name += '-'
            model_name += str(randint(10000, 99999))

            material_count = Material.objects.count()
            random_material = Material.objects.all()[
                randint(0, material_count-1)]

            color_count = Color.objects.count()
            random_color = Color.objects.all()[randint(0, color_count-1)]

            application_count = Application.objects.count()
            random_applications = set([
                Application.objects.all()[randint(0, application_count-1)]
                for x in range(choices([1, 2], [0.8, 0.2])[0])
            ])

            if random_material.name == 'Aluminium':
                price_multiplier = 1.5
                weight_multiplier = 0.7
            elif random_material.name == "Carbon":
                price_multiplier = 2.7
                weight_multiplier = 0.5
            elif random_material.name == "Steel":
                price_multiplier = 1
                weight_multiplier = 1
            elif random_material.name == "Nickel":
                price_multiplier = 0.8
                weight_multiplier = 1.2

            if obj.__name__ == 'Frame':
                wheel_type_count = WheelType.objects.count()
                if range(choices([0, 1], [0.7, 0.3])[0]):
                    wheel_types = [
                        WheelType.objects.get(size=28),
                        WheelType.objects.get(size=29)
                    ]
                else:
                    wheel_types = [WheelType.objects.all()[
                        randint(0, wheel_type_count-1)]]

                rear_derailleur_type_count = RearDerailleurType.objects.count()
                rear_derailleur_types = set([
                    RearDerailleurType.objects.all()[randint(
                        0, rear_derailleur_type_count-1)]
                    for x in range(
                        choices([1, 2, 3, 4], [0.5, 0.3, 0.15, 0.05])[0])
                ])

                front_derailleur_type_count = FrontDerailleurType.objects.count()
                front_derailleur_types = set([
                    FrontDerailleurType.objects.all()[randint(
                        0, front_derailleur_type_count-1)]
                    for x in range(
                        choices([1, 2, 3, 4], [0.5, 0.3, 0.15, 0.05])[0])
                ])

                brake_types_count = BrakeType.objects.count()
                brake_types = set([
                    BrakeType.objects.all()[randint(
                        0, brake_types_count-1)]
                    for x in range(
                        choices([1, 2, 3, 4], [0.5, 0.3, 0.15, 0.05])[0])
                ])

                brake_rotor_type_count = BrakeRotorType.objects.count()
                random_brake_rotor = BrakeRotorType.objects.all()[
                    randint(0, brake_rotor_type_count-1)]
                brake_rotor_types = list(BrakeRotorType.objects.filter(
                    size__lte=random_brake_rotor.size))

                axle_type_count = AxleType.objects.count()
                axle_type = AxleType.objects.all()[
                    randint(0, axle_type_count-1)]

                shock_type_count = ShockType.objects.count()
                shock_type = ShockType.objects.all()[
                    randint(0, shock_type_count-1)]

                bottom_bracket_type_count = BottomBracketType.objects.count()
                bottom_bracket_type = BottomBracketType.objects.all()[
                    randint(0, bottom_bracket_type_count-1)]

                seatclamp_type_count = SeatclampType.objects.count()
                seatclamp_type = SeatclampType.objects.all()[
                    randint(0, seatclamp_type_count-1)]

                headtube_type_count = HeadtubeType.objects.count()
                headtube_type = HeadtubeType.objects.all()[
                    randint(0, headtube_type_count-1)]

                recommended_fork_travel = choice([
                    100, 110, 120, 130, 140, 150, 160, 170, 180, 190])

                mtb = True
                for a in random_applications:
                    if a.name != 'MTB' and a.name != 'Dirt':
                        mtb = False
                if not mtb:
                    recommended_fork_travel = None
                    shock_type = None

                weight = randint(1500, 3000) * weight_multiplier
                price = randint(150, 300) * price_multiplier

                frame = Frame(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    headtube_type=headtube_type,
                    seatclamp_type=seatclamp_type,
                    bottom_bracket_type=bottom_bracket_type,
                    axle_type=axle_type,
                    recommended_fork_travel=recommended_fork_travel,
                    shock_type=shock_type)
                frame.save()
                frame.applications.set(random_applications)
                frame.wheel_types.set(wheel_types)
                frame.brake_types.set(brake_types)
                frame.rear_derailleur_types.set(rear_derailleur_types)
                frame.front_derailleur_types.set(front_derailleur_types)
                frame.brake_rotor_types.set(brake_rotor_types)

                self.stdout.write(self.style.SUCCESS(f'Created {frame}'))
            elif obj.__name__ == 'Fork':
                wheel_type_count = WheelType.objects.count()
                if range(choices([0, 1], [0.7, 0.3])[0]):
                    wheel_types = [
                        WheelType.objects.get(size=28),
                        WheelType.objects.get(size=29)
                    ]
                else:
                    wheel_types = [WheelType.objects.all()[
                        randint(0, wheel_type_count-1)]]

                suspension_type = 'Oil' if choices(
                    [0, 1], [0.5, 0.5])[0] else 'Air'

                travel_choices = [100, 110, 120, 130,
                                  140, 150, 160, 170, 180, 190]
                travel_int = randint(2, len(travel_choices)-3)
                travels = travel_choices[travel_int-2:travel_int+2]

                headtube_type_count = HeadtubeType.objects.count()
                headtube_type = HeadtubeType.objects.all()[
                    randint(0, headtube_type_count-1)]

                axle_type_count = AxleType.objects.count()
                axle_type = AxleType.objects.all()[
                    randint(0, axle_type_count-1)]

                brake_types_count = BrakeType.objects.count()
                brake_types = set([
                    BrakeType.objects.all()[randint(
                        0, brake_types_count-1)]
                    for x in range(
                        choices([1, 2, 3, 4], [0.5, 0.3, 0.15, 0.05])[0])
                ])
                random_applications = set([
                    Application.objects.get(id=randint(3, 4))
                    for x in range(
                        choices([1, 2, 3, 4], [0.5, 0.3, 0.15, 0.05])[0])
                ])

                weight = randint(1500, 2000) * weight_multiplier
                price = randint(120, 280) * price_multiplier

                for travel in travels:
                    new_model_name = model_name + '_' + str(travel)
                    fork = Fork(
                        brand=random_brand,
                        group=random_group,
                        model=new_model_name,
                        material=random_material,
                        weight=weight,
                        color=random_color,
                        price=price,
                        suspension_type=suspension_type,
                        travel=travel,
                        headtube_type=headtube_type,
                        axle_type=axle_type,
                    )
                    fork.save()
                    fork.applications.set(random_applications)
                    fork.wheel_types.set(wheel_types)
                    fork.brake_types.set(brake_types)
                    self.stdout.write(self.style.SUCCESS(f'Created {fork}'))

            elif obj.__name__ == 'Shock':

                weight = randint(300, 900) * weight_multiplier
                price = randint(150, 300) * price_multiplier

                shock_type_count = ShockType.objects.count()
                shock_type = ShockType.objects.all()[
                    randint(0, shock_type_count-1)]

                suspension_type = 'Oil' if choices(
                    [0, 1], [0.5, 0.5])[0] else 'Air'

                random_applications = set([
                    Application.objects.get(id=randint(3, 4))
                    for x in range(
                        choices([1, 2, 3, 4], [0.5, 0.3, 0.15, 0.05])[0])
                ])

                shock = Shock(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    shock_type=shock_type,
                    suspension_type=suspension_type)
                shock.save()
                shock.applications.set(random_applications)
                self.stdout.write(self.style.SUCCESS(f'Created {shock}'))

            elif obj.__name__ == 'Crankset':

                weight = randint(700, 800) * weight_multiplier
                price = randint(40, 80) * price_multiplier

                speed_compatibilities = self.get_speed_compatibilities()

                bot = [20, 22, 24, 26, 28, 30, 32, 34]
                top = [36, 38, 40, 42, 46, 48, 50, 52, 54]

                gradiation = str(choice(bot)) + '-' + str(choice(top)) \
                    if not speed_compatibilities[0].speed_compatibility[0] == "1" \
                    else str(choice(bot))

                arm_lengths = [140, 150, 160, 170, 180, 190]
                arm_length = choice(arm_lengths)

                bottom_bracket_type_count = BottomBracketType.objects.count()
                bottom_bracket_type = BottomBracketType.objects.all()[
                    randint(0, bottom_bracket_type_count-1)]

                crankset = Crankset(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    gradiation=gradiation,
                    bottom_bracket_type=bottom_bracket_type,
                    arm_length=arm_length)
                crankset.save()
                crankset.applications.set(random_applications)
                crankset.speed_compatibilities.set(speed_compatibilities)
                self.stdout.write(self.style.SUCCESS(f'Created {crankset}'))

            elif obj.__name__ == 'Cassette':

                weight = randint(200, 250) * weight_multiplier
                price = randint(30, 50) * price_multiplier

                speed_compatibilities = self.get_speed_compatibilities()

                bot = [9, 10, 11, 12, 14]
                top = [25, 28, 30, 32, 34]

                gradiation = str(choice(bot)) + '-' + str(choice(top)) \
                    if not speed_compatibilities[0].speed_compatibility[0] == "1" \
                    else str(choice(bot))

                cassette = Cassette(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    gradiation=gradiation)
                cassette.save()
                cassette.applications.set(random_applications)
                cassette.speed_compatibilities.set(speed_compatibilities)
                self.stdout.write(self.style.SUCCESS(f'Created {cassette}'))
            elif obj.__name__ == 'FrontDerailleur':

                weight = randint(80, 120) * weight_multiplier
                price = randint(10, 20) * price_multiplier

                speed_compatibilities = self.get_speed_compatibilities(
                    exclude="1")

                front_derailleur_type_count = FrontDerailleurType.objects.count()
                front_derailleur_type = FrontDerailleurType.objects.all()[
                    randint(0, front_derailleur_type_count-1)]

                front_derailleur = FrontDerailleur(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    front_derailleur_type=front_derailleur_type)
                front_derailleur.save()
                front_derailleur.applications.set(random_applications)
                front_derailleur.speed_compatibilities.set(
                    speed_compatibilities)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {front_derailleur}'))
            elif obj.__name__ == 'RearDerailleur':

                weight = randint(180, 220) * weight_multiplier
                price = randint(10, 20) * price_multiplier

                speed_compatibilities = self.get_speed_compatibilities()

                rear_derailleur_type_count = RearDerailleurType.objects.count()
                rear_derailleur_type = RearDerailleurType.objects.all()[
                    randint(0, rear_derailleur_type_count-1)]

                rear_derailleur = RearDerailleur(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    rear_derailleur_type=rear_derailleur_type)
                rear_derailleur.save()
                rear_derailleur.applications.set(random_applications)
                rear_derailleur.speed_compatibilities.set(
                    speed_compatibilities)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {rear_derailleur}'))
            elif obj.__name__ == 'Brake':
                weight = randint(150, 300) * weight_multiplier
                price = randint(20, 80)

                brake_type_count = BrakeType.objects.count()
                brake_type = BrakeType.objects.all()[
                    randint(0, brake_type_count-1)]

                brake = Brake(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    brake_type=brake_type)
                brake.save()
                brake.applications.set(random_applications)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {brake}'))
            elif obj.__name__ == 'BrakeLever':

                weight = randint(150, 200) * weight_multiplier
                price = randint(10, 20)

                brake_type_count = BrakeType.objects.count()
                brake_type = BrakeType.objects.all()[
                    randint(0, brake_type_count-1)]

                random_applications = Application.objects.all()

                brake_lever = BrakeLever(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    brake_type=brake_type)
                brake_lever.save()
                brake_lever.applications.set(random_applications)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {brake_lever}'))
            elif obj.__name__ == 'DerailleurLever':

                weight = randint(150, 200) * weight_multiplier
                price = randint(10, 20)

                speed_compatibilities_tmp = self.get_speed_compatibilities()
                speed_compatibilities = speed_compatibilities_tmp if len(speed_compatibilities_tmp) == 1 \
                    else [speed_compatibilities_tmp[randint(0, len(speed_compatibilities_tmp)-1)]]

                derailleur_lever = DerailleurLever(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price)
                derailleur_lever.save()
                derailleur_lever.applications.set(random_applications)
                derailleur_lever.speed_compatibilities.set(
                    speed_compatibilities)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {derailleur_lever}'))
            elif obj.__name__ == 'Rotor':

                weight = randint(75, 100)
                price = randint(8, 25)

                brake_rotor_type_count = BrakeRotorType.objects.count()
                brake_rotor_type = BrakeRotorType.objects.all()[
                    randint(0, brake_type_count-1)]

                random_applications = Application.objects.all()

                rotor = Rotor(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    brake_rotor_type=brake_rotor_type)
                rotor.save()
                rotor.applications.set(random_applications)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {rotor}'))
            elif obj.__name__ == 'Handlebar':

                weight = randint(160, 200) * weight_multiplier
                price = randint(30, 50) * price_multiplier

                handlebar_type_count = HandlebarType.objects.count()
                handlebar_type = HandlebarType.objects.all()[
                    randint(0, handlebar_type_count-1)]

                widths = [590, 600, 610, 620, 630, 640, 650, 660,
                          670, 680, 690, 700, 710, 720, 730, 740, 750, 760]

                width = choice(widths)

                handlebar = Handlebar(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    handlebar_type=handlebar_type,
                    width=width)
                handlebar.save()
                handlebar.applications.set(random_applications)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {handlebar}'))
            elif obj.__name__ == 'Stem':

                weight = randint(140, 160) * weight_multiplier
                price = randint(20, 40) * price_multiplier

                handlebar_type_count = HandlebarType.objects.count()
                handlebar_type = HandlebarType.objects.all()[
                    randint(0, handlebar_type_count-1)]

                headtube_types = HeadtubeType.objects.all()

                lengths = [80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 140]
                length = choice(lengths)

                angles = [5, 10, 15, 355, 350, 345]
                angle = choice(angles)

                stem = Stem(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    handlebar_type=handlebar_type,
                    length=length,
                    angle=angle)
                stem.save()
                stem.applications.set(random_applications)
                stem.headtube_types.set(headtube_types)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {stem}'))
            elif obj.__name__ == 'Seatpost':

                weight = randint(100, 240) * weight_multiplier
                price = randint(40, 60) * price_multiplier

                seatclamp_type_count = SeatclampType.objects.count()
                seatclamp_type = SeatclampType.objects.all()[
                    randint(0, seatclamp_type_count-1)]

                lengths = [280, 290, 300, 310, 320, 330,
                           340, 350, 360, 370, 380, 390, 400]
                length = choice(lengths)

                mtb = True
                for a in random_applications:
                    if a.name != 'MTB' and a.name != 'Dirt':
                        mtb = False

                random_applications = Application.objects.all()

                travels = [175, 180, 185, 190, 195, 200]
                travel = choice(travels) if mtb and choices(
                    [0, 1], [0.7, 0.3])[0] else None

                if travel:
                    price *= 3
                    weight *= 1.5

                seatpost = Seatpost(
                    brand=random_brand,
                    group=random_group,
                    model=model_name,
                    material=random_material,
                    weight=weight,
                    color=random_color,
                    price=price,
                    seatclamp_type=seatclamp_type,
                    length=length,
                    travel=travel)
                seatpost.save()
                seatpost.applications.set(random_applications)
                self.stdout.write(self.style.SUCCESS(
                    f'Created {seatpost}'))
            elif obj.__name__ == 'Wheels':

                weight = randint(1000, 2000) * weight_multiplier
                price = randint(150, 400) * price_multiplier

                wheel_type_count = WheelType.objects.count()
                wheel_type = WheelType.objects.all()[
                    randint(0, wheel_type_count-1)]

                brake_type_count = BrakeType.objects.count()
                brake_types = set([
                    BrakeType.objects.all()[randint(0, brake_type_count-1)]
                    for _ in range(2)])

                axle_type_count = AxleType.objects.count()
                axle_types = set([
                    AxleType.objects.all()[randint(0, seatclamp_type_count-1)]
                    for _ in range(3)])

                brake_rotor_type_count = BrakeRotorType.objects.count()
                random_brake_rotor = BrakeRotorType.objects.all()[
                    randint(0, brake_rotor_type_count-1)]
                brake_rotor_types = BrakeRotorType.objects.filter(
                    mount_type=random_brake_rotor.mount_type)

                for axle_type in axle_types:
                    for brake_type in brake_types:
                        new_model_name = model_name + '_' + \
                            axle_type.axle_type + '_' + \
                            brake_type.mount_type[0] + brake_type.brake_type[0]
                        wheels = Wheels(
                            brand=random_brand,
                            group=random_group,
                            model=new_model_name,
                            material=random_material,
                            weight=weight,
                            color=random_color,
                            price=price,
                            wheel_type=wheel_type,
                            brake_type=brake_type,
                            axle_type=axle_type)
                        wheels.save()
                        wheels.applications.set(random_applications)
                        wheels.brake_rotor_types.set(brake_rotor_types)
                        self.stdout.write(self.style.SUCCESS(
                            f'Created {wheels}'))

        self.stdout.write(self.style.SUCCESS(
            'Successfully created database models'))
