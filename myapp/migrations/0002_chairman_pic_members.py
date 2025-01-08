# Generated by Django 5.1.4 on 2025-01-06 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='media/defaultpic.png', upload_to='media/images/'),
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=10)),
                ('block_no', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=15)),
                ('family_members', models.CharField(max_length=15)),
                ('vehicle_details', models.CharField(max_length=30)),
                ('blood_group', models.CharField(max_length=5)),
                ('job_description', models.CharField(max_length=30)),
                ('job_address', models.TextField()),
                ('pic', models.FileField(default='media/defaultpic.png', upload_to='media/images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
