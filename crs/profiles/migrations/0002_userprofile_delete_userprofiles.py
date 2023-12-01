# Generated by Django 4.2.3 on 2023-11-30 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=500)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='img')),
                ('about', models.CharField(max_length=300)),
                ('profile_id', models.UUIDField(default=uuid.UUID('5dece241-a1c7-4bee-9057-c753159864c7'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='userProfiles',
        ),
    ]
