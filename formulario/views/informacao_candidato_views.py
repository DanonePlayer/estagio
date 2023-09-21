from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator
from django.http import Http404

# from django.http import HttpResponse
from django.shortcuts import redirect, render
from PIL import Image

from formulario.forms.informacao_candidato_forms import InformacaoCandidatoForm
from formulario.models.informacao_candidato_models import InformacaoCandidato
from formulario.models.paginations_models import Pagination


@login_required(login_url="/login")
def informacao_candidato(request):
    if request.method == "GET":
        dados = InformacaoCandidato.objects.filter(user=request.user).first()

        if not dados:
            form = InformacaoCandidatoForm()
            image = ""  # Define um valor padrão vazio para image
            imagem = ""  # Define um valor padrão vazio para imagem
        else:
            form = InformacaoCandidatoForm(instance=dados)
            image = dados.foto
            imagem = str(dados.foto)
            parts = imagem.split("/")
            imagem = "/".join(parts[3:])

        user_pagination = Pagination.objects.filter(user=request.user).exists()
        if user_pagination:
            pagination = Pagination.objects.filter(user=request.user).first()
            for (
                field_name
            ) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
                field_value = getattr(pagination, field_name.attname)
                if field_value == "active":
                    setattr(pagination, field_name.attname, "used")
            pagination.page_1 = "active"
            pagination.save()
        else:
            pagination = Pagination()
            pagination.user = request.user
            pagination.page_1 = "active"
            pagination.save()

        return render(
            request,
            "informacao_candidato.html",
            {"form": form, "pagination": pagination, "imagem": imagem, "image": image},
        )


@login_required(login_url="/login")
def informacao_candidato_enviado(request):
    if request.method == "POST":
        user = request.user
        dados, created = InformacaoCandidato.objects.get_or_create(user=user)
        form = InformacaoCandidatoForm(request.POST, request.FILES, instance=dados)
        pagination = Pagination.objects.filter(user=request.user).first()

        if form.is_valid():
            form.save()
            pagination.page_1 = "used"
            pagination.page_2 = "used"
            pagination.save()
            return redirect("formulario:dados_candidato")
        else:
            return render(
                request,
                "informacao_candidato.html",
                context={
                    "form": form,
                },
            )
    else:
        raise Http404()
