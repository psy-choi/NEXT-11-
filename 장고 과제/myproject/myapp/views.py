from django.shortcuts import render

# Create your views here.


def hello(request):

    return render(request, 'hello.html')


def count(request):

    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_word = len(list(text.split()))
    total_len = len(text)
    no_blank_len = len(text.replace(" ", ""))
    return render(request, 'result.html', {'text': text, 'total_len': total_len, 'no_blank_len' : no_blank_len, 'total_word': total_word })