# Generated by Django 3.1.5 on 2021-02-12 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210212_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='news',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='news.news', verbose_name='Меропреятие'),
            preserve_default=False,
        ),
    ]
