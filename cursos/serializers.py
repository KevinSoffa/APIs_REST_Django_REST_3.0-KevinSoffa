from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Realationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field -> Gerar links para as avaliações
    """
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True,
        view_name='avaliacao-detail'
    )
    """

    # Primary Key Related Field -> Forma mais performatica
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True,
                                                    read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
