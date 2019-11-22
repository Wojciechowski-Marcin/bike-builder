from django.db import models

import bikeproperties.models


class Category(models.Model):

    name = models.CharField(
        max_length=32)

    # TODO make category model
    slug = models.SlugField()


class BikePart(models.Model):

    brand = models.ForeignKey(
        'bikeproperties.Brand',
        on_delete=models.PROTECT,
        related_name='%(class)ss')

    group = models.ForeignKey(
        'bikeproperties.Group',
        on_delete=models.PROTECT,
        related_name='%(class)ss',
        null=True,
        blank=True)

    model = models.CharField(
        max_length=32,
        unique=True)

    material = models.ForeignKey(
        'bikeproperties.Material',
        on_delete=models.PROTECT,
        related_name='%(class)ss',
        null=True,
        blank=True)

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2)

    color = models.ForeignKey(
        'bikeproperties.Color',
        on_delete=models.PROTECT,
        related_name='%(class)ss',
        null=True,
        blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2)

    applications = models.ManyToManyField(
        bikeproperties.models.Application,
        related_name='%(class)ss')

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        name = f'<{self.class_name}> {self.brand.name} '
        if self.group:
            name += f'{self.group.name} '
        name += f'{self.model}'
        return name

    class Meta:
        abstract = True


class Frame(BikePart):

    wheel_types = models.ManyToManyField(
        bikeproperties.models.WheelType,
        related_name='frames')

    headtube_type = models.ForeignKey(
        'bikeproperties.HeadtubeType',
        on_delete=models.PROTECT,
        related_name='frames')

    seatclamp_type = models.ForeignKey(
        'bikeproperties.SeatclampType',
        on_delete=models.PROTECT,
        related_name='frames')

    bottom_bracket_type = models.ForeignKey(
        'bikeproperties.BottomBracketType',
        on_delete=models.PROTECT,
        related_name='frames')

    brake_types = models.ManyToManyField(
        bikeproperties.models.BrakeType,
        related_name='frames')

    rear_derailleur_types = models.ManyToManyField(
        bikeproperties.models.RearDerailleurType,
        related_name='frames')

    front_derailleur_types = models.ManyToManyField(
        bikeproperties.models.FrontDerailleurType,
        related_name='frames')

    axle_type = models.ForeignKey(
        'bikeproperties.AxleType',
        on_delete=models.PROTECT,
        related_name='frames')

    brake_rotor_types = models.ManyToManyField(
        'bikeproperties.BrakeRotorType',
        related_name='frames')

    recommended_fork_travel = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True)

    shock_type = models.ForeignKey(
        'bikeproperties.ShockType',
        on_delete=models.PROTECT,
        related_name='frames',
        null=True,
        blank=True)

    def find_matching_forks(self):
        qs = Fork.objects.filter(
            headtube_type=self.headtube_type).filter(
                wheel_types__in=self.wheel_types.all()).filter(
                    axle_type=self.axle_type)
        if self.recommended_fork_travel:
            qs.filter(travel=self.recommended_fork_travel)
        return qs

    def find_matching_shocks(self):
        return Shock.objects.filter(
            shock_type=self.shock_type) \
            if self.shock_type else []

    def find_matching_cranksets(self):
        return Crankset.objects.filter(
            bottom_bracket_type=self.bottom_bracket_type)

    def find_matching_frontderailleurs(self):
        return FrontDerailleur.objects.filter(
            front_derailleur_type__in=self.front_derailleur_types.all())

    def find_matching_rearderailleurs(self):
        return RearDerailleur.objects.filter(
            rear_derailleur_type__in=self.rear_derailleur_types.all())

    def find_matching_brakes(self):
        return Brake.objects.filter(
            brake_type__in=self.brake_types.all())

    def find_matching_brakelevers(self):
        return BrakeLever.objects.filter(
            brake_type__in=self.brake_types.all())

    def find_matching_rotors(self):
        return Rotor.objects.filter(
            brake_rotor_type__in=self.brake_rotor_types.all())

    def find_matching_stems(self):
        return Stem.objects.filter(
            headtube_types=self.headtube_type)

    def find_matching_seatposts(self):
        return Seatpost.objects.filter(
            seatclamp_type=self.seatclamp_type)

    def find_matching_wheels(self):
        return Wheels.objects.filter(
            wheel_type__in=self.wheel_types.all()).filter(
                axle_type=self.axle_type).filter(
                    brake_type__in=self.brake_types.all())


