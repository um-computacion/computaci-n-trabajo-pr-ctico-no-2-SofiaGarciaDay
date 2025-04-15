def is_palindrome(text: str) -> bool:
    tex_clear = text.lower()

    reemplazos = {
        'á': 'a', 'é': 'e', 'ü': 'u', 'ñ': 'n', 'í': 'i', 'ó': 'o', 'ú': 'u',
    }

    for acento, sin_acento in reemplazos.items():
        tex_clear = tex_clear.replace(acento, sin_acento)

    resultado = ""
    for caracter in tex_clear:
        if caracter.isalnum():
            resultado += caracter

    return resultado == resultado[::-1]

