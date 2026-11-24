# US 02 · Gerenciar Pedidos e Atendimento Humano no Painel

**O Rei da Carne de Sol · Sistema Chatbot WhatsApp**
Estória de Profissional · Grupo Os 4 Devs · Análise Orientada a Objetos (UVA)

## Histórico de revisões

| Nº versão | Data | Sumário das mudanças | Responsável pela revisão | Nome do arquivo |
| --- | --- | --- | --- | --- |
| 1 | 24/11/2026 | Criação da estória a partir da Proposta de Projeto de 14/11/2026 | Os 4 Devs | US 02 Gerenciar Pedidos e Atendimento Humano |

## Equipe · Os 4 Devs

| Integrante | Matrícula |
| --- | --- |
| Angel Moreira Soares Guimarães | 1250103118 |
| Leonan Pinheiro Costa | 1250103989 |
| Maria Luiza Benevides Cunha | 1250112092 |
| Matheus Frazão Aguiar | [A CONFIRMAR] |

## Descrição

Como um **gestor do restaurante**, eu gostaria que os pedidos recebidos pelo WhatsApp caíssem diretamente em um **painel digital**, para que minha equipe possa focar no preparo, e de receber **alertas imediatos** quando um cliente precisar de atendimento humano, para que eu possa intervir e não perder a venda.

## Hierarquia

Detalha os casos de uso **UC04** (Gerenciar Pedidos) e **UC05** (Transbordo Humano), pelo lado do restaurante. O lado do cliente está na US 01.

## Predecessores e sucessores (no desenvolvimento)

- **Predecessores:** US 01 Fazer Pedido pelo WhatsApp (gera os pedidos e os pedidos de transbordo); US 03 Cadastro de Profissionais (gestores, atendentes e entregadores ativos).
- **Sucessores:** US 04 Cashback (o cashback é creditado quando o pedido chega ao status Entregue).

## Referências

- RF03; RF05; RF06.
- RN03; RN04; RN09; RN10; RN11.
- RNF04.
- MED 02; MED 04.
- MSG 03; MSG 14; MSG 30; MSG 31; MSG 32; MSG 33; MSG 34; MSG 35; MSG 36; MSG 37.

As definições estão no [catálogo de referências](../catalogo-de-referencias.md).

## Requisitos não funcionais específicos

- **RNF04:** o painel deve funcionar em computador e tablet, com os pedidos separados em colunas por status e cores que também tragam o nome do status escrito.
- **RF06:** um novo pedido ou um pedido de atendimento humano aparece no painel em até 2 segundos, sem recarregar a página.

## Cenários e critérios de aceitação

