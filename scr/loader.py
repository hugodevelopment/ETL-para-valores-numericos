import pandas as pd

def salvar_excel(valores, erros, caminho_saida):
    """
    Salva os dados tratados em Excel com duas abas.
    """
    df_valores = pd.DataFrame(valores, columns=['valor'])
    df_erros = pd.DataFrame(erros, columns=['linha', 'valor_original'])

    with pd.ExcelWriter(caminho_saida) as writer:
        df_valores.to_excel(writer, sheet_name='valores_validos', index=False)
        df_erros.to_excel(writer, sheet_name='erros', index=False)