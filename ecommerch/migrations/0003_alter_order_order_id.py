# Generated by Django 5.1.3 on 2024-12-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerch', '0002_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='72385', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
