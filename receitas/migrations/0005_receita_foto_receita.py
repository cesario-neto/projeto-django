# Generated by Django 3.2.2 on 2021-05-20 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_receita_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(default='', upload_to='', verbose_name='fotos/%d,%m,%Y'),
            preserve_default=False,
        ),
    ]