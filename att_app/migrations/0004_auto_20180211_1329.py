# Generated by Django 2.0.1 on 2018-02-11 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0003_auto_20180211_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_details',
            name='t_id',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
