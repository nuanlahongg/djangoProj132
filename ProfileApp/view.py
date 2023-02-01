from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def test(request):
    return HttpResponse("<H1> Hello Word <br> This is my Word wide web </H1>")


def homePage(request):
    return render(request, 'homePage.html')


def secondPage(request):
    return render(request, 'secondPage.html')


def thirdPage(request):
    return render(request, 'thirdPage.html')


def fourthPage(request):
    return render(request, 'fourthPage.html')


def fivePage(request):
    return render(request, 'fivePage.html')


def sixthPage(request):
    return render(request, 'sixthPage.html')


def showMyData(request):
    name = "nuanlahongg"
    surname = "chueasawathee"
    gender = "FeMale"
    satatus = "studen"
    work = "work"
    context = {'name': name, 'surname': surname, 'gender': gender, 'satatus': satatus, 'work': work}
    return render(request, 'showMyData.html', context)


def product(request):
    name = "นวญลหง"
    surname = "เชื้อสาวะถี"
    nickname = "ชมพู่"
    age = "21 ปี"
    weight = "53"
    height = "153"
    color = "สีน้ำเงิน-ขาว"
    song = "ข้างกาย"
    phoneNumber = "0967691570"
    studenCode = "65342310132-6"
    listNameProduct = [
        ["มาร์คมะขามน้ำผึ้ง", 190, '../../static/images/muse1.png'],
        ["มาร์คมะกู้ด", 199, '../../static/images/muse2.png'],
        ["ยาสีฟันนมแพะ", 199, '../../static/images/pro3.png'],
        ["น้ำหอม JANUA กลิ่น flower shop", 290, '../../static/images/pro4.PNG'],
        ["น้ำหอม JANUA กลิ่น wood sand and fresh vibe", 290, '../../static/images/pro5.PNG'],
        ["น้ำหอม JANUA กลิ่น srxy on the beach", 290, '../../static/images/pro6.PNG'],
        ["น้ำหอม JANUA กลิ่น sweetie picnic", 290, '../../static/images/pro7.PNG'],
        ["กลอสดอกไม้ 01-poppy pink", 199, '../../static/images/pro8.png'],
        ["กลอสดอกไม้ 02-sunny flower", 199, '../../static/images/pro9.png'],
        ["กลอสดอกไม้ 03-ruby tulip", 199, '../../static/images/pro10.png']
    ]
    return render(request, 'product.html',
                  {'name': name, 'surname': surname, 'nickname': nickname, 'age': age, 'wight': weight,
                   'height': height,
                   'color': color, 'song': song, 'phoneNumber': phoneNumber, 'studenCode': studenCode,
                   'ListNameProduct': listNameProduct})


listOutProduct = []
from ProfileApp.forms import *
from ProfileApp.models import *


def lisProduct(request):
    context = {'product': listOutProduct}
    return render(request, 'listProduct.html', context)


def inputproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            brand = form.get('brand')
            price = form.get('price')
            amount = form.get('amount')
            detail = form.get('detail')

            if amount < 3:
                discountlate = 0
            elif amount < 5:
                discountlate = 0.05
            else:
                discountlate = 0.10

            total = price * amount
            discount = total * discountlate
            net = total - discount

            product = Product(id, name, brand, price, amount, detail, total, discount, net)
            listOutProduct.append(product)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, 'inputProduct.html', context)
