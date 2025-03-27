from Escola.models import estudante,curso, matricula
from Escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer, ListaEstudantesMatriculasSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from Escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = estudante.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    permission_classes = [DjangoModelPermissions]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):

    permission_classes = [DjangoModelPermissions]
    queryset = curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = matricula.objects.all().order_by('id')
    permission_classes = [DjangoModelPermissions]
    throttle_class = [UserRateThrottle,MatriculaAnonRateThrottle]
    serializer_class = MatriculaSerializer
    http_method_names = ['get','post']


class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        queryset = matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaEstudantesMatriculasSerializer

class ListaMatriculasCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        queryset = matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer

