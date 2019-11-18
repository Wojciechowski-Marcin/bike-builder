from django.http import JsonResponse
from bikeparts.models import *
from bikeproperties.models import *

from .bike_build import BikeBuild, build_parts


population_size = 100


class Builder:

    def __init__(self, budget, bike_type, bike_parts):
        self.budget = budget
        self.bike_type = bike_type
        self.bike_parts = [
            build_parts[index].objects.get(
                pk=bike_parts[build_parts[index].__name__.lower()])
            if bike_parts[build_parts[index].__name__.lower()] != -1
            else None
            for index in range(len(build_parts))]

        self.bike_build = BikeBuild(self.bike_parts)

        self.population = self.starting_population()

    def generate_random_build(self):
        self.bike_build.build()

    def starting_population(self):
        return [self.generate_random_build() for _ in range(population_size)]

    def make_build(self):
        pass

    def make_response(self):
        return JsonResponse({
            bike_part.class_name.lower(): bike_part.id
            for bike_part in self.bike_parts if bike_part},
            safe=False)
