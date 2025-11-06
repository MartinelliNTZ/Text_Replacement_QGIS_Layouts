# Text_Replacement_QGIS_Layouts

# 🧾 Manual de Uso — Script de Substituição de Textos em Layouts QGIS
**Criado por:** M. Martinelli  
**Data de criação:** 31/10/2025  
**Última alteração:** 31/10/2025

---

## 📘 Objetivo do Script
Este script tem como finalidade **realizar substituições automáticas de textos em rótulos (QgsLayoutItemLabel)** dentro de todos os layouts do projeto QGIS atual.  
Útil para padronizar nomes de fazendas, títulos, legendas ou outros textos de layout sem precisar editar cada layout manualmente.

--- 

## ⚙️ Pré-requisitos
1. Projeto QGIS (.qgz) **salvo** antes de executar o script.  
2. Executar no **Console Python do QGIS** (`Ctrl + Alt + P`).  
3. QGIS com suporte a Python (compatível com QGIS 3.22+ conforme ambiente descrito).  
4. Recomenda-se criar uma cópia de segurança do projeto antes de rodar (backup do .qgz).

---

## 🧭 Visão Geral de Uso
- Abra o QGIS e carregue seu projeto.
- Abra o **Console Python** (`Ctrl + Alt + P`).
- Cole o script (ou carregue como arquivo) e execute.
- Verifique no console as mensagens de "Antes" e "Depois" para confirmar as substituições.
- **Observação importante:** O script **não salva** automaticamente o projeto — as mudanças permanecem na sessão até que você salve manualmente.

---

## 🧩 Configurações principais
Edite o dicionário `substituicoes` no início do script para definir as mudanças desejadas:

```python
substituicoes = {
    'Fazenda São João': 'Fazenda MTL',
    'FAZENDA SÃO JOÃO': 'FAZENDA MTL',
Use apenas a parte do texto que deseja alterar (não é necessário incluir todo o conteúdo do rótulo).

O comportamento é literal e sensível a caixa — 'Texto' ≠ 'texto'.

🔎 O que o script faz (resumo técnico)

Importa as classes necessárias:

from qgis.core import QgsProject, QgsLayoutItemLabel.

Define o dicionário substituicoes com pares old_text: new_text.

Carrega o projeto atual com QgsProject.instance().

Obtém todos os layouts: project.layoutManager().layouts().

Para cada layout:

Percorre layout.items() e filtra itens do tipo QgsLayoutItemLabel.

Para cada rótulo encontrado, verifica se old_text está contido no texto atual.

Se presente, substitui apenas a parte correspondente (str.replace) e chama item.setText(new_text_content).

Exibe no console o Antes: e Depois: para cada alteração.

Não grava o projeto automaticamente — permite revisão antes de salvar.

📝 Saída / Logs

O script imprime no console:

Quantidade de layouts encontrados.

Para cada alteração: nome do layout, texto Antes e Depois.

Mensagem final indicando conclusão:
✅ Processamento concluído (nenhum dado salvo automaticamente).

⚠️ Limitações e cuidados

Afeta apenas QgsLayoutItemLabel (rótulos de layout).

Não altera camadas, atributos, simbologias ou dados geográficos.

Substituições são literais; use expressões exatas se necessário.

Se old_text vier a aparecer em contextos indesejados (assinaturas, notas), também será substituído — revisar logs é obrigatório.

Faça backup do projeto antes de executar em ambientes de produção.

✅ Boas práticas

Teste antes em uma cópia do projeto.

Prefira usar partes específicas do texto para evitar substituições indesejadas.

Revise as mensagens de console e, após validação, salve o projeto manualmente.

Para operações em larga escala, execute em etapas (listas menores de substituições).

🧾 Exemplo mínimo do fluxo

Definir substituicoes.

Executar script no Console Python do QGIS.

Revisar saída no console (Antes / Depois).

Salvar projeto se as alterações estiverem corretas.

🛠️ Sugestões de melhoria (futuras)

Adicionar opção interativa para confirmar substituições antes de aplicá-las.

Implementar correspondência case-insensitive opcional.

Gerar um relatório em arquivo (CSV / TXT) com todas as alterações realizadas.

Suportar expressões regulares para correspondências avançadas.

📚 Referência do Autor

Autor: M. Martinelli
Data: 31/10/2025
Compatibilidade: QGIS 3.22 ou superior
Linguagem: Python 3 (Console Python do QGIS)

🪶 Licença

Este script pode ser usado e adaptado livremente, desde que mantida a autoria original. Recomenda-se documentar alterações com data e autor para controle de versão.



    # 'Texto_antigo': 'Texto_novo'
}
