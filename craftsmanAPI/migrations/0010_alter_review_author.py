# Generated by Django 4.2.7 on 2024-03-02 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craftsmanAPI', '0009_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='craftsmanAPI.visitor'),
        ),
    ]
