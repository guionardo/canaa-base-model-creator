def camel_to_snake(text: str):
    letras = []
    abriu_ = False
    for letra in text:
        if letra.isupper() and len(letras) > 0 and not abriu_:
            letras.append('_'+letra.lower())
            abriu_ = True
        else:
            letras.append(letra.lower())
            abriu_ = False

    return "".join(letras)


def snake_to_camel(text: str):
    letras = []
    pegou_under = True
    for letra in text:
        if not letra.isalpha():
            pegou_under = True
        else:
            if pegou_under:
                letra = letra.upper()
                pegou_under = False
            letras.append(letra)

    return "".join(letras)


def get_words(line: str, nwords: int = 0):
    words = [word.replace('"', '').strip() for word in line.split(';')]
    if nwords > 0:
        while len(words) < nwords:
            words.append(None)
    else:
        nwords = len(words)

    return words[:nwords]
