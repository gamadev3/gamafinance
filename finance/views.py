from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from django.shortcuts import redirect
from django.utils import timezone
from finance.models import Conta, Categoria
from finance.forms import ContaForm, CategoriaForm


# Create your views here.
class ListarContas(ListView):
    model = Conta
    template_name = "finance/listar_contas.html"
    context_object_name = "contas"

    def get_queryset(self):
        queryset = super().get_queryset().order_by("data_vencimento").exclude(situacao="P")
        search = self.request.GET.get("search")
        todos = self.request.GET.get("cb-todos")
        abertos = self.request.GET.get("cb-abertos")
        vencidos = self.request.GET.get("cb-vencidos")
        if search:
            queryset = queryset.filter(nome__icontains=search)
        if not todos:
            if abertos:
                queryset = queryset.filter(data_vencimento__gte=timezone.now())
            if vencidos:
                queryset = queryset.filter(data_vencimento__lt=timezone.now())

        return queryset


class CriarConta(CreateView):
    model = Conta
    form_class = ContaForm
    template_name = "finance/add_contas.html"
    success_url = "/"


class DetalheConta(DetailView):
    model = Conta
    template_name = "finance/detalhar_contas.html"


class AtualizarConta(UpdateView):
    model = Conta
    form_class = ContaForm
    template_name = "finance/atualizar_conta.html"
    success_url = "/"

class PagarConta(View):
    def get(self, request, pk):
        conta = Conta.objects.get(pk=pk)
        conta.situacao = "P"
        conta.save()
        return redirect("listar_contas")

class CreateCategory(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "category/create.html"
    success_url = "/"