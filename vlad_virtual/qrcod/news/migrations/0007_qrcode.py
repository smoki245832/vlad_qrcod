# Generated by Django 3.1.1 on 2021-05-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210422_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
            ],
        ),
    ]
