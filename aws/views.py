from django.shortcuts import render
from .models import Test
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        img = request.FILES['img']
        print(name,img)
        db = Test(name=name,img=img)
        db.save()
    return  render(request,'home.html')

def all(request):
    data = Test.objects.all()
    return  render(request,'home.html',{'data':data})
