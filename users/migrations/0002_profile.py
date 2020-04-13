# Generated by Django 3.0.4 on 2020-04-13 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(default='Hey there! I am using Askub', max_length=255)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profiles/')),
                ('current_role', models.CharField(blank=True, choices=[('student', 'Student'), ('teacher', 'Teacher'), ('freelancer', 'Freelancer'), ('working-professional', 'Working Professional')], max_length=155)),
                ('working_at', models.CharField(blank=True, max_length=155)),
                ('city', models.CharField(blank=True, max_length=155)),
                ('country', models.CharField(default='India', max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
