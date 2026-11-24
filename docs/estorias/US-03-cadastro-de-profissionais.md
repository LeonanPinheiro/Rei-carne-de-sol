# US 03 · Cadastro de Profissionais

**O Rei da Carne de Sol · Sistema de Gestão de Pedidos e Delivery Urbano**
Estória de Usuário · Grupo Os 3 Devs · Análise Orientada a Objetos (UVA)

## Histórico de revisões

| Nº versão | Data | Sumário das mudanças | Responsável pela revisão | Nome do arquivo |
| --- | --- | --- | --- | --- |
| 1 | 24/11/2026 | Criação da estória, cenários e padrões de comportamento | Os 3 Devs | US 03 Cadastro de Profissionais |

## Descrição

Como um **gerente**, eu gostaria de manter o cadastro dos **profissionais** do restaurante (atendentes, cozinheiros, expedidores e entregadores), para que a cozinha e o despacho trabalhem apenas com pessoas ativas e com dados corretos.

## Hierarquia

Tema: Cadastros de apoio à operação de delivery. Detalha o requisito funcional **RF11** (cadastrar entregadores e informar seu status).

## Predecessores e sucessores (no desenvolvimento)

- **Predecessores:** N/A.
- **Sucessores:** US 02 Agrupamento e Roteirização de Pedidos (o despacho só pode escolher entregadores ativos, RF12).

## Referências

- RNE 06; RNE 07; RNE 08; RNE 09.
- MED 03.
- MSG 01; MSG 02; MSG 03; MSG 04; MSG 05; MSG 11; MSG 14; MSG 17.

As definições estão no [catálogo de referências](../catalogo-de-referencias.md).

## Requisitos não funcionais específicos

- **RNF 01 · LGPD:** CPF, telefone e CNH são dados pessoais. Na lista e na planilha exportada, o CPF aparece mascarado (ex.: `529.***.***-25`) e a CNH não é exportada.

## Cenários e critérios de aceitação

| Id. e descrição do cenário | Pré-condição para o cenário | Pós-condição para o cenário | Invariante | Entrada | Resultado esperado | Padrões de comportamento utilizados |
| --- | --- | --- | --- | --- | --- | --- |
| Incluir profissional | | Profissional criado | | NOME, CPF, TELEFONE, E-MAIL, FUNÇÃO, STATUS | Profissional criado com sucesso + MSG 01 | CPO 1.1 |
| Incluir entregador | | Entregador criado | | NOME, CPF, TELEFONE, E-MAIL, FUNÇÃO, CNH, PLACA, STATUS | Entregador criado com sucesso + MSG 01 | CPO 1.2 |
| Incluir profissional já cadastrado | Profissional com o mesmo CPF cadastrado | | | NOME, CPF, TELEFONE, E-MAIL, FUNÇÃO, STATUS | Profissional não cadastrado + MSG 02 | CPO 1.3 |
| Incluir dados de profissional com erros de validação | | Profissional não cadastrado | | NOME, CPF, TELEFONE, E-MAIL, FUNÇÃO, STATUS | Profissional não cadastrado + MSG 03 | CPO 1.4 |
| Incluir entregador sem CNH ou placa | | Entregador não cadastrado | | NOME, CPF, TELEFONE, E-MAIL, FUNÇÃO, STATUS | Entregador não cadastrado + MSG 03 | CPO 1.5 |
| Alterar dados de profissional | Profissional cadastrado | Dado de profissional alterado | CPF | TELEFONE, E-MAIL, FUNÇÃO, CNH, PLACA | Dado de profissional alterado + MSG 04 | CPO 2.1 |
| Dado alterado de profissional com erro de validação | Profissional cadastrado | Dado de profissional não alterado | CPF | TELEFONE, E-MAIL, FUNÇÃO, CNH, PLACA | Dado de profissional não alterado + MSG 03 | CPO 2.2 |
| Consultar profissional | Profissional cadastrado | Informações de profissional | | NOME ou CPF | Sistema apresenta dados de profissional | CPO 3.1 |
| Profissional não localizado | Nenhum profissional com o NOME ou CPF informado | | | NOME ou CPF | Sistema não apresenta dados + MSG 11 | CPO 3.2 |
| Excluir profissional | Profissional cadastrado com status inativo | Profissional excluído | | CPF | MSG 05, MSG 17 + Profissional excluído | CPO 4.1 |
| Cancelar exclusão de profissional | Profissional cadastrado | Profissional não excluído | | CPF | MSG 05 + Profissional não excluído | CPO 4.2 |
| Sistema não permite excluir profissional | Profissional cadastrado com status ativo, ou entregador com lote Em Rota | Profissional não excluído | | CPF | MSG 05, MSG 14 + Profissional não excluído | CPO 4.3 |
| Exportar lista de profissionais para arquivo Excel | Profissional cadastrado | Arquivo Excel gerado | | | Arquivo Excel gerado | CPO 5.1 |
| Ativar selecionados | Profissional cadastrado | Profissional ativo | | CPF | Profissionais selecionados ativos | CPO 6.1 |
| Desativar selecionados | Profissional cadastrado e sem lote Em Rota | Profissional não ativo | | CPF | Profissionais selecionados não ativos | CPO 7.1 |
| Sistema não permite desativar entregador em rota | Entregador com lote Em Rota | Entregador continua ativo | | CPF | MSG 14 + Entregador continua ativo | CPO 7.2 |

