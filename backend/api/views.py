from django.http import JsonResponse

def test(request):
    text=request.GET.get("text", "")

    return JsonResponse({"test": len(text)})