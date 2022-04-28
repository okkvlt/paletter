from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render

from .utils.paletter import Paletter

from .utils.upload import checkExtensions


def index(request):
    if request.method != "POST":
        return render(request, "upload.html")

    if not request.FILES["file"]:
        return

    f = request.FILES["file"]
    filename = f.name

    if not checkExtensions(filename):
        return

    img = Paletter(BytesIO(f.read()))
    palettes = img.get_image()

    response = HttpResponse(content_type="image/png")
    palettes.save(response, "PNG")

    return response
