# Generated by Django 4.2.4 on 2023-08-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rise', '0004_remove_interview_id_alter_interview_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='object_type_2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
