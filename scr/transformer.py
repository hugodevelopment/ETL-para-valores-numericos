def limpar_valor(valor_str: str):
    """
    Limpa e converte uma string monetária para float.
    Retorna None se inválido.
    """
    if not valor_str or not valor_str.strip():
        return None

    try:
        valor = (
            valor_str
            .replace('$', '')
            .replace('.', '')
            .replace(',', '.')
            .strip()
        )
        return float(valor)
    except Exception:
        return None