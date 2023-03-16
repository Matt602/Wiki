from django.shortcuts import render

from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    if name not in util.list_entries():
        return HttpResponse("Requested page does not exist")

    else:

        return render(request, "encyclopedia/entry.html", {
            "title": name,
            "entry": util.get_entry(name)
    })



def search(request):
    query = request.GET.get('q')
    lst = util.list_entries()

    if query in lst:

        return render(request, 'encyclopedia/entry.html', {
            "title": query,
            "entry": util.get_entry(query) 
        })
    else:
        subList = []
        for entry in lst:
            if query in entry:
                subList.append(entry)
        return render(request, "encyclopedia/search_sub.html", {
            "query": query,
            "subList": subList,
        })


def toAdd(request):
    return render(request, "encyclopedia/add.html")


def add(request):
    title = request.POST.get('title')
    content = request.POST.get('textBody')
    util.save_entry(title, content)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": content,
    })