# ETL-para-valores-numericos

Recentemente resolvi um problema simples, porém que travava toda a análise.

No Excel, a coluna de valores estava sendo lida como texto por causa de:
símbolos ($), células vazias e formatação inconsistente.

Resultado: não dava pra somar no Power Pivot e criar tabelas dinâmicas que me possibilitavam calcular soma total por região ou por produto por exemplo.

Para resolver isso criei um pequeno ETL em Python para:

- 1º limpar os dados da coluna;
  
- 2º padronizar os valores;
  
- 3º garantir tipo numérico;
  
- 4º Criar de uma maneira estruturada um pipeline

Depois disso:

- ✔ Consegui usar o Power Pivot corretamente e criar as tabelas necessárias;
- ✔ Criei relacionamentos no modelo para fazer filtros personalidados;
- ✔ Melhorei a análise sem precisar retrabalho manual
