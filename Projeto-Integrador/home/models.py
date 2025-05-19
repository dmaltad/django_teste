from django.db import models
from datetime import date

    
class CA(models.Model):
    numero = models.CharField(verbose_name='Certificado de Aprovação', max_length=7, blank=False, null=False, unique=True)
    validade = models.DateField(verbose_name='Validade do CA', null=False)
    descricao = models.CharField(verbose_name='Descrição do CA', max_length=200)

    class Meta:
        verbose_name='CA'
        verbose_name_plural='CAs'
        db_table='Certificado de Aprovação'
        ordering = ['numero']

    def __str__(self):
        return self.numero  
     
class EPI(models.Model):
    nome = models.CharField(verbose_name='Nome do EPI', max_length=50, blank=False, null=False)
    ca = models.ForeignKey(CA, on_delete=models.PROTECT)
    descricao = models.CharField(verbose_name='Descrição do EPI', max_length=200)
    vida_util = models.CharField(verbose_name='Vida útil do EPI', max_length=50, blank=False, null=False )

    class Meta:
        verbose_name='EPI'
        verbose_name_plural='EPIs'
        db_table='EPI'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    epi = models.ForeignKey(EPI, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade em Estoque', default=0)
    entrada = models.DateField(verbose_name='Data de Entrada', null=False)

    class Meta:
        verbose_name='Estoque'
        verbose_name_plural='Estoques'
        db_table='Estoque'
        ordering = ['entrada']

class Colaborador(models.Model):
    nome = models.CharField(verbose_name='Nome do EPI', max_length=50, blank=False, null=False)
    cpf = models.CharField(verbose_name='CPF', max_length=14, blank=False, null=False, unique=True)
    matricula = models.CharField(verbose_name='Matricula', max_length=5, blank=False, null=False, unique=True)
    cargo = models.CharField(verbose_name='Cargo', max_length=50, blank=False, null=False)
    setor = models.CharField(verbose_name='Setor', max_length=50, blank=False, null=False)
    data_admissao = models.DateField(verbose_name='Data de Admissão', null=False)

    class Meta:
        verbose_name='Colaborador'
        verbose_name_plural='Colaboradores'
        db_table='Colaborador'
        ordering = ['matricula']    

class Entrega(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    epi = models.ForeignKey(EPI, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade Entregue', default=0)
    data_entrega = models.DateField(verbose_name='Data de Entrega', null=False)

    class Meta:
        verbose_name='Entrega'
        verbose_name_plural='Entregas'
        db_table='Entrega'
        ordering = ['data_entrega']