
from django.shortcuts import render, redirect, get_object_or_404
from finance.forms import FinanceForm
from finance.models import Finance
from django.http import HttpResponse
from django.core.paginator import Paginator

# Добавление операции
def created_finance_view(request):
    if request.method == "POST":
        form = FinanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/finance_list/')
    else:
        form = FinanceForm()

    return render(request, 'finance/create_finance.html', {
        'form': form
    })



def read_finance_view(request):
    finance = Finance.objects.all().order_by("-id")

    paginator = Paginator(finance, 2)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'finance/finance_list.html', {
        'finance': page_obj,
        'page_obj': page_obj
    })


def update_finance_view(request, id):
    finance_id = get_object_or_404(Finance, id=id)

    if request.method == "POST":
        form = FinanceForm(request.POST, instance=finance_id)

        if form.is_valid():
            form.save()
            return redirect('/finance_list/')
    else:
        form = FinanceForm(instance=finance_id)

    return render(request, 'finance/update_finance.html', {
        'form': form,
        'finance_id': finance_id
    })


def delete_finance_view(request, id):
    finance_id = get_object_or_404(Finance, id=id)

    finance_id.delete()

    return HttpResponse('<h1>Вы успешно удалили операцию!</h1>')
