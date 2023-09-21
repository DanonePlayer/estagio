# from django.contrib.auth import login
from audioop import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.core.paginator import Paginator
from django.http import Http404, JsonResponse

# from django.http import HttpResponse
from django.shortcuts import redirect, render

from formulario.forms.dados_bancarios_forms import DadosBancariosForm
from formulario.models.dados_bancarios_models import DadosBancarios
from formulario.models.paginations_models import Pagination


@login_required(login_url="/login")
def dados_bancarios(request):
    if request.method == "GET":
        dados = DadosBancarios.objects.filter(user=request.user).first()
        pagination = Pagination.objects.filter(user=request.user).first()

        for (
            field_name
        ) in pagination._meta.fields:  # Itera pelos campos do objeto Pagination
            field_value = getattr(pagination, field_name.attname)
            if field_value == "active":
                setattr(pagination, field_name.attname, "used")
        pagination.page_4 = "active"
        pagination.save()

        if not dados:
            form = DadosBancariosForm()
        else:
            form = DadosBancariosForm(instance=dados)

        return render(
            request,
            "dados_bancarios.html",
            {
                "form": form,
                "pagination": pagination,
            },
        )


@login_required(login_url="/login")
def dados_bancarios_enviado(request):
    if request.method == "POST":
        user = request.user
        dados, created = DadosBancarios.objects.get_or_create(user=user)
        form = DadosBancariosForm(data=request.POST, instance=dados)
        pagination = Pagination.objects.filter(user=request.user).first()

        if form.is_valid():
            form.save()
            form.save()
            pagination.page_5 = "used"
            pagination.save()
            return render(
                request,
                "enviar_formulario.html",
            )
        else:
            return render(
                request,
                "dados_bancarios.html",
                {
                    "form": form,
                    "pagination": pagination,
                },
            )
    else:
        raise Http404()
