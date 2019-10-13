from rest_framework import serializers

import bikeparts.models
import bikeproperties.models


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.Brand
        fields = ('id', 'name',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.Group
        fields = ('id', 'name',)


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.Material
        fields = ('id', 'name',)


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.Color
        fields = ('id', 'name',)


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.Application
        fields = ('id', 'name',)


class WheelTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.WheelType
        fields = ('id', 'size',)


class HeadtubeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.HeadtubeType
        fields = ('id', 'h_type', 'size',)


class SeatclampTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.SeatclampType
        fields = ('id', 'size',)


class BrakeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.BrakeType
        fields = ('id', 'b_type', 'mount_type',)


class BottomBracketTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.BottomBracketType
        fields = ('id', 'size',)


class FrontDerailleurTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.FrontDerailleurType
        fields = ('id', 'mount_type',)


class RearDerailleurTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.RearDerailleurType
        fields = ('id', 'mount_type',)


class BrakeRotorTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.Application
        fields = ('id', 'size',)


class AxleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.AxleType
        fields = ('id', 'a_type',)


class SpeedCompatibilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.SpeedCompatibility
        fields = ('id', 'speed_compatibility',)


class HandlebarTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = bikeproperties.models.HandlebarType
        fields = ('id', 'a_type',)


class BikePartSerializer(serializers.ModelSerializer):

    brand = BrandSerializer()
    group = GroupSerializer()
    material = MaterialSerializer()
    color = ColorSerializer()
    application = ApplicationSerializer()

    class Meta:
        model = bikeparts.models.BikePart
        fields = (
            'id',
            'brand',
            'group',
            'model',
            'material',
            'weight',
            'color',
            'price',
            'applications',)
        abstract = True


class FrameSerializer(BikePartSerializer):

    wheel_types = WheelTypeSerializer(many=True)
    headtube_type = HeadtubeTypeSerializer()
    seatclamp_type = SeatclampTypeSerializer()
    bottom_bracket_type = BottomBracketTypeSerializer()
    brake_types = BrakeTypeSerializer(many=True)
    rear_derailleur_types = RearDerailleurTypeSerializer(many=True)
    front_derailleur_types = FrontDerailleurTypeSerializer(many=True)
    brake_rotor_type = BrakeRotorTypeSerializer()


    class Meta:
        model = bikeparts.models.Frame
        fields = BikePartSerializer.Meta.fields + (
            'size',
            'wheel_types',
            'headtube_type',
            'seatclamp_type',
            'bottom_bracket_type',
            'brake_types',
            'rear_derailleur_types',
            'front_derailleur_types',
            'brake_rotor_type',
            'recommended_fork_travel',)


class ForkSerializer(BikePartSerializer):

    wheel_types = WheelTypeSerializer(many=True)
    headtube_type = HeadtubeTypeSerializer()
    axle_type = AxleTypeSerializer()
    brake_types = BrakeTypeSerializer(many=True)

    class Meta:
        model = bikeparts.models.Fork
        fields = BikePartSerializer.Meta.fields + (
            'wheel_types',
            'suspension_type',
            'travel',
            'headtube_type',
            'axle_type',
            'brake_types',)


class CranksetSerializer(BikePartSerializer):

    speed_compatibilities = SpeedCompatibilitySerializer(many=True)
    bottom_bracket_type = BottomBracketTypeSerializer()

    class Meta:
        model = bikeparts.models.Crankset
        fields = BikePartSerializer.Meta.fields + (
            'gradiation',
            'speed_compatibilities',
            'bottom_bracket_type',
            'arm_length',)


class CassetteSerializer(BikePartSerializer):

    speed_compatibilities = SpeedCompatibilitySerializer(many=True)

    class Meta:
        model = bikeparts.models.Cassette
        fields = BikePartSerializer.Meta.fields + (
            'gradiation', 'speed_compatibilities',)


class FrontDerailleurSerializer(BikePartSerializer):

    speed_compatibilities = SpeedCompatibilitySerializer(many=True)
    front_derailleur_type = FrontDerailleurTypeSerializer()

    class Meta:
        model = bikeparts.models.FrontDerailleur
        fields = BikePartSerializer.Meta.fields + (
            'speed_compatibilities', 'front_derailleur_type',)


class RearDerailleurSerializer(BikePartSerializer):

    speed_compatibilities = SpeedCompatibilitySerializer(many=True)
    rear_derailleur_type = RearDerailleurTypeSerializer()

    class Meta:
        model = bikeparts.models.RearDerailleur
        fields = BikePartSerializer.Meta.fields + (
            'speed_compatibilities', 'rear_derailleur_type',)


class BrakeSerializer(BikePartSerializer):

    brake_type = BrakeTypeSerializer()

    class Meta:
        model = bikeparts.models.Brake
        fields = BikePartSerializer.Meta.fields + (
            'brake_type',)


class BrakeLeverSerializer(BikePartSerializer):

    brake_type = BrakeTypeSerializer()

    class Meta:
        model = bikeparts.models.BrakeLever
        fields = BikePartSerializer.Meta.fields + (
            'brake_type',)


class DerailleurLeverSerializer(BikePartSerializer):

    speed_compatibilities = SpeedCompatibilitySerializer(many=True)

    class Meta:
        model = bikeparts.models.DerailleurLever
        fields = BikePartSerializer.Meta.fields + (
            'speed_compatibilities',)


class RotorSerializer(BikePartSerializer):

    brake_rotor_type = BrakeRotorTypeSerializer()

    class Meta:
        model = bikeparts.models.Rotor
        fields = BikePartSerializer.Meta.fields + (
            'brake_rotor_type',)



class HandlebarSerializer(BikePartSerializer):

    handlebar_type = HandlebarTypeSerializer()

    class Meta:
        model = bikeparts.models.Handlebar
        fields = BikePartSerializer.Meta.fields + (
            'width', 'handlebar_type',)



class StemSerializer(BikePartSerializer):

    headtube_type = HeadtubeTypeSerializer()
    handlebar_type = HandlebarTypeSerializer()

    class Meta:
        model = bikeparts.models.Stem
        fields = BikePartSerializer.Meta.fields + (
            'length', 'angle', 'headtube_type', 'handlebar_type',)



class SaddleSerializer(BikePartSerializer):

    class Meta:
        model = bikeparts.models.Saddle
        fields = BikePartSerializer.Meta.fields + (
            'length', 'width')



class SeatpostSerializer(BikePartSerializer):

    seatclamp_type = SeatclampTypeSerializer()

    class Meta:
        model = bikeparts.models.Seatpost
        fields = BikePartSerializer.Meta.fields + (
            'length', 'seatclamp_type', 'travel')



class WheelsSerializer(BikePartSerializer):

    wheel_type = WheelTypeSerializer()
    brake_type = BrakeTypeSerializer()
    axle_type = AxleTypeSerializer()

    class Meta:
        model = bikeparts.models.Wheels
        fields = BikePartSerializer.Meta.fields + (
            'wheel_type', 'brake_type', 'axle_type')
