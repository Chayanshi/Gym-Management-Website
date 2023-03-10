# Generated by Django 4.1.2 on 2023-01-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentStatus', models.CharField(blank=True, max_length=55, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('FullName', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.CharField(max_length=12)),
            ],
        ),
    ]
