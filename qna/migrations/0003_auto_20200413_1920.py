# Generated by Django 3.0.4 on 2020-04-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_question_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.TextField(blank=True),
        ),
    ]