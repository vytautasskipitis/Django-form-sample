from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import CustomerMessage


def CustomerMessageList(request):
    context = {'CustomerMessageList': CustomerMessage.objects.all()}
    return render(request, "customer_form_register/CustomerMessageList.html", context)


def CustomerMessageForm(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            form_update = CustomerMessage.objects.get(pk=id)
            form = CustomerForm(instance=form_update)
        return render(request, "customer_form_register/CustomerMessageForm.html", {'form':form})
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            form_update = CustomerMessage.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=form_update)
        if form.is_valid():
            form.save()
        return redirect('/customer_message_form/list')


def CustomerMessageDelete(request, id):
    form_update = CustomerMessage.objects.get(pk=id)
    form_update.delete()
    return redirect('/customer_message_form/list')








