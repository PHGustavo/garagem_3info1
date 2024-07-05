from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class CategoriaSerializer (ModelSerializer):
    model = Categoria
    fields = "__all__"