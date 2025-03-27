from django.db import models
from django.core.validators import MinLengthValidator

class estudante(models.Model):

    nome = models.CharField(max_length=100)
    email = models.CharField(blank=False ,max_length=30)
    cpf = models.CharField(max_length=11,unique=True)
    nascimento = models.DateField()
    celular = models.CharField(max_length=14)



    def __str__(self):
        return self.nome




class curso(models.Model):

    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado')
    )



    codigo = models.CharField(max_length=10,unique=True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(blank=False, max_length=100)
    nivel =models.CharField(max_length=1 , blank=False, null=False, choices=NIVEL)

    def __str__(self):
        return self.codigo
    

class matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    
    
    estudante = models.ForeignKey(estudante, on_delete= models.CASCADE)
    curso = models.ForeignKey(curso, on_delete= models.CASCADE)
    periodo =models.CharField(max_length=1 , blank=False, null=False, choices=PERIODO, default= 'M')


