from django.http import JsonResponse


class Builder:

    def __init__(self, budget, bike_type, bike_parts):
        self.budget = budget
        self.bike_type = bike_type
        self.bike_parts = bike_parts

    def make_response(self):
        return JsonResponse(self.bike_parts)
