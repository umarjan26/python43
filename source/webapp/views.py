from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'index.html')
    query = request.GET.getlist("name", "rrrr")
    print(query)
    context = {"name": query, "test": "lalala"}
    return render(request, "index.html", context)


def create(request):
    summa = 0
    if request.method == "GET":
        return render(request, "create.html")
    else:
        first = request.POST.get('first')
        first = int(first)
        second = request.POST.get('second')
        second = int(second)
        if request.POST.get("calculate") == "+":
            summa = first + second
        elif request.POST.get("calculate") == "-":
            summa = first - second
        elif request.POST.get("calculate") == "*":
            summa = first * second
        elif request.POST.get("calculate") == "/":
            summa = first / second
        context = {
            "first": request.POST.get("first"),
            "calculate": request.POST.get("calculate"),
            "second": request.POST.get("second"),
            "summa": summa
        }
        return render(request, 'article_view.html', context)