## Padrões de comportamento da estória

| Identificação | Descrição |
| --- | --- |
| CPO 1.1 | Usuário informa NOME, CPF, TELEFONE, E-MAIL, seleciona uma FUNÇÃO (Atendente, Cozinheiro, Expedidor ou Gerente) e um STATUS e clica na opção "Salvar". Sistema realiza a validação dos dados. Se os dados estiverem válidos, o sistema exibe a mensagem: "Cadastro realizado com sucesso". |
| CPO 1.2 | Usuário informa NOME, CPF, TELEFONE, E-MAIL e seleciona a FUNÇÃO Entregador. Sistema exibe os campos CNH e PLACA. Usuário informa CNH e PLACA, seleciona um STATUS e clica na opção "Salvar". Sistema realiza a validação dos dados. Se os dados estiverem válidos, o sistema exibe a mensagem: "Cadastro realizado com sucesso". |
| CPO 1.3 | Usuário informa os dados e clica na opção "Salvar". Sistema realiza a validação dos dados. Se os dados estiverem válidos, mas já existir profissional com o mesmo CPF, o sistema exibe a mensagem: "Profissional já cadastrado". |
| CPO 1.4 | Usuário informa os dados e clica na opção "Salvar". Sistema realiza a validação dos dados. Se algum dado estiver com erro de validação, o sistema exibe uma mensagem de tratamento de erro referente ao campo preenchido: "O preenchimento do campo XXX deve seguir o formato YYY". |
| CPO 1.5 | Usuário seleciona a FUNÇÃO Entregador, não informa a CNH ou a PLACA e clica na opção "Salvar". Sistema realiza a validação e exibe a mensagem: "O preenchimento do campo XXX deve seguir o formato YYY". |
| CPO 2.1 | Sistema apresenta uma lista de profissionais. Usuário seleciona um profissional e clica na opção "Editar". Sistema apresenta os dados do profissional selecionado, com o CPF bloqueado para edição. Usuário altera o dado correspondente e confirma a alteração. Sistema realiza a validação e exibe a mensagem: "Dado alterado com sucesso". |
| CPO 2.2 | Sistema apresenta uma lista de profissionais. Usuário seleciona um profissional e clica na opção "Editar". Usuário altera o dado correspondente e confirma a alteração. Sistema realiza a validação e exibe a mensagem de tratamento para o campo: "O preenchimento do campo XXX deve seguir o formato YYY". |
| CPO 3.1 | Usuário informa o NOME ou o CPF do profissional no campo de busca. Sistema apresenta a lista dos profissionais encontrados. Usuário seleciona um profissional e clica na opção "Detalhes". Sistema apresenta as informações do profissional selecionado. |
| CPO 3.2 | Usuário informa o NOME ou o CPF do profissional no campo de busca. Sistema não localiza nenhum profissional e exibe a mensagem: "O profissional não foi localizado". |
| CPO 4.1 | Sistema apresenta uma lista de profissionais. Usuário seleciona um profissional e clica na opção "Excluir". O sistema solicita confirmação e exibe a mensagem: "Deseja realmente excluir esse registro?". Usuário confirma a exclusão. Sistema exibe a mensagem: "Registro excluído com sucesso". |
| CPO 4.2 | Sistema apresenta uma lista de profissionais. Usuário seleciona um profissional e clica na opção "Excluir". O sistema exibe a mensagem: "Deseja realmente excluir esse registro?". Usuário cancela a exclusão. |
| CPO 4.3 | Sistema apresenta uma lista de profissionais. Usuário seleciona um profissional e clica na opção "Excluir". O sistema exibe a mensagem: "Deseja realmente excluir esse registro?". Usuário confirma. Sistema realiza a validação e, como o profissional está ativo ou é entregador com lote Em Rota, exibe a mensagem: "Sistema não permite esta operação". |
| CPO 5.1 | Usuário clica na opção "Gerar Excel". Sistema gera o arquivo Excel com a lista de profissionais, com o CPF mascarado. |
| CPO 6.1 | Sistema apresenta a lista de profissionais. Usuário seleciona um ou mais profissionais e clica na opção "Ativar selecionados". |
| CPO 7.1 | Sistema apresenta a lista de profissionais. Usuário seleciona um ou mais profissionais e clica na opção "Desativar selecionados". |
| CPO 7.2 | Sistema apresenta a lista de profissionais. Usuário seleciona um entregador com lote Em Rota e clica na opção "Desativar selecionados". Sistema exibe a mensagem: "Sistema não permite esta operação" e mantém o entregador ativo. Os demais selecionados são desativados. |

