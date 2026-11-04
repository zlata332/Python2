
from django.shortcuts import render, redirect, get_object_or_404
from finance.forms import FinanceForm
from finance.models import Finance
from django.http import HttpResponse


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


# Список операций
def read_finance_view(request):
    finance = Finance.objects.all().order_by("-id")

    return render(request, 'finance/finance_list.html', {
        'finance': finance
    })


# Изменение операции
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


# Удаление операции
def delete_finance_view(request, id):
    finance_id = get_object_or_404(Finance, id=id)

    finance_id.delete()

    return HttpResponse('<h1>Вы успешно удалили операцию!</h1>')
