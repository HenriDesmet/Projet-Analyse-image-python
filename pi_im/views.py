# XML ParseError
from _elementtree import ParseError
# Django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import action
# JSON import
import json
# Unique ID
import uuid
# System
import os
from django.views.decorators.csrf import csrf_exempt
# App imports
from pi_im.models import ReferenceImg, ResourceAnalyse, AnalyseResults
from pi_im import bow
from image_srv import settings
from pi_im import convert
from rest_framework.views import APIView


class Img_searchesList(APIView):
    def post(self, request, format=None):
        errors = {"error": "body must not be empty"}
        image_64 = request.data["base64"]
        i64=image_64.split(',')[1]
        type=image_64.split(',')[0]
        print(image_64.split(','))
        #print(image_64)
        print(i64)
        print(type)
        if 'png' in type:
            img_type='png'
        else:
            img_type='jpg'
        img_path = convert.buildAndReturnLabel(i64, img_type)


        res_nb = bow.research(img_path, 4)
        result_str = json.dumps({"location": "/img_searches/" + str(res_nb) + "/"})
        print(result_str)
        return HttpResponse(result_str, content_type="text/json", status=201)

    def get(self, request, id, format=None):
        resource = get_object_or_404(ResourceAnalyse, id=id)

        data = resource.get_data("http://" + request.get_host() + settings.PI_IM_RESOURCES_URL)

        print(json.dumps(data, indent=4))

        return HttpResponse(json.dumps(data), content_type="text/json")



@action(detail=True, methods=['post'])
@csrf_exempt
def image_research(request):
    try:
        file = request.FILES['file']
    except KeyError:
        raise ParseError('Request has no reference file attached')

    extension = file.name.split(".")[-1].lower()
    img_path = os.path.join(settings.PI_IM_STATICIMAGES_DIR, "tmp", str(uuid.uuid4())+"."+extension)
    with open(img_path, "wb") as f:
        f.write(file.read())

    res_id = bow.research(img_path, 3)

    os.remove(img_path)

    result_str = json.dumps({"location": "/image_research/" + str(res_id) + "/"})
    print(result_str)
    return HttpResponse(result_str, content_type="text/json", status=201)

def image_research_result(request, id):
    resource = get_object_or_404(ResourceAnalyse, id=id)

    data = resource.get_data("http://"+request.get_host()+settings.PI_IM_RESOURCES_URL)

    print(json.dumps(data, indent=4))

    return HttpResponse(json.dumps(data), content_type="text/json")


def reindex(request):
    res = bow.indexing()
    return HttpResponse(res)

# ============ Administration ============
def listreferences(request):

    references = ReferenceImg.objects.all()
    analyses_obj = ResourceAnalyse.objects.all()
    analyses = []

    print(references)

    for a in analyses_obj:
        print(a)
        analyses.append(str(a))

    return render(request, 'display_references.html', {"references": references, "analyses": analyses})

def form_sendfile(request):
    return render(request, 'form_sendfile.html', {})


