from django.shortcuts import render
from django import forms
from encyclopedia import util
from markdown import markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
import os

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title of Entry", widget=forms.TextInput(attrs={"size": 20}))
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 10}))
    
class EditForm(forms.Form):
    title = forms.CharField(widget=forms.HiddenInput())
    text = forms.CharField(widget=forms.Textarea())

# Create your views here.
def index(request):
    if request.method == "POST":
        # Creat a list of exist entries
        entries = util.list_entries()
        title = request.POST.get("title")
        text = request.POST.get("text")
        
        if title in entries:
            return render(request, "newpage/error.html", {"title": title})
        else:
            with open(f"entries/{title}.md", "w") as file:
                file.write(text)
            # entry = markdown(util.get_entry(title))
            return HttpResponseRedirect(f"/wiki/{title}")
            # return render(request, "encyclopedia/entry.html", {"title": title, "entry": entry})
    else:
        # todo
        return render(request, "newpage/index.html", {"form": NewTaskForm()})
    
def edit(request, title):
    # Get an enty content
    entry = util.get_entry(title)
    form = EditForm(initial={"text": entry, "title": title})
    
    # Remove the current entry from the primery list
    if os.path.exists(f"entries/{title}.md"):
        os.remove(f"entries/{title}.md")

    return render(request, "newpage/edit.html", {"form": form, "title": title})

    