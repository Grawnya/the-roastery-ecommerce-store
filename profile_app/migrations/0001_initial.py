# Generated by Django 3.2.19 on 2023-08-23 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_full_name', models.CharField(max_length=50)),
                ('profile_email', models.EmailField(max_length=254)),
                ('profile_phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_street_address1', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_street_address2', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_town_or_city', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_county', models.CharField(blank=True, max_length=90, null=True)),
                ('profile_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('website_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('coffee_type', models.CharField(blank=True, choices=[('hawaii', 'Hawaii'), ('brazil', 'Brazil'), ('ethiopia', 'Ethiopia'), ('panama', 'Panama'), ('indonesia', 'Indonesia'), ('peru', 'Peru'), ('costa_rica', 'Costa Rica'), ('burundi', 'Burundi'), ('colombia', 'Colombia'), ('taiwan', 'Taiwan'), ('mexico', 'Mexico'), ('nepal', 'Nepal'), ('kenya', 'Kenya')], default='colombia', max_length=50, null=True)),
                ('roast', models.CharField(blank=True, choices=[('light', 'Light'), ('medium_light', 'Medium-Light'), ('medium', 'Medium'), ('medium_dark', 'Medium Dark'), ('dark', 'Dark')], default='light', max_length=30, null=True)),
                ('website_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
