from django.shortcuts import render

# Create your views here.
def helloworldview(request):
    mylistitems = ['item1','item2','item3']

    return render(request,'helloworld.html', context)
