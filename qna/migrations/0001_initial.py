# Generated by Django 3.0.4 on 2020-04-06 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(editable=False)),
                ('modified_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('code', models.TextField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('modified_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(editable=False)),
                ('modified_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('code', models.TextField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('modified_at', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna.Question')),
            ],
        ),
    ]
