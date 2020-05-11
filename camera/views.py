from io import BytesIO
import qrcode

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def camera(request):
    return render(request, 'index.html')


def camera_qr(request, room_name):
    camera_url = reverse('camera')
    camera_url = request.build_absolute_uri(camera_url) + '#' + room_name
    img = qrcode.make(camera_url)
    output = BytesIO()
    img.save(output, "PNG")
    return HttpResponse(output.getvalue(), content_type='image/png')
