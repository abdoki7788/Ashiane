# Generated by Django 4.2.2 on 2023-06-25 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_pendinguser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OtpCode",
        ),
        migrations.AlterModelOptions(
            name="pendinguser",
            options={
                "verbose_name": "کاربر در انتظار",
                "verbose_name_plural": "کاربران در انتظار",
            },
        ),
    ]