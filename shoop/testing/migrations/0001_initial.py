# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoop', '0020_services_and_methods'),
    ]

    operations = [
        migrations.CreateModel(
            name='PseudoPaymentProcessor',
            fields=[
                ('paymentprocessor_ptr', models.OneToOneField(parent_link=True, to='shoop.PaymentProcessor', serialize=False, primary_key=True, auto_created=True)),
                ('bg_color', models.CharField(default='white', max_length=20, verbose_name='Payment Page Background Color', blank=True)),
                ('fg_color', models.CharField(default='black', max_length=20, verbose_name='Payment Page Text Color', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('shoop.paymentprocessor',),
        ),
    ]
