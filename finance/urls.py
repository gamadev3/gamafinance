from django.urls import path
from finance.views import ListarContas, CriarConta, DetalheConta, AtualizarConta, CreateCategory


urlpatterns = [
    path("", ListarContas.as_view(), name="listar_contas"),
    path("cadastrar/", CriarConta.as_view(), name="cadastrar_contas"),
    path("detalhar/<int:pk>/", DetalheConta.as_view(), name="detalhar_contas"),
    path(
        "detalhar/<int:pk>/update/", AtualizarConta.as_view(), name="atualizar_contas"
    ),
    path("category/cadastrar", CreateCategory.as_view(), name="create_category")
]
