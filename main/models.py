from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    login = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role)
    status = models.CharField(max_length=255)


class Contracts(models.Model):
    id = models.AutoField(primary_key=True)  # уникальный номер контракта
    supplier_code = models.CharField(max_length=255)  # код поставщика из системы TRAX
    reg_num = models.CharField(max_length=255)  # регистрационный номер из системы TRAX
    pot_num = models.CharField(max_length=255)  # POT number


class ShipToAddress(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    contact_person = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    airport = models.CharField(max_length=100, null=False)

class PickupAddress(models.Model):

    id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    contact_person = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    airport = models.CharField(max_length=100, null=False)

class Airports(models.Model):

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, null=False)
    airport_name = models.CharField(max_length=100, null=False)
    TYPE_CHOICES = [
        ('INT', 'Международные'),
        ('EAEU', 'Аэропорты стран Таможенного союза'),
        ('LOCAL', 'Внутренние аэропорты'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)


class RequestforExportShipment(models.Model):

    order_number = models.IntegerField(max_length=255)  # номер заказа
    order_code = models.CharField(max_length=255)  # код заказа
    order_line = models.CharField(max_length=255)  # линия заказа
    pn = models.CharField(max_length=255)  # партийный номер заказа
    sn = models.CharField(max_length=255)  # серийный номер заказа
    quantity = models.IntegerField()  # количество по заказу
    customs_value = models.DecimalField(max_digits=10, decimal_places=2)  # общая стоимость заказа
    currency = models.CharField(max_length=255)  # валюта
    country_of_origin = models.CharField(max_length=255)  # страна происхождения
    agreement = models.ForeignKey(Contracts, on_delete=models.CASCADE)  # контракт
    pot = models.CharField(max_length=255, editable=False)  # PoT
    delivery_terms = models.CharField(max_length=255)  # условия доставки
    ship_to_address = models.ForeignKey(ShipToAddress, on_delete=models.CASCADE)  # адрес назначения
    contact_details = models.CharField(max_length=255)  # контактные данные
    required_delivery_date_to_vendor = models.DateField()  # предпочитаемая дата доставки
    priority_by_initiator = models.CharField(max_length=255)  # приоритет по инициатору
    c_check = models.CharField(max_length=255)  # C-Check
    edit_approval = models.BooleanField(default=False)  # подтверждение редактирования
    comments = models.TextField()  # комментарии
    created_by = models.CharField(max_length=255)  # создано пользователем
    date = models.DateField(auto_now_add=True)  # дата создания


class Waybill(models.Model):
    waybill_number = models.CharField(max_length=255)  # номер авианакладной
    svc = models.BooleanField()  # checkbox поле SVC
    DEPARTURE_CHOICES = [
        ('INT', 'Международные'),
        ('EAEU', 'Аэропорты стран Таможенного союза'),
        ('LOCAL', 'Внутренние аэропорты'),
    ]
    departure_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES)
    transfer_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES, blank=True, null=True)
    arrival_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES)  # аэропорт прибытия
    expected_departure = models.DateField()  # предполагаемая дата вылета
    service_provider = models.CharField(max_length=255)  # поставщик услуги
    agent_notify_party = models.CharField(max_length=255)  # агент/сообщающая сторона
    handling_info = models.TextField()  # информация об обработке
    back_to_initiated = models.BooleanField()  # checkbox поле Back to Initiated
    passed_to_cargo_handling = models.DateField(blank=True, null=True)  # дата передачи в грузовую обработку
    placed_to_bonded_warehouse = models.DateField(blank=True, null=True)  # дата помещения в таможенный склад
    passed_to_customs = models.DateField(blank=True, null=True)  # дата передачи в таможню
    assigned_to_declarant = models.CharField(max_length=255)  # назначен декларанту
    passed_to_declarant = models.DateField(blank=True, null=True)  # дата передачи декларанту
    departure_date = models.DateField()  # дата вылета
    assigned_to_officer_logistics = models.CharField(max_length=255)  # назначено логистическому офицеру
    pod = models.DateField(blank=True, null=True)  # дата доставки груза
    created_date = models.DateField(auto_now_add=True)  # дата создания (по умолчанию текущая дата)


