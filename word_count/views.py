from django.shortcuts import render
from .utils import count_words
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        number_words = count_words(text)
        return JsonResponse({'number_words': number_words})
    return render(request, 'word_count/wordcount.html')
