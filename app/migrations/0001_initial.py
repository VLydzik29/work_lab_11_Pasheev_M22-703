# Generated by Django 4.2.7 on 2023-11-12 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('purpose', models.IntegerField(choices=[(1, 'Для рядовых'), (2, 'Для офицеров')], default=1)),
            ],
            options={
                'verbose_name': 'Казарма',
                'verbose_name_plural': 'Казармы',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Оружие',
                'verbose_name_plural': 'Оружие',
            },
        ),
        migrations.CreateModel(
            name='Military',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255)),
                ('service_start_date', models.CharField(max_length=255)),
                ('service_end_date', models.CharField(default='н.в.', max_length=255)),
                ('barracks_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.barracks')),
                ('received_weapon', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.weapon')),
            ],
            options={
                'verbose_name': 'Военный',
                'verbose_name_plural': 'Военные',
            },
        ),
    ]