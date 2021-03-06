# Generated by Django 3.2.4 on 2021-06-05 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='test_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_round', models.CharField(choices=[('first_round', 'first_round'), ('second_round', 'second_round'), ('third_round', 'third_round')], max_length=200)),
                ('score', models.FloatField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
            ],
        ),
    ]
