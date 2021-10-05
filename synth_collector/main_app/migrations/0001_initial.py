# Generated by Django 3.2.7 on 2021-10-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Synths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maker', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('img', models.CharField(max_length=255)),
                ('info', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
