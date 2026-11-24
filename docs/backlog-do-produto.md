# Product Backlog

Visão do produto: um sistema que concentra os pedidos diretos do O Rei da Carne de Sol (WhatsApp e site), organiza a cozinha e o delivery e fideliza o cliente com pontos e cashback.

As estórias estão agrupadas em épicos. Só a US 03 está detalhada; as demais são candidatas e serão escritas no mesmo modelo quando entrarem em uma Sprint. Itens marcados **[A DEFINIR]** dependem de decisão do grupo ou do restaurante.

## Épicos e estórias

| Épico | Estória | Ator | Situação |
| --- | --- | --- | --- |
| E1 · Pedidos e delivery | US 01 Recepção de Pedidos e Geocodificação de Endereço | Atendente | Especificada no documento do trabalho |
| E1 · Pedidos e delivery | US 02 Agrupamento e Roteirização de Pedidos (GPS) | Expedidor | Especificada no documento do trabalho |
| E2 · Cadastros | [US 03 Cadastro de Profissionais](estorias/US-03-cadastro-de-profissionais.md) | Gerente | Especificada e implementada |
| E2 · Cadastros | US 04 Cadastro automático de cliente pelo WhatsApp | Cliente | Candidata |
| E3 · Atendimento por WhatsApp | US 05 Fazer pedido pelo WhatsApp com o agente de IA | Cliente | Candidata |
| E3 · Atendimento por WhatsApp | US 06 Transferir a conversa para um atendente | Cliente, Atendente | Candidata |
| E4 · Cardápio online | US 07 Manter o cardápio (itens, preços, disponibilidade) | Gerente | Candidata |
| E4 · Cardápio online | US 08 Consultar o cardápio online | Cliente | Candidata |
| E5 · Fidelidade | US 09 Acumular pontos e cashback em pedidos diretos | Cliente | Candidata |
| E5 · Fidelidade | US 10 Resgatar cashback em um pedido | Cliente | Candidata |
| E5 · Fidelidade | US 11 Consultar saldo de pontos e cashback | Cliente | Candidata |
| E5 · Fidelidade | US 12 Configurar as regras de pontos e cashback | Gerente | Candidata |

## Regras de negócio candidatas

| Código | Regra | Situação |
| --- | --- | --- |
| RNE 10 | O telefone do WhatsApp identifica o cliente de forma única. | Proposta |
| RNE 11 | O cliente só é cadastrado depois de aceitar o aviso de uso de dados (LGPD). | Proposta |
| RNE 12 | Pontos e cashback valem apenas para pedidos diretos (WhatsApp e site), não para pedidos do iFood. | [A DEFINIR] |
| RNE 13 | Percentual de cashback, pontos por real gasto, validade e valor mínimo de resgate. | [A DEFINIR] |
| RNE 14 | O agente de IA não confirma pedido nem pagamento sem resumo aprovado pelo cliente, e transfere para um atendente quando não entende o pedido. | Proposta |

## Novos atores

| Ator | Papel |
| --- | --- |
| Agente de IA (WhatsApp) | Ator externo: conversa com o cliente, consulta o cardápio, monta o pedido e o envia para a fila |
| WhatsApp Business Platform | Ator externo: canal oficial da Meta por onde as mensagens entram e saem |
