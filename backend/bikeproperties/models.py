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


class WheelSize(models.Model):

    size = models.DecimalField(
        max_digits=3, 
        decimal_places=1)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}\"'


class Headtube(models.Model):

    h_type = models.CharField(
        max_length=16)

    size = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size} {self.h_type}'


class SeatclampSize(models.Model):

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

    b_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.b_type} {self.mount_type}'


class BottomBracketSize(models.Model):

    size = models.DecimalField(
        max_digits=2,
        decimal_places=0)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}mm'


class FrontDerailleurMount(models.Model):

    mount_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.mount_type}'


class RearDerailleurMount(models.Model):

    mount_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.mount_type}'


class BrakeRotorSize(models.Model):

    size = models.DecimalField(
        max_digits=3, 
        decimal_places=0)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}mm'


class AxleType(models.Model):

    a_type = models.CharField(
        max_length=16)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.a_type}'


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


class HandlebarSize(models.Model):

    size = models.DecimalField(
        max_digits=3,
        decimal_places=1)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f'<{self.class_name}> {self.size}cm'
