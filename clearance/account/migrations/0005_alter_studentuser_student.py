# Generated by Django 4.2.4 on 2023-08-13 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_daouser_students_saouser_students_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
