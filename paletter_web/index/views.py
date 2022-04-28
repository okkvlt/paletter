from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render

from .utils.paletter import Paletter

from .utils.upload import checkExtensions


def index(request):
    if request.method != "POST":
        return render(request,
                      "upload.html",
                      context=None)

    if not request.FILES["file"]:
        contexts = {
            "alert": "Arquivo não reconhecido!"
        }
        return render(request,
                      "upload.html",
                      context=contexts)

    f = request.FILES["file"]
    filename = f.name

    if not checkExtensions(filename):
        contexts = {
            "alert": "Extensão não-permitida!"
        }
        return render(request,
                      "upload.html",
                      context=contexts)

    bytes = BytesIO(f.read())
    img = Paletter(bytes)
    palettes = img.get_image()

    response = HttpResponse(content_type="image/png")
    palettes.save(response, "PNG")

    return response
