# Generated by Django 2.0.6 on 2018-07-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Manager_Name', models.CharField(max_length=50)),
                ('Event_title', models.CharField(max_length=20)),
                ('Event_venue', models.CharField(max_length=10)),
                ('Event_Details', models.TextField(max_length=500)),
                ('Event_date', models.DateTimeField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
