from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        msg=request.POST.get('input_field', '')
        responsemsg=f" is your input."
        return JsonResponse({'response': responsemsg})
    else:
        return render(request,'home.html')
