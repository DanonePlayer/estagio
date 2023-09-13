from django.contrib import admin

from formulario.models.dados_candidato_models import DadosCandidato
from formulario.models.email_candidato_models import EmailCandidato
from formulario.models.email_redes_sociais_models import EmailRedesSociais
from formulario.models.paginations_models import Pagination


class DadosCandidatoAdmin(admin.ModelAdmin):
    # Defina quais campos do modelo serão exibidos na listagem
    list_display = [
        "" "user",
        "nome_candidato",
        "data_nasc_candidato",
        "estado_civil",
        "apelido_candidato",
        "nacionalidade",
        "natural",
        "uf_natural",
        "nome_pai",
        "nome_mae",
        "idiomas",
        "num_identidade",
        "orgao_emissor",
        "num_titulo_eleitor",
        "zona_titulo",
        "num_carteira_profissional",
        "serie_carteira_prof",
    ]

    # Defina campos que poderão ser usados para pesquisa
    search_fields = [
        "user",
        "nome_candidato",
        "data_nasc_candidato",
        "estado_civil",
        "apelido_candidato",
        "nacionalidade",
        "natural",
        "uf_natural",
        "nome_pai",
        "nome_mae",
        "idiomas",
        "num_identidade",
        "orgao_emissor",
        "num_titulo_eleitor",
        "zona_titulo",
        "num_carteira_profissional",
        "serie_carteira_prof",
    ]

    # Outras configurações personalizadas, se necessário...


admin.site.register(DadosCandidato, DadosCandidatoAdmin)


# class EmailCandidatoAdmin(admin.ModelAdmin):
#     list_display = [
#         "user",
#         "email_candidato",
#     ]

#     search_fields = [
#         "user",
#         "email_candidato",
#     ]


# admin.site.register(EmailCandidato, EmailCandidatoAdmin)


class EmailRedesSociaisAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "email",
        "email_2",
        "email_3",
        "instagram",
        "facebook",
        "twitter",
        "tiktok",
        "outros",
    ]

    search_fields = [
        "user",
        "email",
        "email_2",
        "email_3",
        "instagram",
        "facebook",
        "twitter",
        "tiktok",
        "outros",
    ]


admin.site.register(EmailRedesSociais, EmailRedesSociaisAdmin)


class PaginationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "page_1",
        "page_2",
        "page_3",
    ]

    search_fields = [
        "user",
        "page_1",
        "page_2",
        "page_3",
    ]


admin.site.register(Pagination, PaginationAdmin)
