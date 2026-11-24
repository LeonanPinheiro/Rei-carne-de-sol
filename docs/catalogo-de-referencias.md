# Catálogo de referências

Requisitos, regras de negócio, casos de uso, modelo de dados e mensagens citados nas estórias. Os itens RF01 a RF06, RNF01 a RNF04, RN01 a RN05 e UC01 a UC05 vêm da [Proposta de Projeto](proposta/Proposta_de_Projeto_-_Rei_da_Carne_de_Sol.pdf) de 14/11/2026; os demais foram criados no detalhamento das estórias.

## Casos de uso (UC)

| Código | Caso de uso | Estória |
| --- | --- | --- |
| UC01 | Consultar Cardápio: navegação estruturada em menus para ver opções e preços. | US 01 |
| UC02 | Realizar Pedido: seleção dos pratos com a confirmação de que o pagamento será na entrega. | US 01 |
| UC03 | Rastreio em Tempo Real: o cliente consulta o andamento e, quando o pedido sai, recebe a localização do entregador no chat. | US 01 |
| UC04 | Gerenciar Pedidos (Painel Web): o restaurante atualiza o status de cada pedido. | US 02 |
| UC05 | Transbordo Humano: o cliente pede "Falar com pessoa" ou não é compreendido várias vezes; o bot pausa e o painel é notificado. | US 01, US 02 |

## Requisitos funcionais (RF)

| Código | Requisito | Estória |
| --- | --- | --- |
| RF01 | O sistema deve saudar o cliente e fornecer um menu principal interativo (botões ou opções de 1 a 5). | US 01 |
| RF02 | O sistema deve calcular o total da compra e incluir a taxa de entrega da localidade. | US 01 |
| RF03 | O sistema deve instruir o entregador e o cliente para o uso do envio de localização nativo do WhatsApp. | US 01, US 02 |
| RF04 | O sistema deve contabilizar saldo de cashback atrelado ao número do WhatsApp. | US 04 |
| RF05 | O sistema deve possuir um comando claro de interrupção do bot para direcionamento à equipe humana. | US 01, US 02 |
| RF06 | O painel web deve receber atualizações instantâneas de novos pedidos (websockets). | US 02 |

## Requisitos não funcionais (RNF)

| Código | Requisito |
| --- | --- |
| RNF01 | A resposta do bot nas navegações estruturadas deve ser imediata (até 2 segundos). |
| RNF02 | A identidade visual (textos e emojis) deve remeter à cultura nordestina. |
| RNF03 | Conformidade com a LGPD, sem retenção de cartões. Dados pessoais aparecem mascarados em listas e exportações. |
| RNF04 | O painel operacional deve ser visualmente claro e responsivo. |

## Regras de negócio (RN)

| Código | Regra | Estórias |
| --- | --- | --- |
| RN01 | Horário: os menus automáticos de pedidos só operam durante o expediente do restaurante. | US 01 |
| RN02 | Pagamento físico: é proibido pedir dados financeiros no WhatsApp. Todo pagamento ocorre na entrega. | US 01 |
| RN03 | Segurança de rastreio: o status "Saiu para Entrega" é ativado manualmente no painel para liberar o rastreio ao cliente. | US 01, US 02 |
| RN04 | Garantia de atendimento humano: o pedido de contato humano tem precedência e congela o bot até o gestor resolver a pendência. | US 01, US 02 |
| RN05 | Validade de pontos: o cashback expira em 90 dias e exige valor mínimo para resgate. | US 04 |
| RN06 | O CPF identifica o profissional de forma única e não pode ser alterado depois do cadastro. | US 03 |
| RN07 | O entregador deve ter celular com WhatsApp, usado para receber a instrução de envio de localização (RF03). | US 03 |
| RN08 | Profissional com status Ativo não pode ser excluído; deve ser desativado antes, para preservar o histórico. | US 03 |
| RN09 | Entregador com pedido em status "Saiu para Entrega" não pode ser desativado nem excluído. | US 02, US 03 |
| RN10 | O status do pedido segue a ordem Recebido, Em preparo, Pronto, Saiu para Entrega, Entregue. Só é possível avançar uma etapa por vez ou cancelar antes da saída para entrega. | US 02 |
| RN11 | Detalha o UC05: depois de 3 mensagens seguidas não compreendidas, o bot transfere a conversa para atendimento humano. | US 01, US 02 |

## Modelo de dados (MED)

| Código | Entidade | Campos |
| --- | --- | --- |
| MED 01 | Cliente | NÚMERO WHATSAPP (identificador), NOME, PERFIL (novo ou recorrente), SALDO DE CASHBACK |
| MED 02 | Pedido | NÚMERO, CLIENTE, ITENS, TOTAL, TAXA DE ENTREGA, STATUS, ENTREGADOR, DATA E HORA, MOTIVO DE CANCELAMENTO |
| MED 03 | Profissional | ID, NOME, CPF, TELEFONE, E-MAIL, FUNÇÃO (Gestor, Atendente, Cozinha, Entregador), STATUS (Ativo, Inativo) |
| MED 04 | Atendimento humano | CLIENTE, MOTIVO (solicitado ou não compreendido), STATUS (Aguardando, Em atendimento, Encerrado), RESPONSÁVEL, ABERTURA, ENCERRAMENTO |

### Formatos aceitos

| Campo | Formato | Exemplo |
| --- | --- | --- |
| NOME | 3 a 100 caracteres, com nome e sobrenome | Maria da Silva |
| CPF | 11 dígitos com dígitos verificadores válidos | 529.982.247-25 |
| TELEFONE | DDD + 8 ou 9 dígitos | (22) 2665-1234 |
| TELEFONE do entregador | Celular: DDD + 9 + 8 dígitos | (22) 98824-1488 |
| E-MAIL | nome@dominio | maria@email.com |
| MOTIVO DE CANCELAMENTO | 5 a 200 caracteres | Cliente desistiu do pedido |

## Mensagens do sistema (MSG)

| Código | Texto |
| --- | --- |
| MSG 01 | Cadastro realizado com sucesso. |
| MSG 02 | Profissional já cadastrado. |
| MSG 03 | O preenchimento do campo XXX deve seguir o formato YYY. |
| MSG 04 | Dado alterado com sucesso. |
| MSG 05 | Deseja realmente excluir esse registro? |
| MSG 11 | O profissional não foi localizado. |
| MSG 14 | Sistema não permite esta operação. |
| MSG 17 | Registro excluído com sucesso. |
| MSG 30 | Novo pedido recebido. (alerta visual e sonoro no painel) |
| MSG 31 | Cliente aguardando atendimento humano. (alerta visual e sonoro no painel) |
| MSG 32 | Status do pedido atualizado. |
| MSG 33 | Seu pedido saiu para entrega, visse! Já já o entregador manda a localização dele aqui no chat. (para o cliente) |
| MSG 34 | Envie sua localização em tempo real para o cliente pelo WhatsApp. (para o entregador) |
| MSG 35 | Deseja realmente cancelar este pedido? |
| MSG 36 | Pedido cancelado. O cliente foi avisado pelo WhatsApp. |
| MSG 37 | Atendimento encerrado. O bot voltou a responder este cliente. |
