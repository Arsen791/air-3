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
    filter_value = request.GET.get('filter')
    all_orders = Orders.objects.all()
    orders = all_orders

    if filter_value:
        orders = orders.filter(OrderName=filter_value)
    print(orders)

    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['ShippingName']
            shipping = Shipping(ShippingName=name)
            shipping.save()
            selected_details = request.POST.getlist("selected_details")
            details = request.POST.getlist("checkbox_service")
            details = [int(i) for i in details]
            detail_counts = request.POST.getlist("detail_counts")

            for detail_id, detail_count in zip(details, detail_counts):
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

            # Сохраняем выбранные значения в сеансе
            request.session['selected_details'] = selected_details
            request.session['detail_counts'] = detail_counts

            return redirect('shiplist')
    else:
        selected_details = request.session.get('selected_details', [])
        detail_counts = request.session.get('detail_counts', [])
        form = ShippingForm()

    context = {
        'form': form,
        'all_orders': all_orders,
        'orders': orders,
        'filter_value': filter_value,
        'selected_details': selected_details,
        'detail_counts': detail_counts,
    }
    return render(request, 'main/crship.html', context)





def shiplist(request):
    a = Shipping.objects.all()
    return render(request, 'main/shiplist.html', {'title': 'Список всех ордеров', 'a': a})
