# Generated by Django 3.2.4 on 2021-07-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(blank=True, max_length=128)),
                ('description', models.TextField(blank=True)),
                ('date_opened', models.DateField(null=True)),
                ('rating', models.FloatField(default=0)),
            ],
        ),
    ]
