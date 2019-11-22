from random import randint, shuffle

from bikeparts.models import *
from .model_dependences import model_dependences
from . import utils


build_parts = [
    Frame,
    Crankset,
    Cassette,
    FrontDerailleur,
    RearDerailleur,
    Brake,
    BrakeLever,
    DerailleurLever,
    Rotor,
    Stem,
    Handlebar,
    Seatpost,
    Wheels
]


class BikeBuild:

    def __init__(self, budget, bike_type, bike_parts):
        self.budget = budget
        self.bike_type = bike_type
        self.bike_parts = bike_parts
        self.build_parts = build_parts
        if bike_type == 'MTB' or bike_type == 'Dirt':
            self.build_parts.append(Shock)
            self.build_parts.append(Fork)
        self.build = None
        self.fill_build_with_initial_params()

    @property
    def price(self):
        return sum([part.price for part in self.build])

    @property
    def weight(self):
        return sum([part.weight for part in self.build])

    @property
    def response(self):
        return {name: part.id for name, part in self.build.items()}

    @property
    def score(self):
        score = self.weight
        price = self.price

        score = score+5000 if price > self.budget \
            else score-(self.budget-price)

        return score

    def get_matching_parts(self, part_class):
        querysets = []
        part_class_name = part_class.__name__.lower()
        dependency_keys = model_dependences[part_class_name]

        if len(self.build) == 0 or \
                not utils.is_any_key_in_dict(dependency_keys, self.build):
            return part_class.objects.all()

        shuffle(dependency_keys)
        for key in dependency_keys:
            dependent_part = self.build.get(key)
            if dependent_part:
                plural_class_name = 'wheels' if part_class_name == 'wheels' \
                    else part_class_name + 's'
                function_name = f'find_matching_{plural_class_name}'

                get_matching_parts_function = getattr(
                    dependent_part, function_name)

                queryset = get_matching_parts_function()
                filtered_queryset = queryset.filter(
                    applications__name=self.bike_type)

                querysets.append(queryset)

        return utils.querysets_intersection(querysets)

    def fill_build_with_initial_params(self):
        self.build = self.bike_parts

    def validate_build(self):
        for key, value in self.build.items():
            if not value:
                print(key)
                return False
        return True

    def initial_build(self):
        self.fill_build_with_initial_params()

        shuffle(self.build_parts)
        for build_part in self.build_parts:
            build_part_name = build_part.__name__.lower()
            part = self.build.get(build_part_name)
            if not part:
                matching_parts = self.get_matching_parts(build_part)
                found_part = None
                if matching_parts:
                    found_part = utils.get_random_object(matching_parts)
                self.build[build_part_name] = found_part

        if not self.validate_build():
            self.build = None

        return self.build
