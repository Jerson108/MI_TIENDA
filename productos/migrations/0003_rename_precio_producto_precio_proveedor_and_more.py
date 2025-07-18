# Generated by Django 5.2.3 on 2025-06-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='precio_proveedor',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='disponible',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_sugerido',
            field=models.DecimalField(decimal_places=2, default=70.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
