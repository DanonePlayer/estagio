# flake8: noqa
from django.contrib.auth.models import User
from django.db import models

OPCOES_CARGO = [
    ("Delegado", "Delegado"),
    ("Investigador", "Investigador"),
    ("Escrivão", "Escrivão"),
    ("Perito", "Perito"),
    ("Criminal", "Criminal"),
    ("Papiloscopista", "Papiloscopista"),
    ("Médico Legista", "Médico Legista"),
    ("Auxiliar de Necropsia", "Auxiliar de Necropsia"),
    ("Tercerizado", "Tercerizado"),
]


class InformacaoCandidato(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuário"
    )
    cargo = models.CharField(
        max_length=100,
        choices=OPCOES_CARGO,
        null=True,
        verbose_name="Cargo",
    )
    portador_necess_especial = models.BooleanField(
        default=False, verbose_name="Portador de Necessidade Especial - P.N.E"
    )
    num_cid = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="N° C.I.D",
    )
    foto = models.ImageField(
        upload_to="formulario/images/",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Informações do candidato"
        verbose_name_plural = "Informações dos candidatos"
