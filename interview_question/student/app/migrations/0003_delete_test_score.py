# Generated by Django 3.2.4 on 2021-06-05 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_candidate_test_score_candi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test_score',
        ),
    ]