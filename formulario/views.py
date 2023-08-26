# from django.contrib.auth import login
from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator
from django.http import Http404

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms.dados_candidato_forms import DadosCandidatoForm
from formulario.forms.email_candidato_forms import EmailCandidatoForm

from .models.dados_candidato_models import DadosCandidato
from .models.email_candidato_models import EmailCandidato


@login_required(login_url="/login")
def formulario(request):
    dados = DadosCandidato.objects.filter(user=request.user).first()

    if not dados:
        form = DadosCandidatoForm()
    else:
        form = DadosCandidatoForm(instance=dados)

    return render(
        request,
        "formulario.html",
        {
            "form": form,
            # "form_action": reverse("formulario:formulario_enviado")
        },
    )


@login_required(login_url="/login")
def formulario_enviado(request):
    if not request.POST:
        raise Http404()

    user = request.user
    dados = DadosCandidato.objects.filter(user=user).first()

    if not dados:
        form = DadosCandidatoForm(data=request.POST)

        if form.is_valid():
            dados = DadosCandidato.objects.create(
                user=user,
                nome_candidato=request.POST.get("nome_candidato"),
                data_nasc_candidato=request.POST.get("data_nasc_candidato"),
                estado_civil=request.POST.get("estado_civil"),
                apelido_candidato=request.POST.get("apelido_candidato"),
                nacionalidade=request.POST.get("nacionalidade"),
                natural=request.POST.get("natural"),
                uf_natural=request.POST.get("uf_natural"),
                nome_pai=request.POST.get("nome_pai"),
                nome_mae=request.POST.get("nome_mae"),
                idiomas=request.POST.get("idiomas"),
                num_identidade=request.POST.get("num_identidade"),
                orgao_emissor=request.POST.get("orgao_emissor"),
                num_titulo_eleitor=request.POST.get("num_titulo_eleitor"),
                zona_titulo=request.POST.get("zona_titulo"),
                num_carteira_profissional=request.POST.get("num_carteira_profissional"),
                serie_carteira_prof=request.POST.get("serie_carteira_prof"),
            )
            dados.save()
    return redirect("formulario:formulario_2")


@login_required(login_url="/login")
def formulario_2(request):
    if request.method == "GET":
        email_data = request.session.get("register_form_data", None)
        if email_data:
            form = EmailCandidatoForm(email_data)
            return render(
                request,
                "formulario_2.html",
                {
                    "form": form,
                },
            )
        else:
            form = EmailCandidatoForm()
            return render(
                request,
                "formulario_2.html",
                {
                    "form": form,
                },
            )


@login_required(login_url="/login")
def formulario_enviado_2(request):
    if not request.POST:
        raise Http404()

    user = request.user
    dados = EmailCandidato.objects.filter(user=user).first()
    POST = request.POST
    request.session["register_form_data"] = POST
    form = EmailCandidatoForm(request.POST, instance=dados)
    if form.is_valid():
        dados = EmailCandidato.objects.create(
            user=user,
            email_candidato=request.POST.get("email_candidato"),
        )
        dados.save()
    return redirect("formulario:formulario_2")
