from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    dados_adicionais_views,
    dados_bancarios_views,
    dados_candidato_views,
    email_redes_sociais_views,
    informacao_candidato_views,
)

app_name = "formulario"

urlpatterns = [
    path(
        "formulario_dados_adicionais/",
        dados_adicionais_views.formulario_dados_adicionais,
        name="formulario_dados_adicionais",
    ),
    path(
        "formulario_dados_adicionais/enviado/",
        dados_adicionais_views.formulario_dados_adicionais_enviado,
        name="formulario_dados_adicionais_enviado",
    ),
    path("get_cidades/", dados_adicionais_views.get_cidades, name="get_cidades"),
    path(
        "formulario_email_redes_sociais/",
        email_redes_sociais_views.formulario_email_redes_sociais,
        name="formulario_email_redes_sociais",
    ),
    path(
        "formulario_email_redes_sociais/enviado/",
        email_redes_sociais_views.formulario_email_redes_sociais_enviado,
        name="formulario_email_redes_sociais_enviado",
    ),
    path(
        "formulario_dados_bancarios/",
        dados_bancarios_views.dados_bancarios,
        name="formulario_dados_bancarios",
    ),
    path(
        "formulario_dados_bancarios/enviado/",
        dados_bancarios_views.dados_bancarios_enviado,
        name="formulario_dados_bancarios_enviado",
    ),
    path(
        "formulario_informacao_candidato/",
        informacao_candidato_views.informacao_candidato,
        name="formulario_informacao_candidato",
    ),
    path(
        "formulario_informacao_candidato/enviado/",
        informacao_candidato_views.informacao_candidato_enviado,
        name="formulario_informacao_candidato_enviado",
    ),
    path("lista/", dados_candidato_views.lista, name="inlineform_lista"),
    path(
        "formulario_dados_candidato/",
        dados_candidato_views.dados_candidato,
        name="formulario_dados_candidato_inserir",
    ),
    path(
        "formulario_dados_candidato/<int:candidato_id>/",
        dados_candidato_views.dados_candidato_editar,
        name="formulario_dados_candidato_editar",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
