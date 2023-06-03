from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Orders, Details, Shipping, ShippingDetails
from .forms import OrdersForm, DetailForm, ShippingForm
from django.http import JsonResponse




def index(request):
    return render(request, 'main/index.html')

def test(request):
    return render(request, 'main/test.html')


def order(request):
    if request.method == 'GET':
        a = Orders.objects.all()
        form = OrdersForm()
        return render(request, 'main/order.html', {'title': 'Список всех ордеров', 'form': form, 'a': a})

    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            if Orders.objects.filter(OrderName=form.cleaned_data['OrderName']).count() == 0:
                order = Orders(OrderName=form.cleaned_data['OrderName'],
                               OrderDate=form.cleaned_data['OrderDate'])
                order.save()
            else:
                order = Orders.objects.get(OrderName=form.cleaned_data['OrderName'])
            detail = Details(DetailName=form.cleaned_data['DetailName'], Count=form.cleaned_data['Count'],
                             DeliveryCountry=form.cleaned_data['DeliveryCountry']
                             )
            detail.save()
            order.save()
            order.Details.add(detail)
            return redirect('/')
        else:
            print(form.errors)
            a = Orders.objects.all()
            form = OrdersForm()
            return render(request, 'main/order.html', {'title': 'Список всех ордеров', 'form': form, 'a': a})



def create(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            
            if Orders.objects.filter(OrderName=form.cleaned_data['OrderName']).count() == 0:
                order = Orders(OrderName=form.cleaned_data['OrderName'],
                               OrderDate=form.cleaned_data['OrderDate'])
                order.save()
            else:
                order = Orders.objects.get(OrderName=form.cleaned_data['OrderName'])
            detail = Details(DetailName=form.cleaned_data['DetailName'], Count=form.cleaned_data['Count'],
                             DeliveryCountry=form.cleaned_data['DeliveryCountry']
                             )
            detail.save()
            order.Details.add(detail)
            order.save()
        
    form = OrdersForm()

    context = {
        'form': form,
    }
    return render(request, 'main/create.html', context)


def edit_detail(request, pk):
    if request.method == 'POST':
        detail = Details.objects.get(pk=pk)
        detail_name = request.POST.get('detail_name')
        count = request.POST.get('count')
        delivery_country = request.POST.get('delivery_country')
        
        detail.DetailName = detail_name
        detail.Count = count
        detail.DeliveryCountry = delivery_country
        detail.save()
        
        return redirect('/order'.format(pk=pk))
        
    return render(request, 'main/order.html')  



@csrf_exempt
def delete_order_detail(request, pk):
    if request.method == 'DELETE':
        try:
            data = Details.objects.get(pk=pk)
            data.delete()
            return JsonResponse({'success': True})
        except Details.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Data not found'}, status=404)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


def change_order_detail(request, pk):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            detail = Details.objects.get(pk=pk)
            detail.DetailName = form.cleaned_data['DetailName']
            detail.Count = Count = form.cleaned_data['Count']
            detail.DeliveryCountry = form.cleaned_data['DeliveryCountry']
            detail.save()

    form = DetailForm()

    context = {
        'form': form
    }
    return render(request, 'main/change_detail.html', context)


def crship(request):
    checkbox_service_values = []
    detail_counts_values = []

    filter_value = request.GET.get('filter')
    orders = Orders.objects.all()

    if filter_value:
        orders = orders.filter(OrderName=filter_value)

    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['ShippingName']
            shipping = Shipping(ShippingName=name)
            shipping.save()

            details = request.POST.getlist("checkbox_service")
            details = [int(i) for i in details]
            details_count = request.POST.getlist('detail_counts')
            checkbox_service_values = request.POST.getlist('checkbox_service')
            detail_counts_values = request.POST.getlist('detail_counts')

            for detail_id, detail_count in zip(details, details_count):
                try:
                    detail = Details.objects.get(pk=detail_id)
                    detail.Count -= int(detail_count)
                    if detail.Count == 0:
                        detail.delete()
                    else:
                        detail.save()

                    sh_detail = ShippingDetails(DetailName=detail.DetailName, Count=detail_count)
                    sh_detail.save()

                    shipping.Details.add(sh_detail)
                except Details.DoesNotExist:
                    # Обработка случая, когда детали не найдены
                    pass

            return redirect('shiplist')
    else:
        form = ShippingForm()

    context = {
        'form': form,
        'orders': orders,
        'filter_value': filter_value,
        'checkbox_service_values': checkbox_service_values,
        'detail_counts_values': detail_counts_values,
    }
    return render(request, 'main/crship.html', context)






def shiplist(request):
    a = Shipping.objects.all()
    return render(request, 'main/shiplist.html', {'title': 'Список всех ордеров', 'a': a})
