from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import bikeparts.models
import bikeproperties.models
from api import serializers


# def test(request):
#     text=request.GET.get("text", ""),

#     return JsonResponse({"test": len(text)})


# @csrf_exempt
def frame_view(request):
    if request.method == 'GET':
        frames = bikeparts.models.Frame.objects.all()
        serializer = serializers.FrameSerializer(frames, many=True)
        return JsonResponse(serializer.data, safe=False)
