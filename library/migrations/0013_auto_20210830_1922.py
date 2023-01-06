
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20210830_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='expiry_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.CharField(max_length=10),
        ),
    ]
