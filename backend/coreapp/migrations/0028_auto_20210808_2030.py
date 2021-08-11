# Generated by Django 3.2.4 on 2021-08-08 11:30

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0027_scratch_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compilerconfiguration',
            name='compiler',
        ),
        migrations.RemoveField(
            model_name='assembly',
            name='compiler_config',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='compiler_config',
        ),
        migrations.RemoveField(
            model_name='scratch',
            name='compiler_config',
        ),
        migrations.AddField(
            model_name='assembly',
            name='as_opts',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='assembly',
            name='compiler',
            field=models.CharField(default='gcc2.8.1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compilation',
            name='as_opts',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='compilation',
            name='cc_opts',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='compilation',
            name='compiler',
            field=models.CharField(default='gcc2.8.1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compilation',
            name='cpp_opts',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='scratch',
            name='as_opts',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='scratch',
            name='cc_opts',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='scratch',
            name='compiler',
            field=models.CharField(default='gcc2.8.1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scratch',
            name='cpp_opts',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='assembly',
            name='object',
            field=models.FilePathField(path=pathlib.PurePosixPath('/home/ethteck/repos/decomp.me/backend/local_files/assemblies')),
        ),
        migrations.AlterField(
            model_name='compilation',
            name='object',
            field=models.FilePathField(path=pathlib.PurePosixPath('/home/ethteck/repos/decomp.me/backend/local_files/compilations')),
        ),
        migrations.DeleteModel(
            name='Compiler',
        ),
        migrations.DeleteModel(
            name='CompilerConfiguration',
        ),
    ]