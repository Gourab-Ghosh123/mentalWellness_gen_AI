from django.shortcuts import render
from .models import Helpline

def helpline(request):
    query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    helplines = Helpline.objects.all()  # model, not variable

    if query:
        helplines = helplines.filter(name__icontains=query)  # <-- double underscore

    if category_filter:
        helplines = helplines.filter(category=category_filter)

    categories = Helpline.CATEGORY_CHOICES

    return render(request, "helpline.html", {
        "helplines": helplines,
        "categories": categories,
        "search": query,
        "selected_category": category_filter
    })
