from django.core.exceptions import ValidationError

def leao_nao(value):
    if value == 'leao':
        raise ValidationError(
            f'O valor "{value}" é inválido. A palavra "leao" não é permitida.'
        )
    return value


