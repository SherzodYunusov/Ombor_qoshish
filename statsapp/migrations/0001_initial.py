# Generated by Django 4.2.1 on 2023-06-03 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Asosiy', '0003_rename_ombor_mahsulot_ombor1_and_more'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateTimeField(auto_created=True)),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('umumiy_summa', models.PositiveSmallIntegerField()),
                ('tolandi', models.PositiveSmallIntegerField()),
                ('nasiya', models.PositiveSmallIntegerField()),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asosiy.mahsulot')),
                ('mijoz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asosiy.mijoz')),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.ombor')),
            ],
        ),
    ]