## Cartão, conversa e confirmação (3 Cs)

**Cartão (frente)**

> **Título:** Cadastro de Profissionais · **Prioridade:** 1-Alta · **Pontos:** 5 (sugestão; definir no Planning Poker)
>
> Como gerente, eu quero manter o cadastro dos profissionais do restaurante, para que a cozinha e o despacho trabalhem apenas com pessoas ativas e com dados corretos.

**Cartão (verso): testes de aceitação.** São os 16 cenários acima, automatizados em [`tests/test_aceitacao_us03.py`](../../tests/test_aceitacao_us03.py), um teste por CPO.

**Conversa: pontos combinados com o Product Owner**

- As funções são Atendente, Cozinheiro, Expedidor, Entregador e Gerente.
- O CPF identifica o profissional e não pode ser alterado depois do cadastro.
- Só o entregador precisa de CNH e placa do veículo.
- Profissional ativo não é excluído: primeiro é desativado, para não perder o histórico.
- Entregador com lote Em Rota não pode ser desativado nem excluído até concluir a entrega.

## Checagem INVEST

| Atributo | Atende? | Justificativa |
| --- | --- | --- |
| Independente | Sim | Não depende de outra estória para ser desenvolvida. |
| Negociável | Sim | Campos e funções podem mudar na conversa com o PO sem refazer a estória. |
| Valiosa | Sim | Sem profissionais ativos cadastrados, o despacho da US 02 não funciona. |
| Estimável | Sim | Escopo conhecido: um cadastro com 16 cenários de aceitação. |
| Pequena | Sim | Cabe em uma Sprint. |
| Testável | Sim | Cada cenário tem entrada, resultado e mensagem definidos. |

## Tarefas (quebra da estória para o Sprint Backlog)

1. Modelar a entidade Profissional (MED 03) e as enumerações de função e status.
2. Implementar as validações de CPF, telefone, e-mail, CNH e placa (MSG 03).
3. Implementar inclusão, alteração e consulta (CPO 1.1 a 3.2).
4. Implementar exclusão com confirmação e regras RNE 08 e RNE 09 (CPO 4.1 a 4.3).
5. Implementar exportação para Excel com CPF mascarado (CPO 5.1, RNF 01).
6. Implementar ativação e desativação em lote (CPO 6.1 a 7.2).
7. Escrever os testes de aceitação de cada CPO.
8. Construir a tela de cadastro (lista, formulário e botões).
