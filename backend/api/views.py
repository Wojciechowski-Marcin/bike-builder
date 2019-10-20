from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import bikeparts.models
import bikeproperties.models
from api import serializers


# def test(request):
#     text=request.GET.get("text", ""),

#     return JsonResponse({"test": len(text)})


def serialize_all_models(cls, serializer):
    models = cls.objects.all()
    serializer = serializer(models, many=True)
    return JsonResponse(serializer.data, safe=False)


def frame_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Frame, 
            serializers.FrameSerializer)


def fork_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Fork, 
            serializers.ForkSerializer)


def crankset_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Crankset, 
            serializers.CranksetSerializer)


def cassette_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Cassette, 
            serializers.CassetteSerializer)


def front_derailleur_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.FrontDerailleur, 
            serializers.FrontDerailleurSerializer)


def rear_derailleur_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.RearDerailleur, 
            serializers.RearDerailleurSerializer)


def brake_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Brake, 
            serializers.BrakeSerializer)


def brake_lever_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.BrakeLever, 
            serializers.BrakeLeverSerializer)


def derailleur_lever_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.DerailleurLever, 
            serializers.DerailleurLeverSerializer)


def rotor_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Rotor, 
            serializers.RotorSerializer)


def handlebar_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Handlebar, 
            serializers.HandlebarSerializer)


def stem_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Stem, 
            serializers.StemSerializer)


def saddle_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Saddle, 
            serializers.SaddleSerializer)


def seatpost_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Seatpost, 
            serializers.SeatpostSerializer)


def wheels_view(request):
    if request.method == 'GET':
        return serialize_all_models(
            bikeparts.models.Wheels, 
            serializers.WheelsSerializer)