class Fork(BikePart):

    SUSPENSION_TYPES = [
        ('Oil', 'Oil'),
        ('Air', 'Air')
    ]

    wheel_types = models.ManyToManyField(
        bikeproperties.models.WheelType,
        related_name='forks')

    suspension_type = models.CharField(
        max_length=16,
        choices=SUSPENSION_TYPES)

    travel = models.DecimalField(
        max_digits=3,
        decimal_places=0)

    headtube_type = models.ForeignKey(
        'bikeproperties.HeadtubeType',
        on_delete=models.PROTECT,
        related_name='forks')

    axle_type = models.ForeignKey(
        'bikeproperties.AxleType',
        on_delete=models.PROTECT,
        related_name='forks')

    brake_types = models.ManyToManyField(
        bikeproperties.models.BrakeType,
        related_name='forks')

    def find_matching_frames(self):
        return Frame.objects.filter(
            headtube_type=self.headtube_type).filter(
                wheel_types__in=self.wheel_types.all()).filter(
                    axle_type=self.axle_type)

    def find_matching_brakes(self):
        return Brake.objects.filter(
            brake_type__in=self.brake_types.all())

    def find_matching_brakelevers(self):
        return BrakeLever.objects.filter(
            brake_type__in=self.brake_types.all())

    def find_matching_stems(self):
        return Stem.objects.filter(
            headtube_types=self.headtube_type)

    def find_matching_wheels(self):
        return Wheels.objects.filter(
            wheel_type__in=self.wheel_types.all()).filter(
                axle_type=self.axle_type).filter(
                    brake_type__in=self.brake_types.all())


class Crankset(BikePart):

    gradiation = models.CharField(
        max_length=8)

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='cranksets')

    bottom_bracket_type = models.ForeignKey(
        'bikeproperties.BottomBracketType',
        on_delete=models.PROTECT,
        related_name='cranksets')

    arm_length = models.DecimalField(
        max_digits=3,
        decimal_places=0)

    def find_matching_frames(self):
        return Frame.objects.filter(
            bottom_bracket_type=self.bottom_bracket_type)

    def find_matching_cassettes(self):
        return Cassette.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_frontderailleurs(self):
        return FrontDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_rearderailleurs(self):
        return RearDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_derailleurlevers(self):
        return DerailleurLever.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())


class Cassette(BikePart):

    gradiation = models.CharField(
        max_length=35)

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='cassettes')

    def find_matching_cranksets(self):
        return Crankset.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_frontderailleurs(self):
        return FrontDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_rearderailleurs(self):
        return RearDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_derailleurlevers(self):
        return DerailleurLever.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())


class FrontDerailleur(BikePart):

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='front_derailleurs')

    front_derailleur_type = models.ForeignKey(
        'bikeproperties.FrontDerailleurType',
        on_delete=models.PROTECT,
        related_name='front_derailleurs')

    def find_matching_frames(self):
        return Frame.objects.filter(
            front_derailleur_types=self.front_derailleur_type)

    def find_matching_cassettes(self):
        return Cassette.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_cranksets(self):
        return Crankset.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_rearderailleurs(self):
        return RearDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_derailleurlevers(self):
        return DerailleurLever.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())


class RearDerailleur(BikePart):

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='rear_derailleurs')

    rear_derailleur_type = models.ForeignKey(
        'bikeproperties.RearDerailleurType',
        on_delete=models.PROTECT,
        related_name='rear_derailleurs')

    def find_matching_frames(self):
        return Frame.objects.filter(
            rear_derailleur_types=self.rear_derailleur_type)

    def find_matching_cassettes(self):
        return Cassette.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_cranksets(self):
        return Crankset.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_frontderailleurs(self):
        return FrontDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_derailleurlevers(self):
        return DerailleurLever.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())


class Brake(BikePart):

    brake_type = models.ForeignKey(
        'bikeproperties.BrakeType',
        on_delete=models.PROTECT,
        related_name='brakes')

    def find_matching_frames(self):
        return Frame.objects.filter(
            brake_types=self.brake_type)

    def find_matching_forks(self):
        return Fork.objects.filter(
            brake_types=self.brake_type)

    def find_matching_brakelevers(self):
        return BrakeLever.objects.filter(
            brake_type=self.brake_type)

    def find_matching_wheels(self):
        return Wheels.objects.filter(
            brake_type=self.brake_type)


class BrakeLever(BikePart):

    brake_type = models.ForeignKey(
        'bikeproperties.BrakeType',
        on_delete=models.PROTECT,
        related_name='brake_levers')

    def find_matching_frames(self):
        return Frame.objects.filter(
            brake_types=self.brake_type)

    def find_matching_forks(self):
        return Fork.objects.filter(
            brake_types=self.brake_type)

    def find_matching_brakes(self):
        return Brake.objects.filter(
            brake_type=self.brake_type)

    def find_matching_wheels(self):
        return Wheels.objects.filter(
            brake_type=self.brake_type)


