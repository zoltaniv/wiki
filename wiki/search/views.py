from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from markdown import markdown

from encyclopedia import util

# Create your views here.
def index(request):
    # q = HttpRequest.GET.get("q")
    title = request.GET.get("q")

    # Get the list of all entries
    entries = util.list_entries()
    subentries = []

    # Compare the query and the entry title
    if title in entries:
        # Get an enty content
        entry = markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {"title": title, "entry": entry})

    for article in entries:
        if title in article:
            subentries.append(article)
            
    if subentries:
        return render(request, "search/index.html", {"subentries": subentries})
    else:
        return render(request, "encyclopedia/fail.html", {"title": title})
