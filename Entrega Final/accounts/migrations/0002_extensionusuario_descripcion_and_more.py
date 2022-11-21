# Generated by Django 4.1.1 on 2022-11-03 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionusuario',
            name='descripcion',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='extensionusuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
