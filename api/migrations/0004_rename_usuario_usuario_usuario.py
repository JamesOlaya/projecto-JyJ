# Generated by Django 4.2.5 on 2023-09-08 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_estado_idcliente_alter_estado_idproducto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Usuario',
            new_name='usuario',
        ),
    ]
