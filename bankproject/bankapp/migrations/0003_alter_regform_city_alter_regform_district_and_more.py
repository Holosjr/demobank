# Generated by Django 4.2.5 on 2023-09-18 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_regform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.sbranch'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.branch'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
    ]