# Generated by Django 3.0.6 on 2020-05-30 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '4. Articles'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': '1. Authors'},
        ),
        migrations.AlterModelOptions(
            name='citieslist',
            options={'verbose_name_plural': '7. Cities list'},
        ),
        migrations.AlterModelOptions(
            name='fictionbook',
            options={'verbose_name_plural': '2. Fiction books'},
        ),
        migrations.AlterModelOptions(
            name='libraryuseraddress',
            options={'verbose_name_plural': '6. Library user addresses'},
        ),
        migrations.AlterModelOptions(
            name='libraryuserinfo',
            options={'verbose_name_plural': '5. Library user info'},
        ),
        migrations.AlterModelOptions(
            name='sciencebook',
            options={'verbose_name_plural': '3. Science books'},
        ),
        migrations.AlterModelOptions(
            name='streetslist',
            options={'verbose_name_plural': '8. Streets list'},
        ),
    ]
