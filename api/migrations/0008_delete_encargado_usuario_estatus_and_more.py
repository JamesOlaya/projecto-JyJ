# Generated by Django 4.2.5 on 2023-10-20 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_prediop_producto_preciop_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Encargado',
        ),
        migrations.AddField(
            model_name='usuario',
            name='estatus',
            field=models.CharField(default='cliente', max_length=8),
        ),
        migrations.AlterField(
            model_name='estado',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]