| Id. e descrição do cenário | Pré-condição para o cenário | Pós-condição para o cenário | Invariante | Entrada | Resultado esperado | Padrões de comportamento utilizados |
| --- | --- | --- | --- | --- | --- | --- |
| Receber novo pedido no painel | Cliente concluiu um pedido pelo WhatsApp | Pedido exibido com status Recebido | | | Pedido no painel + MSG 30 | CPO 1.1 |
| Consultar detalhes do pedido | Pedido no painel | Informações do pedido | | NÚMERO DO PEDIDO | Sistema apresenta itens, total, taxa de entrega e dados do cliente | CPO 1.2 |
| Avançar status do pedido | Pedido com status Recebido, Em preparo ou Pronto | Status avançado uma etapa; cliente avisado no WhatsApp | NÚMERO, ITENS | NOVO STATUS | Status atualizado + MSG 32 | CPO 2.1 |
| Pular etapa de status | Pedido com status Recebido ou Em preparo | Status não alterado | NÚMERO, ITENS | NOVO STATUS | MSG 14 + status não alterado | CPO 2.2 |
| Liberar pedido para entrega | Pedido com status Pronto e entregador ativo cadastrado | Status Saiu para Entrega; rastreio liberado | NÚMERO, ITENS | ENTREGADOR | MSG 32 + MSG 33 ao cliente + MSG 34 ao entregador | CPO 3.1 |
| Liberar pedido sem entregador | Pedido com status Pronto | Status não alterado | NÚMERO, ITENS | ENTREGADOR | MSG 03 + status não alterado | CPO 3.2 |
| Confirmar entrega | Pedido com status Saiu para Entrega | Status Entregue; entregador liberado | NÚMERO, ITENS | | Status atualizado + MSG 32 | CPO 3.3 |
| Receber pedido de atendimento humano | Cliente escolheu "Falar com pessoa" no WhatsApp | Bot congelado para o cliente; atendimento Aguardando | | | Alerta no painel + MSG 31 | CPO 4.1 |
| Transbordo por mensagens não compreendidas | Cliente enviou 3 mensagens seguidas não compreendidas | Bot congelado para o cliente; atendimento Aguardando | | | Alerta no painel + MSG 31 | CPO 4.2 |
| Assumir atendimento humano | Atendimento com status Aguardando | Atendimento Em atendimento, com responsável | CLIENTE | | Conversa aberta no painel; bot continua congelado | CPO 4.3 |
| Encerrar atendimento humano | Atendimento com status Em atendimento | Atendimento Encerrado; bot reativado | CLIENTE | | MSG 37 | CPO 4.4 |
| Cancelar pedido | Pedido com status Recebido, Em preparo ou Pronto | Pedido Cancelado; cliente avisado | NÚMERO, ITENS | MOTIVO | MSG 35, MSG 36 + pedido cancelado | CPO 5.1 |
| Desistir do cancelamento | Pedido com status Recebido, Em preparo ou Pronto | Pedido não cancelado | NÚMERO, ITENS | | MSG 35 + pedido não cancelado | CPO 5.2 |
| Sistema não permite cancelar | Pedido com status Saiu para Entrega ou Entregue | Pedido não cancelado | NÚMERO, ITENS | MOTIVO | MSG 35, MSG 14 + pedido não cancelado | CPO 5.3 |

## Padrões de comportamento da estória

| Identificação | Descrição |
| --- | --- |
| CPO 1.1 | Cliente conclui um pedido pelo WhatsApp. Sistema registra o pedido com status Recebido e o exibe na coluna "Recebidos" do painel, sem recarregar a página, com alerta visual e sonoro: "Novo pedido recebido". |
| CPO 1.2 | Sistema apresenta os pedidos separados por status. Usuário clica em um pedido. Sistema apresenta número, itens, total, taxa de entrega, nome e número de WhatsApp do cliente e horário do pedido. |
| CPO 2.1 | Usuário seleciona um pedido e clica na opção do próximo status ("Iniciar preparo" ou "Marcar como pronto"). Sistema valida a ordem dos status, atualiza o pedido, envia a atualização ao cliente pelo WhatsApp e exibe a mensagem: "Status do pedido atualizado". |
| CPO 2.2 | Usuário tenta mover um pedido para um status que pula etapas (por exemplo, de Recebido para Pronto). Sistema valida a ordem dos status e exibe a mensagem: "Sistema não permite esta operação". |
| CPO 3.1 | Usuário seleciona um pedido Pronto, escolhe um ENTREGADOR ativo e clica na opção "Saiu para entrega". Sistema atualiza o status e exibe "Status do pedido atualizado". O cliente recebe no WhatsApp: "Seu pedido saiu para entrega, visse! Já já o entregador manda a localização dele aqui no chat." O entregador recebe: "Envie sua localização em tempo real para o cliente pelo WhatsApp." |
| CPO 3.2 | Usuário seleciona um pedido Pronto e clica na opção "Saiu para entrega" sem escolher um ENTREGADOR. Sistema exibe a mensagem: "O preenchimento do campo ENTREGADOR deve seguir o formato entregador ativo cadastrado". |
| CPO 3.3 | Usuário seleciona um pedido Saiu para Entrega e clica na opção "Confirmar entrega". Sistema atualiza o status para Entregue, libera o entregador e exibe a mensagem: "Status do pedido atualizado". |
| CPO 4.1 | Cliente escolhe "Falar com pessoa" no WhatsApp. Sistema congela o bot para esse cliente, cria um atendimento com status Aguardando e exibe no painel, com alerta visual e sonoro: "Cliente aguardando atendimento humano". |
| CPO 4.2 | Cliente envia 3 mensagens seguidas que o bot não compreende. Sistema congela o bot para esse cliente, cria um atendimento com status Aguardando e exibe no painel: "Cliente aguardando atendimento humano". |
| CPO 4.3 | Usuário clica na opção "Assumir conversa" de um atendimento Aguardando. Sistema registra o usuário como responsável, muda o status para Em atendimento e abre a conversa no painel. O bot continua congelado. |
| CPO 4.4 | Usuário clica na opção "Encerrar atendimento". Sistema muda o status para Encerrado, reativa o bot para o cliente e exibe a mensagem: "Atendimento encerrado. O bot voltou a responder este cliente". |
| CPO 5.1 | Usuário seleciona um pedido e clica na opção "Cancelar". Sistema exibe a mensagem: "Deseja realmente cancelar este pedido?". Usuário informa o MOTIVO e confirma. Sistema cancela o pedido, avisa o cliente pelo WhatsApp e exibe: "Pedido cancelado. O cliente foi avisado pelo WhatsApp". |
| CPO 5.2 | Usuário seleciona um pedido e clica na opção "Cancelar". Sistema exibe a mensagem: "Deseja realmente cancelar este pedido?". Usuário desiste do cancelamento. |
| CPO 5.3 | Usuário seleciona um pedido Saiu para Entrega ou Entregue e clica na opção "Cancelar". Sistema exibe a mensagem: "Deseja realmente cancelar este pedido?". Usuário confirma. Sistema valida o status e exibe a mensagem: "Sistema não permite esta operação". |

