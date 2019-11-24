import numpy as np
from copy import deepcopy

from random import randint, shuffle, uniform, choice

from bikeparts import models
from .model_dependences import model_dependences
from . import utils


build_parts = [
    models.Frame,
    models.Crankset,
    models.Cassette,
    models.FrontDerailleur,
    models.RearDerailleur,
    models.Brake,
    models.BrakeLever,
    models.DerailleurLever,
    models.Rotor,
    models.Stem,
    models.Handlebar,
    models.Seatpost,
    models.Wheels
]


class BikeBuild:

    def __init__(self, budget, bike_type, bike_parts):
        self.budget = budget
        self.bike_type = bike_type
        self.bike_parts = bike_parts
        self.build_parts = build_parts
        if bike_type == 'MTB' or bike_type == 'Dirt':
            self.build_parts.append(models.Shock)
            self.build_parts.append(models.Fork)
        self.build = None
        self.initial_build()

    def build_price(self, build):
        return sum([part.price for part in build.values()])

    def build_weight(self, build):
        return sum([part.weight for part in build.values()])

    @property
    def price(self):
        return sum([part.price for part in self.build.values()])

    @property
    def weight(self):
        return sum([part.weight for part in self.build.values()])

    @property
    def response(self):
        return {name: {'id': part.id} for name, part in self.build.items()}

    @property
    def score(self):
        score = self.weight
        price = self.price

        if price > self.budget:
            score += 50000

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
                # print(key, part_class_name)
                filtered_queryset = queryset.filter(
                    applications__name=self.bike_type)

                querysets.append(filtered_queryset)

        return utils.querysets_intersection(querysets)

    def validate_build(self, debug=True):
        for key, value in self.build.items():
            if not value:
                if debug:
                    print(key)
                return False
        return True

    def swap_random_part(self, max_tries=30):
        if max_tries == 0:
            return None

        build_length = len(self.build)
        random_build_part_name = choice(list(self.build.keys()))
        random_build_part_class = utils.igetattr(
            models, random_build_part_name)
        new_matching_parts = self.get_matching_parts(
            random_build_part_class)

        if new_matching_parts:
            random_new_part = utils.get_random_object(new_matching_parts)
            self.build[random_build_part_name] = random_new_part
            return random_new_part

        return self.swap_random_part(max_tries-1)

    def _temperature(self, fraction):
        return max(0.01, min(1, 1-fraction))

    def _acceptance_probability(self, cost, new_cost, temp):
        if cost > new_cost:
            return 1
        else:
            return np.exp(-float(new_cost-cost)/temp)

    def find_best_parts(self, max_steps=1000, debug=True):
        if not self.build:
            return
        build, cost = self.build, self.score
        builds, costs = [build], [cost]
        for step in range(max_steps):
            fraction = step / float(max_steps)
            temp = self._temperature(fraction)
            self.swap_random_part()
            new_build, new_cost = deepcopy(self.build), deepcopy(self.score)
            builds.append(new_build)
            costs.append(new_cost)
            if debug:
                print(
                    f'Step {step} : T = {"{0:.3f}".format(temp)}\t'
                    f'cost = {cost}\tnew_cost = {new_cost}')
            if self._acceptance_probability(
                    cost, new_cost, temp) > uniform(0, 1):
                build, cost = new_build, new_cost
            else:
                self.build = build

        budget_builds = self.filter_builds_under_budget(builds)
        self.build = self.best_build(budget_builds) if budget_builds else None

    def best_build(self, builds):
        sorted_builds = sorted(
            builds, key=lambda build: self.build_weight(build))
        return sorted_builds[0]

    def filter_builds_under_budget(self, builds):
        budget = self.budget
        budget_builds = []

        for build in builds:
            if self.build_price(build) <= self.budget:
                budget_builds.append(build)

        return budget_builds

    def initial_build(self, max_tries=200):
        if max_tries == 0:
            return None

        self.build = self.bike_parts

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
            return self.initial_build(max_tries-1)

        return self.build
