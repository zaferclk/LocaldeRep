# Generated by Django 2.0.4 on 2018-04-24 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DAppAdiYazilar', '0002_auto_20180424_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='YorumlarTabloAdiKlasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum_yapanin_adi', models.CharField(max_length=200, verbose_name='Yorum Yapan')),
                ('yorum_metni', models.TextField(verbose_name='Yorum')),
                ('yorum_olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('yorum_yapilan_yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Yorumlar', to='DAppAdiYazilar.YazilarTabloAdiKlasi')),
            ],
        ),
    ]