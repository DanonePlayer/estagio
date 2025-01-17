from django.contrib import admin

from formulario.models import (
    DadosAdicionais,
    DadosBancarios,
    EmailRedesSociais,
    InformacaoCandidato,
    Pagination,
)


class DadosAdicionaisAdmin(admin.ModelAdmin):
    dados_adicionais = [
        "user",
        "nome_candidato",
        "data_nasc_candidato",
        "estado_civil",
        "apelido_candidato",
        "nacionalidade",
        "uf_natural",
        "natural",
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

    list_display = dados_adicionais

    # Defina campos que poderão ser usados para pesquisa
    search_fields = dados_adicionais[1:]

    # Outras configurações personalizadas, se necessário...

    raw_id_fields = ["user"]


admin.site.register(DadosAdicionais, DadosAdicionaisAdmin)


class EmailRedesSociaisAdmin(admin.ModelAdmin):
    email_redes_sociais = [
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

    list_display = email_redes_sociais

    search_fields = email_redes_sociais[1:]


admin.site.register(EmailRedesSociais, EmailRedesSociaisAdmin)


class DadosBancariosAdmin(admin.ModelAdmin):
    dados_bancarios = [
        "user",
        "banco",
        "num_conta",
        "num_agencia",
        "endereco_banco",
        "banco_2",
        "num_conta_2",
        "num_agencia_2",
        "endereco_banco_2",
        "banco_3",
        "num_conta_3",
        "num_agencia_3",
        "endereco_banco_3",
    ]

    list_display = dados_bancarios

    search_fields = dados_bancarios[1:]


admin.site.register(DadosBancarios, DadosBancariosAdmin)


class InformacaoCandidatoAdmin(admin.ModelAdmin):
    informacao_candidato = [
        "user",
        "cargo",
        "portador_necess_especial",
        "num_cid",
        "foto",
    ]
    list_display = informacao_candidato

    search_fields = informacao_candidato[1:]

    list_filter = ["cargo", "portador_necess_especial"]

    raw_id_fields = ["user"]


admin.site.register(InformacaoCandidato, InformacaoCandidatoAdmin)


class PaginationAdmin(admin.ModelAdmin):
    pagination = [
        "user",
        "page_1",
        "page_2",
        "page_3",
        "page_4",
        "page_5",
        "page_6",
        "page_7",
    ]

    list_display = pagination

    search_fields = pagination[1:]

    # list_display_links = pagination
    # search_fields = ("nome", "descricao")


admin.site.register(Pagination, PaginationAdmin)
