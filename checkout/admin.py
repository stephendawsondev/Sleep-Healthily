from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'shipping_cost', 'order_subtotal',
                       'order_total', 'original_cart',
                       'stripe_pid')

    fields = (
        'order_number',
        'user_profile',
        'date',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'shipping_cost',
        'order_subtotal',
        'order_total',
        'original_cart',
        'stripe_pid')

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_subtotal', 'shipping_cost',
                    'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
