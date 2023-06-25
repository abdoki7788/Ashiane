# Generated by Django 4.2.2 on 2023-06-25 17:06

import django.contrib.auth.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_delete_otpcode_alter_pendinguser_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pendinguser",
            name="full_name",
        ),
        migrations.RemoveField(
            model_name="pendinguser",
            name="id",
        ),
        migrations.RemoveField(
            model_name="user",
            name="full_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="id",
        ),
        migrations.AddField(
            model_name="pendinguser",
            name="auth_method",
            field=models.CharField(
                choices=[("number", "شماره تلفن"), ("email", "ایمیل")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="pendinguser",
            name="email",
            field=models.EmailField(
                blank=True,
                max_length=254,
                null=True,
                unique=True,
                verbose_name="آدرس ایمیل",
            ),
        ),
        migrations.AddField(
            model_name="pendinguser",
            name="username",
            field=models.CharField(
                default="root",
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 60 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=60,
                primary_key=True,
                serialize=False,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="نام کاربری",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(
                default="root",
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 60 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=60,
                primary_key=True,
                serialize=False,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="نام کاربری",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="pendinguser",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                unique=True,
                verbose_name="شماره تلفن",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                unique=True,
                verbose_name="شماره تلفن",
            ),
        ),
    ]