# Generated by Django 3.2.4 on 2021-07-23 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('H', 'Fight Helicopter'), ('U', 'Unknown')], max_length=1)),
                ('job', models.CharField(choices=[('WTR', 'Waiter'), ('CLN', 'Cleaner'), ('CK', 'Cook'), ('GRD', 'Guard')], max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('date_joined', models.DateField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]
