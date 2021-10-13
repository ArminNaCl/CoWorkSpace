# Generated by Django 3.1.2 on 2021-10-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('delete_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='delete time')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
