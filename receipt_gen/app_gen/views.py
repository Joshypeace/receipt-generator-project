from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .models import Receipt
from .forms import ReceiptForm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save()
            return redirect('download_receipt_pdf', pk=receipt.pk)
    else:
        form = ReceiptForm()
    return render(request, 'index.html', {'form': form})


def generate_pdf(response, receipt):
   
    image_path = 'C:\\Users\\SHAKIRA CHILAPONDWA\\Desktop\\New folder\\receipt_gen\\static\\letsgo.jpeg'


    custom_page_size = (600, 500)

    c = canvas.Canvas(response, pagesize= custom_page_size)
    c.translate(inch, inch)

#container 
    c.setLineWidth(2)
    c.setStrokeColor('black')
    c.roundRect(-40,-60,540,470,20)

#divider
    c.setStrokeColor('black')
    c.setLineWidth(2)
    c.line(-40, 230, 500, 230)
    c.setFillColor('black')

# blue divider
    c.setStrokeColor('#18bef0')
    c.setLineWidth(8)
    c.line(-30, 235, 499, 235)
    c.setFillColor('#18bef0')

    c.setStrokeColor('black')
    c.setLineWidth(8.5)
    c.line(300, 235, 499, 235)
    c.setFillColor('black')

    c.setStrokeColor('black')
    c.setLineWidth(8.5)
    c.line(275, 235, 290, 235)
    c.setFillColor('black')

# logo
    c.drawImage(image_path, -30, 250, width=150, height=150)

# strings
    c.setFillColor('black')
    c.setFont('Times-Bold', 21)
    c.drawString(180, 380, 'RECEIPT')

# addresses
    c.setFillColor('#18bef0')
    c.setFont('Helvetica-Bold', 12)
    c.drawString(335, 385, 'Lets Go Travel and Tours')

    c.setFillColor('black')
    c.setFont('Helvetica', 11)
    c.drawString(394, 370, 'Private Bag A130')

    c.setFillColor('black')
    c.setFont('Helvetica', 11)
    c.drawString(395, 355, 'Lilongwe, Malawi')

    c.setFillColor('#18bef0')
    c.setFont('Helvetica-Bold', 12)
    c.drawString(438, 340, 'Mobile:')

    c.setFillColor('black') 
    c.setFont('Helvetica', 11)
    c.drawString(373, 325, '+265 (0) 999 879 759')

    c.setFillColor('black')
    c.setFont('Helvetica', 11)
    c.drawString(373, 310, '+265 (0) 996 880 692')

    c.setFillColor('#18bef0')
    c.setFont('Helvetica-Bold', 12)
    c.drawString(444, 295, 'Email:')

    c.setFillColor('black')
    c.setFont('Helvetica', 11)
    c.drawString(300, 280, 'letsgotravelandtours299@gmail.com')
  
    c.setFillColor('black')
    c.setFont('Helvetica', 11)
    c.drawString(327, 265, 'info@letsgotravelandtours.com')

    c.setFillColor('black')
    c.setFont('Helvetica', 16)
    c.drawString(140, 250, 'TPIN NO: 31731228')

# body content
    c.setFillColor('red')
    c.setFont('Helvetica-Bold', 14)
    c.drawString(-35, 200, "No:-")

    c.setFillColor('grey')
    c.setFont('Helvetica-Bold', 14)
    c.drawString(15, 200, f"{ receipt.receipt_number }")

    c.setFillColor('black')
    c.setFont('Times-Roman', 14)
    c.drawString(301, 200, f"Date :{ receipt.date.day }/{receipt.date.month}/{receipt.date.year}")

    c.setFillColor('black')
    c.setFont('Times-Italic', 14)
    c.drawString(-35, 160, f"Received from :{ receipt.received_from }")

    c.setFillColor('black')
    c.setFont('Times-Italic', 14)
    c.drawString(-35, 120, f"The sum of :{ receipt.sum_amount }")

    c.setFillColor('black')
    c.setFont('Times-Bold', 14) 
    c.drawString(-35, 70, f"K :{ receipt.actual_amount }")

    c.setFillColor('black')
    c.setFont('Times-Roman', 14)
    c.drawString(350, 80, f"{ receipt.signature }")

    c.setFillColor('black')
    c.setFont('Times-Italic', 14)
    c.drawString(350, 60, "(With Thanks)")


    c.setFillColor('black')
    c.setFont('Times-Italic', 14)
    c.drawString(-35, 0, f"being payment for :{ receipt.payment_details }")

    c.setFillColor('black')
    c.setFont('Times-Italic', 14)
    c.drawString(-35, -40, f"Cash / Cheque No :{ receipt.payment_method }")
    
    c.showPage()
    c.save()



def download_receipt_pdf(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Receipt_{receipt.receipt_number}.pdf"'
    generate_pdf(response, receipt)
    return response
