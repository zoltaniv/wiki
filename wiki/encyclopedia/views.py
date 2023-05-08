from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from markdown import markdown
from django import forms

import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def read_entry(request, title):

    # Get the list of all entries
    entries = util.list_entries()

    # Check if the title exists
    if title in entries:
        # Get an enty content
        entry = markdown(util.get_entry(title))

        return render(request, "encyclopedia/entry.html", {"title": title, "entry": entry})
    else:
        # Todo
        return render(request, "encyclopedia/fail.html", {"title": title})


def random_page(request):
    # Get the list of all entries
    entries = util.list_entries()

    # Get a random title of the entries list
    title = random.choice(entries)

    # Get entry with current title
    entry = markdown(util.get_entry(title))

    return render(request, "encyclopedia/entry.html", {"title": title, "entry": entry})
