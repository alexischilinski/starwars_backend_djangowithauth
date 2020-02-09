# Generated by Django 3.0.2 on 2020-02-09 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('starwarsapi', '0028_userwildlife_diet'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercharacter',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usercharacters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userplanet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userplanets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userwildlife',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userwildlife', to=settings.AUTH_USER_MODEL),
        ),
    ]
