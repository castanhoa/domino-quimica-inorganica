TAMANHO_EXTRA_FONTE = 0

MODO_DALTONISMO = False
ALTO_CONTRASTE = False

MODO_NORMAL = "normal"
MODO_DEUTERANOPIA = "deuteranopia"
MODO_PROTANOPIA = "protanopia"
MODO_TRITANOPIA = "tritanopia"

_modo_atual = MODO_NORMAL

def aumentar_fonte():
    global TAMANHO_EXTRA_FONTE
    if TAMANHO_EXTRA_FONTE < 12:
        TAMANHO_EXTRA_FONTE += 4


def diminuir_fonte():
    global TAMANHO_EXTRA_FONTE
    if TAMANHO_EXTRA_FONTE > -4:
        TAMANHO_EXTRA_FONTE -= 4


def tamanho_fonte(base):
    return max(12, base + TAMANHO_EXTRA_FONTE)


def alternar_daltonismo():
    global MODO_DALTONISMO
    MODO_DALTONISMO = not MODO_DALTONISMO


def alternar_alto_contraste():
    global ALTO_CONTRASTE
    ALTO_CONTRASTE = not ALTO_CONTRASTE

def definir_modo_daltonismo(modo):
    global _modo_atual
    _modo_atual = modo


def obter_modo_daltonismo():
    return _modo_atual

def ajustar_cor(r, g, b):

    modo = _modo_atual

    if modo == MODO_NORMAL:
        return (r, g, b)

    # Deuteranopia (vermelho-verde)
    if modo == MODO_DEUTERANOPIA:
        return (
            int(r * 0.8 + g * 0.2),
            int(g * 0.3 + b * 0.7),
            int(b)
        )

    # Protanopia (vermelho reduzido)
    if modo == MODO_PROTANOPIA:
        return (
            int(r * 0.4),
            int(g * 0.6),
            int(b * 0.9)
        )

    # Tritanopia (azul afetado)
    if modo == MODO_TRITANOPIA:
        return (
            int(r),
            int(g * 0.7),
            int(b * 0.4)
        )

    return (r, g, b)
