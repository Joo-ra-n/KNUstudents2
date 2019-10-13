# Generated by Django 2.2.4 on 2019-08-24 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('introduction', 'introduction')], max_length=50)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('text', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='info_photo/%Y/%m/%d')),
                ('file', models.FileField(blank=True, upload_to='info_file/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_operation_introduction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('board', 'board')], max_length=50)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('text', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='info_photo/%Y/%m/%d')),
                ('file', models.FileField(blank=True, upload_to='info_file/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_operation_board', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
