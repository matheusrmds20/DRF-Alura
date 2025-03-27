from rest_framework import serializers
from Escola.models import estudante, curso, matricula
from Escola.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudante
        fields = '__all__'

    def validate(self,data):
        
        if cpf_invalido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Cpf tem que ter 11 numero mula'})
        
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({'nome':'Nome apenas com letras Animal!!'})
    
        if celular_invalido(data['celular']):
            raise serializers.ValidationError({'celular':'Numero de celular tem que ter 13 caracteres numericos'})
        
        return data 

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = matricula
        fields = '__all__'


class ListaEstudantesMatriculasSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField() 
    
    class Meta:
        model = matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self,obj):
        return obj.get_periodo_display()
    

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')

    class Meta:
        model = matricula
        fields = ['estudante_nome']




#VERSIONAMENTO   

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = estudante
        fields = ['id','nome','email','celular']
        


