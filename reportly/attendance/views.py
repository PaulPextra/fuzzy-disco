from django.shortcuts import render, HttpResponse

# Create your views here.
def test_view(request):
    # print(request.user)
    return render(request, 'test.html')

def homePage_view(request):
    return HttpResponse('Homepage!')
