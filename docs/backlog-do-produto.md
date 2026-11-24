# Product Backlog

**Visão do produto:** um chatbot de WhatsApp com menus em árvore de decisão, sem IA generativa, que atende o cliente do O Rei da Carne de Sol do cardápio à entrega, com rastreio pelo GPS nativo do WhatsApp e cashback. Do lado do restaurante, um painel web organiza os pedidos e os pedidos de atendimento humano. O pagamento é sempre feito na entrega.

Fonte: [Proposta de Projeto](proposta/Proposta_de_Projeto_-_Rei_da_Carne_de_Sol.pdf) de 14/11/2026. O andamento das tarefas fica no [quadro do Trello](https://trello.com/b/FnCgakIm/rei-da-carne-do-sol-delivery). Requisitos, regras e mensagens estão no [catálogo de referências](catalogo-de-referencias.md).

## Estórias

| Estória | Tipo | Título | Casos de uso e requisitos | Prioridade | Situação |
| --- | --- | --- | --- | --- | --- |
| US 01 | História do Usuário | Fazer pedido pelo WhatsApp (cardápio, pedido, rastreio e falar com pessoa) | UC01, UC02, UC03, UC05 · RF01, RF02, RF03, RF05 | 1-Alta | Em elaboração pelo grupo |
| [US 02](estorias/US-02-gerenciar-pedidos-e-atendimento-humano.md) | História do Profissional | Gerenciar pedidos e atendimento humano no painel | UC04, UC05 · RF03, RF05, RF06 | 1-Alta | Especificada |
| [US 03](estorias/US-03-cadastro-de-profissionais.md) | Estória de apoio | Cadastro de profissionais | UC03, UC04 | 2-Média | Especificada e implementada |
| US 04 | Estória de usuário | Acumular e resgatar cashback | RF04 · RN05 | 2-Média | Candidata |
| US 05 | Estória de usuário | Identificar o cliente pelo número do WhatsApp (novo ou recorrente) | MED 01 | 2-Média | Candidata |

## Decisões em aberto

| Decisão | Por que importa |
| --- | --- |
| Quem entrega os pedidos feitos pelo WhatsApp? | Na entrevista, o restaurante disse que usa motoboy do aplicativo, escolhido automaticamente pelo app. O rastreio (UC03, RF03) depende de um entregador que compartilhe a localização pelo WhatsApp. |
| Valor mínimo para resgate e percentual do cashback | A RN05 exige um valor mínimo, mas não diz qual. O percentual também não foi definido. |
| Pedidos do iFood e do 99 Food acumulam cashback? | Se só os pedidos diretos acumularem, o cashback vira motivo para o cliente pedir pelo WhatsApp. |
| Quantas mensagens não compreendidas disparam o transbordo? | A US 02 usa 3 (RN11). O UC05 só diz "repetidas vezes". |

## Histórico

As estórias US 01 (Recepção de Pedidos e Geocodificação) e US 02 (Agrupamento e Roteirização por GPS) da versão anterior do trabalho foram substituídas pela Proposta de Projeto de 14/11/2026, que troca a roteirização pela localização nativa do WhatsApp.
