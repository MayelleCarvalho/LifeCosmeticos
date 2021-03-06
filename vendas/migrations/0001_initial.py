# Generated by Django 2.1.3 on 2018-12-09 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total_item', models.FloatField()),
                ('qtd_item', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_produto', models.FileField(upload_to='')),
                ('descricao', models.CharField(max_length=100)),
                ('qtd_estoque', models.IntegerField()),
                ('valor_unit', models.FloatField()),
                ('categoria', models.CharField(choices=[('hidra', 'Hidratantes'), ('perfumes', 'Perfumes'), ('maquiagem', 'Maquiagens'), ('oleos', 'Óleos'), ('anti', 'Antitranspirantes'), ('esfol', 'Esfoliantes'), ('bases', 'Bases')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField()),
                ('hora_venda', models.TimeField()),
                ('valor_total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='perfis.Cliente')),
                ('produtos', models.ManyToManyField(through='vendas.ItemVenda', to='vendas.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='itemvenda',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='vendas.Produto'),
        ),
        migrations.AddField(
            model_name='itemvenda',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venda', to='vendas.Venda'),
        ),
    ]
