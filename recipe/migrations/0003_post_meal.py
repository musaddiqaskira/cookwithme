# Generated by Django 3.1.7 on 2021-02-28 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='recipe_meals', to='recipe.meal'),
        ),
    ]