class Packing(models.Model):
    length = models.DecimalField(max_digits=10, decimal_places=2)  # длина (в см)
    width = models.DecimalField(max_digits=10, decimal_places=2)  # ширина (в см)
    height = models.DecimalField(max_digits=10, decimal_places=2)  # высота (в см)
    diameter = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # диаметр (в см)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)  # нетто-вес (в кг)
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  # брутто-вес (в кг)
    aircraft_type = models.CharField(max_length=255)  # тип воздушного судна
    package_type = models.CharField(max_length=255)  # тип упаковки
    dangerous_goods = models.BooleanField()  # наличие опасных грузов
    un_code = models.CharField(max_length=255)  # UN-код
    assigned_to = models.CharField(max_length=255)  # назначено
    created_date = models.DateField(auto_now_add=True)  # дата создания (по умолчанию текущая дата)


class Invoice(models.Model):
    item = models.CharField(max_length=255)  # товар
    order_number = models.CharField(max_length=255)  # номер заказа
    part_description = models.CharField(max_length=255)  # описание детали
    part_number = models.CharField(max_length=255)  # номер детали
    serial_number = models.CharField(max_length=255)  # серийный номер
    unit_of_measure = models.CharField(max_length=255)  # единица измерения
    quantity = models.IntegerField()  # количество
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # цена за единицу
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)  # общая стоимость
    currency = models.CharField(max_length=255)  # валюта



class PackingList(models.Model):
    item = models.CharField(max_length=255)  # товар
    box_id = models.CharField(max_length=255)  # идентификатор коробки
    package_type = models.CharField(max_length=255)  # тип упаковки
    dimensions = models.CharField(max_length=255)  # размеры (в см)
    part_description = models.CharField(max_length=255)  # описание детали
    part_number = models.CharField(max_length=255)  # номер детали
    serial_number = models.CharField(max_length=255)  # серийный номер
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  # брутто-вес (в кг)
    nett_weight = models.DecimalField(max_digits=10, decimal_places=2)  # нетто-вес (в кг)
    unit_of_measure = models.CharField(max_length=255)  # единица измерения
    quantity = models.IntegerField()  # количество



class ImportShipment(models.Model):
    order_number = models.CharField(max_length=255)  # номер заказа из Тракса
    order_code = models.CharField(max_length=255)  # код заказа
    order_line = models.CharField(max_length=255)  # линия заказа
    part_number = models.CharField(max_length=255)  # партийный номер заказа
    agreement = models.CharField(max_length=255)  # актуальные контракты
    pot = models.CharField(max_length=255)  # PoT (Point of Transfer)
    payment_terms = models.CharField(max_length=255)  # условия оплаты
    delivery_terms = models.CharField(max_length=255)  # условия доставки
    pick_up_address_contact = models.CharField(max_length=255)  # адрес и контакт для забора
    ship_to_address = models.CharField(max_length=255)  # адрес доставки
    c_check = models.BooleanField(default=False)  # флаг для C-Check
    comments = models.TextField()  # комментарии
    edit_approval = models.BooleanField(default=False)  # разрешение на редактирование
    CHOICES = [
        ('AOG', 'AOG'),
        ('Urgent', 'Urgent'),
        ('Routine', 'Routine'),
    ]
    priority  = models.CharField(max_length=100, choices=CHOICES)


class PreShipment(models.Model):
    serial_number = models.CharField(max_length=255)  # серийный номер
    quantity = models.PositiveIntegerField()  # количество
    customs_value = models.DecimalField(max_digits=10, decimal_places=2)  # стоимость в таможенной декларации
    currency = models.CharField(max_length=3)  # валюта
    actual_pick_up_date = models.DateField()  # фактическая дата забора
    remark = models.TextField()  # примечание


