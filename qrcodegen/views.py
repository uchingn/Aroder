from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.conf import settings
from io import BytesIO
import qrcode
from .models import Qrcode  # assuming you have a model named Qrcode
from qrcodegen.forms import CreatePostForm 


def qrcode_gen(request):
    qr_image_url = None

    if request.method == 'POST':
        data = request.POST.get('qr_data')
        mobile_number = request.POST.get("mobile_number")

        # Validate mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'qrcodegen/qrcode.html', {
                'error': "Invalid number! Please enter a 10-digit mobile number."
            })

        # Combine data
        qr_content = f"{data}|{mobile_number}"

        # Generate QR code
        qr_img = qrcode.make(qr_content)
        qr_image = BytesIO()  # create Byte stream
        qr_img.save(qr_image, format="PNG")
        qr_image.seek(0)

        # Save record to DB
        Qrcode.objects.create(data=data, mobile_number=mobile_number)

        # Save file to /media/qr_code/
        re_storage = settings.MEDIA_ROOT / 'qr_code'
        fs = FileSystemStorage(location=re_storage, base_url="/media/qr_code/")

        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image.read(), name=filename)
        filepath = fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)

    # render template with QR code image (if generated)
    context = {"qr_image_url": qr_image_url}
    return render(request, 'qrcodegen/qrcode.html', context)


def posthome(request):
    form=CreatePostForm()
    context={
        'form':form,
    }
    
    
    return render(request,"post.html",context)