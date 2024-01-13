# Generated by Django 5.0.1 on 2024-01-13 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary_api', '0002_rename_users_user_rename_userwords_userword_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('WordID', models.AutoField(primary_key=True, serialize=False)),
                ('Word', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.CreateModel(
            name='UserWords',
            fields=[
                ('UserWordID', models.AutoField(primary_key=True, serialize=False)),
                ('IsLearned', models.BooleanField(default=False)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary_api.users')),
                ('WordID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary_api.words')),
            ],
        ),
        migrations.DeleteModel(
            name='UserWord',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
