# Generated by Django 4.2.5 on 2023-09-05 18:48

from django.db import migrations, models
import django.db.models.deletion
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_musician_person_shirt_size_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateTimeField(default=task.models.default_to_one_week)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.category')),
            ],
            options={
                'ordering': ('-due_date',),
            },
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['title'], name='task_catego_title_4a63ad_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['-due_date', '-created'], name='task_task_due_dat_b07c0b_idx'),
        ),
    ]