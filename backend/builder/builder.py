import time

from django.http import JsonResponse
from bikeparts import models as bikeparts_models
from bikeproperties.models import *

from .bike_build import BikeBuild, build_parts


class Builder:

    def __init__(self, budget, bike_type, bike_parts):
        self.budget = budget
        self.bike_type = bike_type
        self.bike_parts = {name.lower(): getattr(
            bikeparts_models, name).objects.get(pk=part_id)
            for name, part_id in bike_parts.items() if part_id != -1}

        self.bike_build = self.initial_bike_build()

    def initial_bike_build(self):
        timeout = time.time() + 5
        bike_build = BikeBuild(self.budget, self.bike_type, self.bike_parts)
        build = None

        while not build:
            build = bike_build.initial_build()
            if time.time() > timeout:
                break

        return bike_build

    def make_build(self):
        return self.bike_build

    def make_response(self):
        build = self.make_build()
        if not build.build:
            print("RETURNED NONE")
        return JsonResponse(build.response) if build.build \
            else JsonResponse({'error': "couldnt build"})
