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

    brake_rotor_type = models.ManyToManyField(
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


class Shock(BikePart):

    shock_type = models.ForeignKey(
        'bikeproperties.ShockType',
        on_delete=models.PROTECT,
        related_name='shocks')

    suspension_type = models.CharField(
        max_length=16)


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


class Cassette(BikePart):

    gradiation = models.CharField(
        max_length=35)

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='cassettes')


class FrontDerailleur(BikePart):

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='front_derailleurs')

    front_derailleur_type = models.ForeignKey(
        'bikeproperties.FrontDerailleurType',
        on_delete=models.PROTECT,
        related_name='front_derailleurs')


class RearDerailleur(BikePart):

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='rear_derailleurs')

    rear_derailleur_type = models.ForeignKey(
        'bikeproperties.RearDerailleurType',
        on_delete=models.PROTECT,
        related_name='rear_derailleurs')


class Brake(BikePart):

    material = models.ForeignKey(
        'bikeproperties.Material',
        on_delete=models.PROTECT,
        related_name='brakes')

    brake_type = models.ForeignKey(
        'bikeproperties.BrakeType',
        on_delete=models.PROTECT,
        related_name='brakes')


class BrakeLever(BikePart):

    brake_type = models.ForeignKey(
        'bikeproperties.BrakeType',
        on_delete=models.PROTECT,
        related_name='brake_levers')


class DerailleurLever(BikePart):

    speed_compatibilities = models.ManyToManyField(
        bikeproperties.models.SpeedCompatibility,
        related_name='derailleur_levers')


class Rotor(BikePart):

    brake_rotor_type = models.ForeignKey(
        'bikeproperties.BrakeRotorType',
        on_delete=models.PROTECT,
        related_name='rotors')


class Handlebar(BikePart):

    width = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    handlebar_type = models.ForeignKey(
        'bikeproperties.HandlebarType',
        on_delete=models.PROTECT,
        related_name='handlebars')


class Stem(BikePart):

    length = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    angle = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    headtube_type = models.ManyToManyField(
        bikeproperties.models.HeadtubeType,
        related_name='stems')

    handlebar_type = models.ForeignKey(
        'bikeproperties.HandlebarType',
        on_delete=models.PROTECT,
        related_name='stems')


class Saddle(BikePart):

    length = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    width = models.DecimalField(
        max_digits=3, 
        decimal_places=0)


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
        decimal_places=1,
        null=True,
        blank=True)


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

    class Meta:
        verbose_name_plural = 'Wheels'
