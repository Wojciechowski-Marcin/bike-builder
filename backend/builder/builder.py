import time

from django.http import JsonResponse
from collections import OrderedDict

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

        self.bike_build = BikeBuild(
            self.budget, self.bike_type, self.bike_parts)

    def make_build(self):
        self.bike_build.find_best_parts()

    def make_response(self):
        self.make_build()
        if not self.bike_build.build:
            print("RETURNED NONE")
        sortedResponse = OrderedDict(sorted(
            self.bike_build.response.items(),
            key=lambda i: i[0])) \
            if self.bike_build.build else None
        return JsonResponse(sortedResponse) if sortedResponse \
            else JsonResponse({'error': "couldnt build"})
