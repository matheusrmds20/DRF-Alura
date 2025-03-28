import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from Escola.models import estudante

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        nascimento = fake.date_of_birth(minimum_age=18, maximum_age=30)  # Gera uma data de nascimento aleatória entre 18 e 30 anos
        celular = "{} 9{}-{}".format(random.randrange(10, 89), random.randrange(4000, 9999), random.randrange(4000, 9999))
        p = estudante(nome=nome, email=email, cpf=cpf, nascimento=nascimento, celular=celular)
        p.save()

criando_pessoas(50)