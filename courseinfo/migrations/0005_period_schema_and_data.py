# Generated by Django 2.1.7 on 2019-10-30 16:51

from django.db import migrations, models


PERIODS =[
    {
        "period_sequence": 9999,
        "period_name": "TemporaryValue",
    },
    {
        "period_sequence":10,
        "period_name":"Spring",
    },
    {
        "period_sequence":20,
        "period_name":"Summer",
    },
    {
        "period_sequence": 30,
        "period_name": "Fall",
    },
    {
        "period_sequence": 40,
        "period_name": "Winter",
    },

]


def add_period_data(apps, schema_editor):
    period_class = apps.get_model('courseinfo','Period')
    for this_period in PERIODS:
        period_object = period_class.objects.create(
            period_sequence = this_period['period_sequence'],
            period_name=this_period['period_name']
        )
        period_object.save()

def remove_period_data(apps, schema_editor):
    period_class = apps.get_model('courseinfo','Period')
    for this_period in PERIODS:
        period_object = period_class.objects.get(
            period_sequence=this_period['period_sequence']
        )
        period_object.delete()

        

class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0004_semester_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('period_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_sequence', models.IntegerField(unique=True)),
                ('period_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'ordering': ['period_sequence'],
            },
        ),
        migrations.RunPython(
            add_period_data,
            remove_period_data
        ),
    ]
