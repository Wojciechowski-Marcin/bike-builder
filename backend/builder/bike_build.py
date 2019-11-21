from random import randint

from bikeparts.models import *


build_parts = [
    Frame,
    Fork,
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
    Saddle,
    Wheels
]


class BikeBuild:

    def __init__(self, bike_parts):
        self.bike_parts = bike_parts
        self.result = []

    def get_random_part(self, part_queryset):
        count = part_queryset.count()
        return part_queryset[randint(0, count-1)] if count else None

    def get_random_frame(self):
        frames = Frame.objects.all()
        return self.get_random_part(frames)

    def get_random_matching_fork(self, frame):
        matching_forks = frame.find_matching_forks()
        return self.get_random_part(matching_forks)

    def get_random_matching_crankset(self, frame):
        matching_cranksets = frame.find_matching_cranksets()
        return self.get_random_part(matching_cranksets)

    def get_random_matching_cassette(self, frame, crankset):
        matching_cassettes = crankset.find_matching_cassettes()
        return self.get_random_part(matching_cassettes)

    def get_random_matching_front_derailleur(self, frame, crankset):
        frame_matching_front_derailleurs = frame.find_matching_front_derailleurs()
        crankset_matching_front_derailleurs = crankset.find_matching_front_derailleurs()
        matching_front_derailleurs = frame_matching_front_derailleurs.intersection(
            crankset_matching_front_derailleurs)
        return self.get_random_part(matching_front_derailleurs)

    def get_random_matching_rear_derailleur(self, frame, crankset):
        frame_matching_rear_derailleurs = frame.find_matching_rear_derailleurs()
        crankset_matching_rear_derailleurs = crankset.find_matching_rear_derailleurs()
        matching_rear_derailleurs = frame_matching_rear_derailleurs.intersection(
            crankset_matching_rear_derailleurs)
        return self.get_random_part(matching_rear_derailleurs)

    def get_random_matching_brake(self, frame, fork):
        frame_matching_brakes = frame.find_matching_brakes()
        fork_matching_brakes = fork.find_matching_brakes()
        matching_brakes = frame_matching_brakes.intersection(
            fork_matching_brakes)
        return self.get_random_part(matching_brakes)

    def get_random_matching_brake_levers(self, brake):
        matching_brake_levers = brake.find_matching_brake_levers()
        return self.get_random_part(matching_brake_levers)

    def get_random_matching_derailleur_levers(self, crankset):
        matching_derailleur_levers = crankset.find_matching_derailleur_levers()
        return self.get_random_part(matching_derailleur_levers)

    def get_random_matching_rotor(self, frame):
        matching_rotors = frame.find_matching_rotors()
        return self.get_random_part(matching_rotors)

    def get_random_matching_stem(self, frame):
        matching_stems = frame.find_matching_stems()
        return self.get_random_part(matching_stems)

    def get_random_matching_handlebar(self, stem):
        matching_handlebars = stem.find_matching_handlebars()
        return self.get_random_part(matching_handlebars)

    def get_random_matching_seatpost(self, frame):
        matching_seatposts = frame.find_matching_seatposts()
        return self.get_random_part(matching_seatposts)

    def get_random_matching_saddle(self):
        saddles = Saddle.objects.all()
        return self.get_random_part(saddles)

    def get_random_matching_wheels(self, frame, fork):
        frame_matching_wheels = frame.find_matching_wheels()
        fork_matching_wheels = fork.find_matching_wheels()
        matching_wheels = frame_matching_wheels.intersection(
            fork_matching_wheels)
        return self.get_random_part(matching_wheels)

    def price(self):
        price = 0
        for part in self.result:
            price += part.price
        return price

    def weight(self):
        weight = 0
        for part in self.result:
            weight += part.weight
        return weight

    def score(self, budget, application):
        score = 0
        price = 0
        for part in self.result:
            score += part.weight
            price += part.price

        if price > budget:
            score += 5000
        else:
            score -= (budget-price)

        return score

    def build(self):
        result = []

        frame = self.bike_parts[0] or self.get_random_frame()
        result.append(frame)
        if not frame:
            return None

        fork = self.bike_parts[1] or self.get_random_matching_fork(frame)
        result.append(fork)
        if not fork:
            return None

        crankset = self.bike_parts[2] or \
            self.get_random_matching_crankset(frame)
        result.append(crankset)
        if not crankset:
            return None

        cassette = self.bike_parts[3] or \
            self.get_random_matching_cassette(frame, crankset)
        result.append(cassette)

        frontDerailleur = self.bike_parts[4] or \
            self.get_random_matching_front_derailleur(frame, crankset)
        result.append(frontDerailleur)

        rearDerailleur = self.bike_parts[5] or \
            self.get_random_matching_rear_derailleur(frame, crankset)
        result.append(rearDerailleur)

        brake = self.bike_parts[6] or \
            self.get_random_matching_brake(frame, fork)
        result.append(brake)
        if not brake:
            return None

        brakeLever = self.bike_parts[7] or \
            self.get_random_matching_brake_levers(brake)
        result.append(brakeLever)

        derailleurLever = self.bike_parts[8] or \
            self.get_random_matching_derailleur_levers(crankset)
        result.append(derailleurLever)

        rotor = self.bike_parts[9] or self.get_random_matching_rotor(frame)
        result.append(rotor)

        stem = self.bike_parts[10] or self.get_random_matching_stem(frame)
        result.append(stem)
        if not stem:
            return None

        handlebar = self.bike_parts[11] or \
            self.get_random_matching_handlebar(stem)
        result.append(handlebar)

        seatpost = self.bike_parts[12] or \
            self.get_random_matching_seatpost(frame)
        result.append(seatpost)

        saddle = self.bike_parts[13] or self.get_random_matching_saddle()
        result.append(saddle)

        wheels = self.bike_parts[14] or \
            self.get_random_matching_wheels(frame, fork)
        result.append(wheels)

        for r in result:
            if not r:
                return None

        self.result = result

        return result
