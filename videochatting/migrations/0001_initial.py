# Generated by Django 4.2.6 on 2023-10-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=252)),
                ('phone', models.CharField(max_length=12)),
                ('feedback', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
