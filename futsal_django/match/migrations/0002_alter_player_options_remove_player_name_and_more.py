# Generated by Django 4.0.1 on 2022-02-02 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': '選手', 'verbose_name_plural': '選手'},
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.AddField(
            model_name='player',
            name='birth_day',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='誕生日'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='first_name',
            field=models.CharField(default='サンプル', max_length=32, verbose_name='名前（漢字）'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(default=' ', max_length=32, verbose_name='苗字（漢字）'),
        ),
        migrations.AddField(
            model_name='player',
            name='uniform_number',
            field=models.IntegerField(default=0, verbose_name='背番号'),
        ),
    ]
