# Generated by Django 4.0.2 on 2022-04-06 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=2500)),
                ('q2', models.CharField(max_length=2500)),
                ('q3', models.CharField(max_length=2500)),
            ],
        ),
    ]