class DerailleurLever(BikePart):

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='derailleur_levers')

    def find_matching_cassettes(self):
        return Cassette.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_cranksets(self):
        return Crankset.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_frontderailleurs(self):
        return FrontDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())

    def find_matching_rearderailleurs(self):
        return RearDerailleur.objects.filter(
            speed_compatibilities__in=self.speed_compatibilities.all())


class Rotor(BikePart):

    brake_rotor_type = models.ForeignKey(
        'bikeproperties.BrakeRotorType',
        on_delete=models.PROTECT,
        related_name='rotors')

    def find_matching_frames(self):
        return Frame.objects.filter(
            brake_rotor_types=self.brake_rotor_type)

    def find_matching_wheels(self):
        return Wheels.objects.filter(
            brake_rotor_types=self.brake_rotor_type)


class Stem(BikePart):

    length = models.DecimalField(
        max_digits=3,
        decimal_places=0)

    angle = models.DecimalField(
        max_digits=3,
        decimal_places=0)

    headtube_types = models.ManyToManyField(
        bikeproperties.models.HeadtubeType,
        related_name='stems')

    handlebar_type = models.ForeignKey(
        'bikeproperties.HandlebarType',
        on_delete=models.PROTECT,
        related_name='stems')

    def find_matching_frames(self):
        return Frame.objects.filter(
            headtube_type__in=self.headtube_types.all())

    def find_matching_forks(self):
        return Fork.objects.filter(
            headtube_type__in=self.headtube_types.all())

    def find_matching_handlebars(self):
        return Handlebar.objects.filter(
            handlebar_type=self.handlebar_type)


class Handlebar(BikePart):

    width = models.DecimalField(
        max_digits=3,
        decimal_places=0)

    handlebar_type = models.ForeignKey(
        'bikeproperties.HandlebarType',
        on_delete=models.PROTECT,
        related_name='handlebars')

    def find_matching_stems(self):
        return Stem.objects.filter(
            handlebar_type=self.handlebar_type)


class Seatpost(BikePart):

    length = models.DecimalField(
        max_digits=3,
        decimal_places=0)

    seatclamp_type = models.ForeignKey(
        'bikeproperties.SeatclampType',
        on_delete=models.PROTECT,
        related_name='seatposts')

    travel = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True)

    def find_matching_frames(self):
        return Frame.objects.filter(
            seatclamp_type=self.seatclamp_type)


class Wheels(BikePart):

    wheel_type = models.ForeignKey(
        'bikeproperties.WheelType',
        on_delete=models.PROTECT,
        related_name='wheels')

    brake_type = models.ForeignKey(
        'bikeproperties.BrakeType',
        on_delete=models.PROTECT,
        related_name='wheels')

    axle_type = models.ForeignKey(
        'bikeproperties.AxleType',
        on_delete=models.PROTECT,
        related_name='wheels')

    brake_rotor_types = models.ManyToManyField(
        'bikeproperties.BrakeRotorType',
        related_name='wheels')

    def find_matching_frames(self):
        return Frame.objects.filter(
            wheel_types=self.wheel_type).filter(
                axle_type=self.axle_type).filter(
                    brake_types=self.brake_type)

    def find_matching_forks(self):
        return Fork.objects.filter(
            wheel_types=self.wheel_type).filter(
                axle_type=self.axle_type).filter(
                    brake_types=self.brake_type)

    def find_matching_rotors(self):
        return Rotor.objects.filter(
            brake_rotor_type__in=self.brake_rotor_types.all())

    def find_matching_brakes(self):
        return Brake.objects.filter(
            brake_type=self.brake_type)

    def find_matching_brakelevers(self):
        return BrakeLever.objects.filter(
            brake_type=self.brake_type)

    class Meta:
        verbose_name_plural = 'Wheels'


class Shock(BikePart):

    SUSPENSION_TYPES = [
        ('Oil', 'Oil'),
        ('Air', 'Air')
    ]

    shock_type = models.ForeignKey(
        'bikeproperties.ShockType',
        on_delete=models.PROTECT,
        related_name='shocks')

    suspension_type = models.CharField(
        max_length=16,
        choices=SUSPENSION_TYPES)

    def find_matching_frames(self):
        return Frame.objects.filter(
            shock_type=self.shock_type)
