# Generated by Django 3.2.5 on 2021-07-26 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_chioce_txt_choice_choice_txt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='auestion_text',
            new_name='question_text',
        ),
    ]
