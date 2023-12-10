# Generated by Django 2.2.24 on 2023-12-09 15:05

from django.db import migrations

def move_owners_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            name=flat.owner,
            phone_number=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone,
        )



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(move_owners_data)
    ]
