# Generated by Django 3.0.5 on 2020-12-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationForAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_date', models.DateField(default='')),
                ('operation_type', models.CharField(default='', max_length=70)),
                ('details', models.CharField(default='', max_length=200)),
                ('cost', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