## Cartão, conversa e confirmação (3 Cs)

**Cartão (frente)**

> **Título:** Painel de pedidos e atendimento humano · **Prioridade:** 1-Alta · **Pontos:** 8 (sugestão; definir no Planning Poker)
>
> Como gestor do restaurante, eu quero que os pedidos do WhatsApp caiam direto em um painel digital e receber alertas quando um cliente precisar de atendimento humano, para que a equipe foque no preparo e nenhuma venda se perca.

**Cartão (verso): testes de aceitação.** São os 14 cenários acima.

**Conversa: pontos combinados com o Product Owner**

- Os pedidos aparecem em colunas por status: Recebido, Em preparo, Pronto, Saiu para Entrega, Entregue.
- O status só avança uma etapa por vez, e só o gestor libera a saída para entrega (RN03).
- O pedido de atendimento humano congela o bot até o gestor encerrar o atendimento (RN04).
- O pedido só pode ser cancelado antes de sair para entrega.
- O pagamento é feito na entrega, então o painel não registra dados de cartão (RN02, RNF03).

## Checagem INVEST

| Atributo | Atende? | Justificativa |
| --- | --- | --- |
| Independente | Parcial | Precisa dos pedidos da US 01 para ser testada de ponta a ponta, mas o painel pode ser desenvolvido com pedidos simulados. |
| Negociável | Sim | Colunas, alertas e nomes de botões podem mudar com o PO sem refazer a estória. |
| Valiosa | Sim | Resolve o gargalo apontado na entrevista: controlar o delivery e o salão ao mesmo tempo. |
| Estimável | Sim | Escopo definido: 14 cenários sobre dois casos de uso. |
| Pequena | Parcial | Cabe em uma Sprint se o chat do transbordo usar o próprio WhatsApp do restaurante; um chat dentro do painel pode virar outra estória. |
| Testável | Sim | Cada cenário tem pré-condição, resultado e mensagem definidos. |

## Tarefas (quebra da estória para o Sprint Backlog)

1. Modelar Pedido (MED 02) e Atendimento humano (MED 04), com a máquina de status (RN10).
2. Criar o endpoint que recebe os pedidos e os pedidos de transbordo vindos do fluxo do n8n/Typebot.
3. Enviar novos pedidos e alertas ao painel por websocket (RF06).
4. Construir o painel em React: colunas por status, detalhes do pedido e alertas (RNF04).
5. Implementar avanço de status e a liberação para entrega com escolha do entregador (RN03, RF03).
6. Integrar as mensagens de status ao cliente e ao entregador pela Cloud API do WhatsApp (MSG 32 a 34).
7. Implementar o congelamento e a reativação do bot no transbordo (RN04, RN11).
8. Implementar o cancelamento com motivo (CPO 5.1 a 5.3).
9. Escrever os testes de aceitação de cada CPO.
