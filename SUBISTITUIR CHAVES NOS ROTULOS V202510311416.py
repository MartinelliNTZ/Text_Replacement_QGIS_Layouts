from qgis.core import QgsProject, QgsLayoutItemLabel


"""
🧾 Script de Substituição de Textos em Layouts QGIS
Autor: M. Martinelli
Criado em: 31/10/2025 | Atualizado: 31/10/2025

Descrição:
Realiza substituições automáticas de textos em rótulos (QgsLayoutItemLabel)
dentro de todos os layouts do projeto QGIS atual. 
Ideal para padronizar nomes de fazendas, legendas ou títulos sem alterar manualmente cada layout.

Uso:
- ⚠️⚠️⚠️ SEMPRE FAÇA UMA CÓPIA DO PROJETO ANTES DE EXECUTAR ⚠️⚠️⚠️
- Rode o script no Console Python do QGIS (Ctrl + Alt + P).
- Verifique no console as mensagens de "Antes" e "Depois" para confirmar as substituições.
- As alterações só são salvas no projeto se você salvar manualmente após a execução.

Configurações:
substituicoes = {
    'Texto_antigo': 'Texto_novo',
    'Outro_antigo': 'Outro_novo'
}
→ Define os pares de texto a serem substituídos nos rótulos.

Saída:
- Nenhum arquivo é criado.
- Exibe no console todos os rótulos alterados e seus respectivos layouts.

Observações:
- Afeta apenas rótulos de layout (QgsLayoutItemLabel).
- Não altera camadas, simbologias, mapas ou dados.
- Não grava automaticamente no arquivo .qgz — a alteração só é efetiva se o projeto for salvo depois.
"""


# Dicionário de substituições
# Aqui o ideal é usar APENAS a parte que quer mudar, não o texto inteiro do rótulo.
substituicoes = {
    'Fazenda São João do Morro Alto': 'Fazenda MTL'
    , 'FAZENDA SÃO JOÃO DO MORRO ALTO': 'FAZENDA MTL',
    # 'Média': 'Media'
}


# Função para atualizar o texto do rótulo
def update_label_text(layout, old_text, new_text):
    for item in layout.items():
        if isinstance(item, QgsLayoutItemLabel):
            label_text = item.text()
            # Substitui apenas se o texto exato aparecer no conteúdo
            if old_text in label_text:
                new_text_content = label_text.replace(old_text, new_text)
                # Atualiza o texto SEM ajustar tamanho ou posição
                print(f"Atualizando rótulo no layout '{layout.name()}':")
                print(f" - Antes: {label_text}")
                print(f" - Depois: {new_text_content}\n")
                item.setText(new_text_content)

# Carregar o projeto atual
project = QgsProject.instance()
layouts = project.layoutManager().layouts()

# Processar cada layout
print(f"Encontrados {len(layouts)} layouts.\n")
for layout in layouts:
    print(f"Processando layout: {layout.name()}")
    for old_text, new_text in substituicoes.items():
        update_label_text(layout, old_text, new_text)

print("✅ Processamento concluído (nenhum dado salvo automaticamente).")

"""
🧾 Docstring detalhado — Funcionamento passo a passo
Script: Substituição de Textos em Rótulos de Layout QGIS
Autor: M. Martinelli
Data: 31/10/2025

Objetivo:
Explicar, passo a passo, o que o script faz internamente desde a carga do projeto
até a execução das substituições em rótulos (QgsLayoutItemLabel).

Passo a passo:

1) Importações
   - O script importa as classes necessárias do QGIS:
     from qgis.core import QgsProject, QgsLayoutItemLabel
   - Essas importações permitem acessar o projeto atual e identificar objetos
     de tipo rótulo dentro dos layouts.

2) Definição do dicionário de substituições
   - `substituicoes` é um dicionário Python onde:
       chave = texto a ser procurado (old_text)
       valor = texto que irá substituir a chave (new_text)
   - Exemplo:
       substituicoes = {
           'Fazenda A': 'Fazenda B',
           'TEXTO ANTIGO': 'TEXTO NOVO'
       }
   - O ideal é incluir apenas a parte do texto que deseja modificar (não o rótulo inteiro).

3) Inicialização do projeto e coleta dos layouts
   - `project = QgsProject.instance()` obtém a instância do projeto aberto no QGIS.
   - `layouts = project.layoutManager().layouts()` retorna uma lista de objetos
     `QgsLayout` correspondentes a todos os layouts presentes no projeto.

4) Iteração sobre cada layout
   - O script percorre cada layout da lista.
   - Para cada layout, ele imprime no console que está processando aquele layout
     (útil para rastrear progresso).

5) Iteração sobre cada par de substituição
   - Para cada par `old_text, new_text` em `substituicoes`, o script chama a função
     `update_label_text(layout, old_text, new_text)` para inspecionar e alterar rótulos.

6) Identificação de rótulos dentro do layout
   - Dentro da função `update_label_text`, o script percorre `layout.items()` que
     retorna todos os itens (textos, mapas, imagens, legendas, etc.) daquele layout.
   - Usa `isinstance(item, QgsLayoutItemLabel)` para filtrar e atuar apenas
     sobre itens do tipo rótulo.

7) Verificação e substituição do texto do rótulo
   - Para cada rótulo identificado:
       a) Recupera o texto atual via `label_text = item.text()`.
       b) Verifica se `old_text` está contido em `label_text` com `if old_text in label_text:`.
       c) Se presente, cria o novo conteúdo `new_text_content = label_text.replace(old_text, new_text)`.
       d) Compara e, se houver alteração, aplica `item.setText(new_text_content)` para
          atualizar o texto do rótulo no layout.
       e) Imprime no console o antes/depois para auditoria.

8) Comportamento quanto ao salvamento
   - O script **não salva** automaticamente o projeto no disco.
   - As alterações ficam na sessão do QGIS até que o usuário salve manualmente o projeto.
   - Isso permite revisar as mudanças antes de torná-las permanentes.

9) Limitações e escopo
   - O script **aplica-se somente a** `QgsLayoutItemLabel` (rótulos de layout).
   - **Não** altera camadas, atributos, geometria, estilos, legendas que não sejam rótulos,
     ou outros elementos do projeto.
   - A substituição é textual e literal — sensível à caixa de caracteres conforme definido nas chaves.
   - Se uma string `old_text` aparece em contextos não desejados (ex.: dentro de uma nota,
     assinatura ou legenda), também será substituída — por isso a necessidade de revisão.

10) Recomendações de uso seguro
    - Fazer backup/cópia do arquivo do projeto (.qgz / pasta do projeto) antes de rodar.
    - Rodar inicialmente em modo de teste (ou comentar a linha `item.setText(...)` e apenas listar
      o que seria alterado).
    - Conferir o console do Python para ver as linhas "Antes" e "Depois" e validar as mudanças.
    - Após validação, salvar o projeto manualmente no QGIS.

Resumo:
- Fluxo: carregar projeto → coletar layouts → para cada layout inspecionar itens → filtrar rótulos → verificar ocorrência do texto antigo → substituir pelo texto novo → exibir logs → término (sem salvar automático).
- Segurança: mudanças restritas a rótulos e reversíveis até o salvamento do projeto.
"""

