# Generated by Django 3.2.8 on 2021-11-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='creator',
            field=models.CharField(default='David Stumbra', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Creator',
        ),
    ]
