# Generated by Django 4.0 on 2022-03-11 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ombor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanasi', models.DateTimeField()),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('umumiy_summa', models.IntegerField()),
                ('tolandi', models.IntegerField()),
                ('nasiyaga', models.IntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ombor_app.client')),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ombor_app.ombor')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ombor_app.product')),
            ],
        ),
    ]