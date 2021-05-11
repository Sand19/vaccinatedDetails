# Generated by Django 3.1.4 on 2021-05-11 11:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vaccineDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50, unique=True)),
                ('staff_no', models.PositiveIntegerField(unique=True)),
                ('dp_code', models.PositiveIntegerField()),
                ('branch_name', models.CharField(max_length=50)),
                ('ro_code', models.PositiveIntegerField()),
                ('circle_name', models.CharField(choices=[('Agra', 'Agra'), ('Ahmedabad', 'Ahmedabad'), ('Bangalore', 'Bangalore'), ('Bhopal', 'Bhopal'), ('Bhubaneswar', 'Bhubaneswar'), ('Chandigarh', 'Chandigarh'), ('Chennai', 'Chennai'), ('Delhi', 'Delhi'), ('Guwahati', 'Guwahati'), ('Headoffice', 'Headoffice'), ('Hyderabad', 'Hyderabad'), ('Hubballi', 'Hubballi'), ('Jaipur', 'Jaipur'), ('Karnal', 'Karnal'), ('Kolkata', 'Kolkata'), ('Lucknow', 'Lucknow'), ('Madurai', 'Madurai'), ('Mangalore', 'Mangalore'), ('Manipal', 'Manipal'), ('Mumbai', 'Mumbai'), ('Patna', 'Patna'), ('Pune', 'Pune'), ('Ranchi', 'Ranchi'), ('Trivandrum', 'Trivandrum'), ('Vijayawada', 'Vijayawada')], max_length=11)),
                ('vaccinated', models.CharField(choices=[('None', 'None'), ('Single', 'Single'), ('Both', 'Both')], max_length=6)),
                ('vaccinated_date', models.DateTimeField()),
                ('contact_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Valid Phone number must be entered !!', regex='^[6-9]\\d{9}$')])),
                ('submit_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Vaccinated Details',
            },
        ),
    ]
