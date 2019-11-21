import time

from django.http import JsonResponse
from bikeparts.models import *
from bikeproperties.models import *

from .bike_build import BikeBuild, build_parts


population_size = 25


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

        self.population = []

    def starting_population(self):
        population = []
        timeout = time.time() + 15
        while len(population) < population_size:
            bike_build = BikeBuild(self.bike_parts)
            build = bike_build.build()
            if(build):
                population.append(bike_build)
            if time.time() > timeout:
                break
        return population

    def make_build(self):
        self.population = self.starting_population()
        self.population.sort(key=lambda x: x.score(
            self.budget, self.bike_type))
        for p in self.population:
            print(p.score(self.budget, self.bike_type))
        return self.population[0].result

    def make_response(self):
        build = self.make_build()
        return JsonResponse({
            bike_part.class_name.lower(): bike_part.id for bike_part in build},
            safe=False) if build else JsonResponse({'error': "couldnt build"})
