# Generated by Django 5.1.3 on 2024-12-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerch', '0008_alter_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='9E91D', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
