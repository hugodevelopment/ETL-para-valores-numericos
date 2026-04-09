def ler_arquivo_txt(file_path: str):
    """
    Lê arquivo linha por linha.
    Retorna lista de linhas com número.
    """
    linhas = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for i, linha in enumerate(f, start=1):
            linhas.append((i, linha.strip()))

    return linhas