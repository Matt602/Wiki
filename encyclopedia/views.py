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
