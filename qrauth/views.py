try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image, ImageDraw

from django.shortcuts import render
import qrcode
import os


def page(request):

	return render(request, 'qrauth/first_page.html')


def qrcod(request):

	string = "http://127.0.0.1:8000/qr-code-demo/qrcode"

	with open('qr_index.txt', 'r') as file:
		qr_index = int(file.read())

	with open('qr_index.txt', 'w') as file:
		x = qr_index + 1
		file.write(str(x))

	stringx = string + str(qr_index)

	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=9,
		border=2,
	)
	qr.add_data(stringx)
	qr.make(fit=True)

	image = qr.make_image(fill_color="black", back_color="white")

	image.save('qrauth/static/qrauth/qrcode.jpg')


	return render(request, 'qrauth/page.html')


def qrcod_activate(request, name):

	with open('qr_index.txt', 'r') as file:
		x = int(file.read())

	qr_index = x - 1

	if name == qr_index:
		return render(request, 'qrauth/activate.html')
	else:
		return render(request, 'qrauth/invalid_code.html')
