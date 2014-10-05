#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django import forms

from shop.models import Order

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'ingredients',
        )
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', u'Make an order'))