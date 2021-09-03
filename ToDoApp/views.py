from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ToDoApp.models import ToDoItem

# Create your views here.
def todo(request):
    all_todo_items=ToDoItem.objects.all()
    return render(request,"ToDoApp/index.html",
        {'All_items':all_todo_items})

def addToDo(request):
    new_item=ToDoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/Todo/')

def deleteToDo(request,todo_id):
    item_to_delete=ToDoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/Todo/')
