from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Orders, Details, Shipping, ShippingDetails
from .forms import OrdersForm, DetailForm, ShippingForm
from django.http import JsonResponse



def index(request):
    return render(request, 'main/index.html')


def order(request):
    a = Orders.objects.all()
    return render(request, 'main/order.html', {'title': 'Список всех ордеров', 'a': a})


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
        'form': form
    }
    return render(request, 'main/create.html', context)


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
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        name = request.POST.get('ShippingName', '')
        country = request.POST.get('DeliveryCountry', '')
        day = request.POST.get('ShippingDate_day', '')
        month = request.POST.get('ShippingDate_month', '')
        year = request.POST.get('ShippingDate_year', '')
        if len(day) < 2:
            day = '0' + day
        date = year + '-' + month + '-' + day

        is_present = Shipping.objects.filter(ShippingName=name).exists()

        if not is_present:
            shipping = Shipping(ShippingName=name,
                                ShippingDate=date,
                                DeliveryCountry=country)
            shipping.save()

            details = request.POST.getlist("checkbox_service")
            details = [int(i) for i in details]
            current_details = Details.objects.values_list('pk')
            details_count = request.POST.getlist('detail_counts')

            count_indexes_in_detail = []

            for i in range(len(current_details)):
                if current_details[i][0] in details:
                    count_indexes_in_detail.append(str(i))

            details_count = [details_count[i] for i in range(len(details_count)) if str(i) in count_indexes_in_detail]

            # print(details)
            # print(current_details)
            # print(details_count)
            # print(count_indexes_in_detail)

            for i in range(len(details)):
                detail = Details.objects.get(pk=details[i])
                detail.Count -= int(details_count[i])
                if detail.Count == 0:
                    detail.delete()
                detail.save()

                sh_detail = ShippingDetails(DetailName=detail.DetailName,
                                Count=details_count[i])
                sh_detail.save()
                shipping.Details.add(sh_detail)
                shipping.save()

        return redirect('shiplist')

    form = ShippingForm()
    context = {
        'form': form,
        'orders': Orders.objects.all()
    }
    return render(request, 'main/crship.html', context)


def shiplist(request):
    a = Shipping.objects.all()
    return render(request, 'main/shiplist.html', {'title': 'Список всех ордеров', 'a': a})