class ImportWaybill(models.Model):
    waybill_number = models.CharField(max_length=255)  # номер авианакладной
    hawb = models.CharField(max_length=255)  # HAWB
    DEPARTURE_CHOICES = [
        ('INT', 'Международные'),
        ('EAEU', 'Аэропорты стран Таможенного союза'),
        ('LOCAL', 'Внутренние аэропорты'),
    ]
    departure_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES)
    transfer_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES, blank=True, null=True)
    arrival_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES)  # аэропорт прибытия
    flight_number = models.CharField(max_length=255)  # номер рейса
    departure_date = models.DateField()  # дата отправления
    expected_delivery_to_terminal = models.DateField()  # ожидаемая дата доставки в терминал
    expected_delivery_to_stores = models.DateField()  # ожидаемая дата доставки в магазины
    service_provider = models.CharField(max_length=255)  # поставщик услуг
    quantity_of_pieces = models.PositiveIntegerField()  # количество единиц груза
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  # вес груза (брутто)
    chargeable_weight = models.DecimalField(max_digits=10, decimal_places=2)  # вес груза (затариваемый)
    urgent = models.BooleanField()  # флаг срочности
    assigned_to_officer = models.CharField(max_length=255)  # назначенный сотрудник
    assigned_date = models.DateField()  # дата назначения
    arrival_date = models.DateField()  # дата прибытия
    lost_damaged_report_number = models.CharField(max_length=255)  # номер отчета о потере или повреждении
    lost_damaged_report_date = models.DateField()  # дата отчета о потере или повреждении
    lost_damaged_report_description = models.TextField()  # описание отчета о потере или повреждении
    vdt = models.DateField()  # VDT (время доставки в пункт назначения)
    docs_passed_to_clearance = models.DateField()  # дата передачи документов на таможенное оформление
    docs_passed_to_customs = models.DateField()  # дата передачи документов в таможню
    assigned_to_declarant = models.CharField(max_length=255)  # назначенный декларант
    assigned_date_to_declarant = models.DateField()  # дата назначения декларанта
    delivered_to_stores = models.DateField()  # дата доставки в магазины
    delivered_to_stores_by = models.CharField(max_length=255)  # поставщик доставки в магазины
    remarks = models.TextField()  # примечания


class RelatedLinkOrder(models.Model):
    waybill = models.ForeignKey(ImportWaybill, on_delete=models.CASCADE)  # связь с авианакладной
    order_number = models.CharField(max_length=255)  # номер заказа
    link_date = models.DateField()  # дата связи


class ImportTransitWaybill(models.Model):
    waybill_number = models.CharField(max_length=255)  # номер накладной
    DEPARTURE_CHOICES = [
        ('INT', 'Международные'),
        ('EAEU', 'Аэропорты стран Таможенного союза'),
        ('LOCAL', 'Внутренние аэропорты'),
    ]
    transfer_waybill = models.CharField(max_length=100, choices=DEPARTURE_CHOICES, blank=True, null=True)
    departure_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES)
    arrival_airport = models.CharField(max_length=100, choices=DEPARTURE_CHOICES)  # аэропорт прибытия
    flight_number = models.CharField(max_length=255)  # номер рейса
    departure_date = models.DateField()  # дата отправления
    arrival_date = models.DateField()  # дата прибытия
    lost_damaged_report_number = models.CharField(max_length=255)  # номер отчета о потере или повреждении
    lost_damaged_report_date = models.DateField()  # дата отчета о потере или повреждении
    lost_damaged_report_description = models.TextField()  # описание отчета о потере или повреждении
    delivered_to_stores = models.DateField()  # дата доставки в магазины
    delivered_to_stores_by = models.CharField(max_length=255)  # поставщик доставки в магазины
    remarks = models.TextField()  # примечания



class RelatedMainMAWB(models.Model):
    import_transit_waybill = models.ForeignKey(ImportTransitWaybill, on_delete=models.CASCADE)  # связь с накладной Import/Transit Waybill
    main_mawb = models.CharField(max_length=255)  # главная MAWB
    order_number = models.CharField(max_length=255)  # номер заказа
    link_date = models.DateField()  # дата связи



class Details(models.Model):
    DetailName = models.CharField('Detail Name', max_length=100)
    Count = models.IntegerField('Count of details')
    DeliveryCountry = models.CharField('Delivery Country', max_length=100)


class Orders(models.Model):
    OrderName = models.IntegerField('Name of order')
    OrderDate = models.DateField('Date when order came')
    Details = models.ManyToManyField(Details)
    airport = models.ForeignKey(Airports, related_name='airport', on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(PickupAddress, related_name='address', on_delete=models.CASCADE, null=True)


class ShippingDetails(models.Model):
    DetailName = models.CharField('Detail Name', max_length=100)
    Count = models.IntegerField('Count of details')

class Shipping(models.Model):
    ShippingName = models.CharField('Name of Shipping', max_length=50)
    Details = models.ManyToManyField(ShippingDetails)




