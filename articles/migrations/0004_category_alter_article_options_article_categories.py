# Generated by Django 4.0.5 on 2022-06-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_content_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publication_date']},
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='articles.category'),
        ),
    ]
