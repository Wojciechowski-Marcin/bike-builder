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
    Saddle,
    Wheels
]


class Command(BaseCommand):
    help = 'Imports database from excel sheet'

    # def add_arguments(self, parser):
    #     parser.add_argument('dupa', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        obj_index = 0

        for i in range(100*(len(build_parts)-1)-1):

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
                if not random_group else random_group.name[0:1].upper()
            model_name += '-'
            model_name += str(randint(1000, 9999))

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
                weight_multiplier = 0.5
            elif random_material.name == "Carbon":
                price_multiplier = 2.7
                weight_multiplier = 0.3
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

                for a in random_applications:
                    if a.name != 'MTB' and a.name != 'Dirt':
                        recommended_fork_travel = None
                        shock_type = None

                weight = randint(2500, 4000) * weight_multiplier
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
                frame.brake_rotor_type.set(brake_rotor_types)
                frame.save()

                self.stdout.write(self.style.SUCCESS(
                    f'Created Frame \n \
    brand={random_brand}, \n \
    group={random_group}, \n \
    model={model_name}, \n \
    material={random_material}, \n \
    weight={weight}, \n \
    color={random_color}, \n \
    price={price}, \n \
    applications={random_applications}, \n \
    wheel_types={wheel_types}, \n \
    headtube_type={headtube_type}, \n \
    seatclamp_type={seatclamp_type}, \n \
    bottom_bracket_type={bottom_bracket_type}, \n \
    brake_types={brake_types}, \n \
    rear_derailleur_types={rear_derailleur_types}, \n \
    front_derailleur_types={front_derailleur_types}, \n \
    axle_type={axle_type}, \n \
    brake_rotor_types={brake_rotor_types}, \n \
    recommended_fork_travel={recommended_fork_travel}, \n \
    shock_type={shock_type}\n'
                ))
            elif obj.class_name == 'Fork':
                pass
            elif obj.class_name == 'Shock':
                pass
            elif obj.class_name == 'Crankset':
                pass
            elif obj.class_name == 'Cassette':
                pass
            elif obj.class_name == 'FrontDerailleur':
                pass
            elif obj.class_name == 'RearDerailleur':
                pass
            elif obj.class_name == 'Brake':
                pass
            elif obj.class_name == 'BrakeLever':
                pass
            elif obj.class_name == 'DerailleurLever':
                pass
            elif obj.class_name == 'Rotor':
                pass
            elif obj.class_name == 'Handlebar':
                pass
            elif obj.class_name == 'Stem':
                pass
            elif obj.class_name == 'Saddle':
                pass
            elif obj.class_name == 'Seatpost':
                pass
            elif obj.class_name == 'Wheels':
                pass

        self.stdout.write(self.style.SUCCESS(
            'Successfully created database models'))
