from django.shortcuts import render
from mainapp.forms import feedback



# Create your views here.
def main_view(request):
    return render(request,'home.html')



def images_view(request):
    return render(request,'info.html')


def registration_view(request):
    name=""
    regi='get'
    submitted=False
    myform=feedback()
    if request.method=='POST':
        take=feedback(request.POST)
        if take.is_valid():
            print("form validation successfull.....")
            print("name:",take.cleaned_data['name'])
            print("contact:",take.cleaned_data['contact'])
            print("feedback:",take.cleaned_data['feedmsg'])
            submitted=True
            name=take.cleaned_data['name']
    return render(request,'info.html',{'regi':regi,'mydict':myform,'name':name,'submitted':submitted},)
