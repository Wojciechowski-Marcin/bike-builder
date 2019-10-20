from django.db import models


class Brand(models.Model):

    name = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.name}'


class Group(models.Model):

    name = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.name}'


class Material(models.Model):
    
    name = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.name}'


class Color(models.Model):

    name = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.name}'


class Application(models.Model):

    name = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.name}'


class WheelType(models.Model):

    size = models.DecimalField(
        max_digits=3, 
        decimal_places=1)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}\"'


class HeadtubeType(models.Model):

    headtube_type = models.CharField(
        max_length=16)

    size = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size} {self.headtube_type}'


class SeatclampType(models.Model):

    size = models.DecimalField(
        max_digits=3,
        decimal_places=1)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}mm'


class BrakeType(models.Model):

    mount_type = models.CharField(
        max_length=16)

    brake_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.brake_type} {self.mount_type}'


class BottomBracketType(models.Model):

    size = models.DecimalField(
        max_digits=2,
        decimal_places=0)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}mm'


class FrontDerailleurType(models.Model):

    mount_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.mount_type}'


class RearDerailleurType(models.Model):

    mount_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.mount_type}'


class BrakeRotorType(models.Model):

    size = models.DecimalField(
        max_digits=3, 
        decimal_places=0)
    
    mount_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.mount_type} {self.size}mm'


class AxleType(models.Model):

    axle_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.axle_type}'


class SpeedCompatibility(models.Model):

    speed_compatibility = models.CharField(
        max_length=4)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.speed_compatibility}'

    class Meta:
        verbose_name_plural = 'Speed Compatibilities'


class HandlebarType(models.Model):

    size = models.DecimalField(
        max_digits=3,
        decimal_places=1)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}mm'


class ShockType(models.Model):

    mount_length = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.mount_length}mm'