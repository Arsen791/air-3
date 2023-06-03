def crship(request):
    if request.method == 'POST':
        print('error')
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

            print(details)
            print(current_details)
            print(details_count)
            print(count_indexes_in_detail)

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
    filter_value = request.GET.get('filter')
    orders = Orders.objects.all()
    print("Filter value:", filter_value)  # Отладочное сообщение
    if filter_value:
        orders = orders.filter(OrderName=filter_value)
    print("Filtered orders:", orders) 
    context = {
        'form': form,
        'orders': orders,
        'filter_value': filter_value
    }
    return render(request, 'main/crship.html', context)