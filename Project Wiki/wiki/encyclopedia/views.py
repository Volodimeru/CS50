from django.shortcuts import render
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, title):
    getEntry = util.get_entry(title)
    if getEntry == None:
        return render(request, "encyclopedia/error.html", {
             "errorMessage": "Requested page was not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": getEntry,
        })

def searchPage(request):
    if request.method =="POST":
        searchInput = request.POST['q']
        page = util.get_entry(searchInput)
        if page is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": searchInput,
            "entry": page,
        })
        else:
            entries = util.list_entries()
            entriesList = []
            for entry in entries:
                if searchInput.lower() in entry.lower():
                    entriesList.append(entry)
            return render(request, "encyclopedia/search.html", {
                "entriesList" : entriesList
            })
def newPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newPage.html")
    else:
        titleInputed = request.POST['title']
        content = request.POST['content']
        alreadyExists = util.get_entry(titleInputed)
        if alreadyExists is not None:
            return render(request, "encyclopedia/error.html", {
                "errorMessage": "Entry with this title already exists"
            })
        else:
            util.save_entry(titleInputed, content)
            entry = util.get_entry(titleInputed)
            return render(request, "encyclopedia/entry.html", {
                "title": titleInputed,
                "entry": entry
            })
def editPage(request):
    if request.method == "POST":
        entryToEdit = request.POST['entryToEdit']
        entry = util.get_entry(entryToEdit)
        return render(request, "encyclopedia/edit.html", {
            "title": entryToEdit,
            "entry": entry,
        })
def saveEdit(request):
    if request.method == "POST":
        entryTosave = request.POST['title']
        entry = request.POST['content']
        util.save_entry(entryTosave, entry)
        editedEntry = util.get_entry(entryTosave)
        return render(request, "encyclopedia/entry.html", {
            "title": entryTosave,
            "entry": editedEntry,
        })
def randomPage(request):
    entryList = util.list_entries()
    randEntry = random.choice(entryList)
    entry = util.get_entry(randEntry)
    return render(request,"encyclopedia/entry.html", {
        "title": randEntry,
         "entry": entry,
    })