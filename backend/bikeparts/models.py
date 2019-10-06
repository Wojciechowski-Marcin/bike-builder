from django.db import models
from .choices import *


class Category(models.Model):

    name = models.CharField(
        max_length=32)

    # TODO make category model
    slug = models.SlugField()


class BikePart(models.Model):

    brand = models.CharField(
        max_length=32)

    group = models.CharField(
        max_length=32, 
        null=True, 
        blank=True)

    model = models.CharField(
        max_length=32, 
        unique=True)

    material = models.CharField(
        max_length=32, 
        null=True)

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2)

    color = models.CharField(
        max_length=32, 
        null=True, 
        blank=True)

    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2)

    application = models.CharField(
        max_length=32,
        choices=APPLICATION_CHOICES)

    def __str__(self):
        return f'{self.__class__} {self.brand} {self.group} {self.model}'

    class Meta:
        abstract = True


class Frame(BikePart):

    size = models.DecimalField(
        max_digits=2, 
        decimal_places=1)

    wheel_size = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        choices=WHEEL_SIZES)

    headtube_type = models.CharField(
        max_length=3, 
        choices=HEADTUBE_TYPES)

    headtube_diameter = models.CharField(
        max_length=13, 
        choices=HEADTUBE_DIAMETRES)
        
    seatclamp_size = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        choices=SEATCLAMP_SIZES)

    bottom_bracket_size = models.DecimalField(
        max_digits=2, 
        decimal_places=0, 
        choices=BOTTOM_BRACKET_SIZES)

    brake_mount_type = models.CharField(
        max_length=2, 
        choices=BRAKE_MOUNT_TYPES)

    rear_derailleur_mount_type = models.CharField(
        max_length=1,
        null=True, 
        choices=REAR_DERAILLEUR_MOUNT_TYPES)

    front_derailleur_mount_type = models.CharField(
        max_length=2,
        null=True, 
        choices=FRONT_DERAILLEUR_MOUNT_TYPES)

    max_rotor_size = models.DecimalField(
        max_digits=3, 
        decimal_places=0,
        null=True, 
        choices=BRAKE_ROTOR_SIZES)

    recommended_fork_travel = models.DecimalField(
        max_digits=3, 
        decimal_places=0,
        null=True)

    # shock_size = models.CharField(
    #     null=True)
    


class Fork(BikePart):

    wheel_size = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        choices=WHEEL_SIZES)

    suspension_type = models.CharField(
        max_length=16,
        choices=SUSPENSION_TYPES)

    travel = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    steerer_tube_diameter = models.CharField(
        max_length=16,
        choices=HEADTUBE_DIAMETRES)

    axle_type = models.CharField(
        max_length=16,
        choices=AXLE_TYPE)

    brake_mount_type = models.CharField(
        max_length=2,
        choices=BRAKE_MOUNT_TYPES)


# class Shock(BikePart):

#     size = models.DecimalField(
#         max_digits=, 
#         decimal_places=,
#         choices=)

#     suspension_type = models.CharField(
#         max_length=16)


class Crankset(BikePart):

    gradiation = models.CharField(
        max_length=8)

    speed_compatibility = models.CharField(
        max_length=4,
        choices=SPEED_COMPATIBILITY_CHOICES)

    bottom_bracket_size = models.DecimalField(
        max_digits=2, 
        decimal_places=0, 
        choices=BOTTOM_BRACKET_SIZES)

    arm_length = models.DecimalField(
        max_digits=3, 
        decimal_places=0)


class Cassette(BikePart):

    gradiation = models.CharField(
        max_length=35)

    speed_compatibility = models.CharField(
        max_length=4,
        choices=SPEED_COMPATIBILITY_CHOICES)



class FrontDerailleur(BikePart):
    
    speed_compatibility = models.CharField(
        max_length=4,
        choices=SPEED_COMPATIBILITY_CHOICES)

    mount_type = models.CharField(
        max_length=2,
        null=True, 
        choices=FRONT_DERAILLEUR_MOUNT_TYPES)


class RearDerailleur(BikePart):
    
    speed_compatibility = models.CharField(
        max_length=4,
        choices=SPEED_COMPATIBILITY_CHOICES)

    mount_type = models.CharField(
        max_length=1,
        null=True, 
        choices=REAR_DERAILLEUR_MOUNT_TYPES)


class Brake(BikePart):

    brake_type = models.CharField(
        max_length=4,
        choices=BRAKE_TYPES)

    mount_type = models.CharField(
        max_length=2,
        choices=BRAKE_MOUNT_TYPES)


class BrakeLever(BikePart):

    brake_type = models.CharField(
        max_length=4,
        choices=BRAKE_TYPES)


class DerailleurLever(BikePart):
    
    speed_compatibility = models.CharField(
        max_length=4,
        choices=SPEED_COMPATIBILITY_CHOICES)


class Rotor(BikePart):

    size = models.DecimalField(
        max_digits=3, 
        decimal_places=0,
        choices=BRAKE_ROTOR_SIZES)


class Handlebar(BikePart):

    width = models.DecimalField(
        max_digits=3, 
        decimal_places=0)
        
    diameter = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        choices=HANDLEBAR_DIAMETERS)


class Stem(BikePart):

    length = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    angle = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    headtube_diameter = models.CharField(
        max_length=13, 
        choices=HEADTUBE_DIAMETRES)

    handlebar_diameter = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        choices=HANDLEBAR_DIAMETERS)

    mount = models.CharField(
        max_length=3,
        choices=HEADTUBE_TYPES)


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

    diameter = models.DecimalField(
        max_digits=3, 
        decimal_places=1)

    travel = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        null=True)


class Wheels(BikePart):

    size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        choices=WHEEL_SIZES)

    brake_type = models.CharField(
        max_length=4,
        choices=BRAKE_TYPES)

    hub = models.CharField(
        max_length=9, 
        choices=HUB_TYPES)

    class Meta:
        verbose_name_plural = 'Wheels'
