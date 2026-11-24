# Catálogo de referências

Regras de negócio (RNE), modelo de dados (MED) e mensagens do sistema (MSG) citadas nas estórias de usuário.

## Regras de negócio (RNE)

| Código | Regra | Estórias |
| --- | --- | --- |
| RNE 05 | Integração obrigatória com a Google Maps Directions API, com falha prevista e despacho manual como alternativa. | US 02 |
| RNE 06 | O CPF identifica o profissional de forma única. Não pode haver dois profissionais com o mesmo CPF, e o CPF não pode ser alterado depois do cadastro. | US 03 |
| RNE 07 | Profissional com a função Entregador deve ter CNH (11 dígitos) e placa do veículo (padrão antigo `ABC1234` ou Mercosul `ABC1D23`). | US 03 |
| RNE 08 | Profissional com status Ativo não pode ser excluído. Ele deve ser desativado antes, para preservar o histórico. | US 03 |
| RNE 09 | Entregador com lote em status Em Rota não pode ser desativado nem excluído até concluir a entrega. | US 02, US 03 |

## Modelo de dados (MED)

| Código | Entidade | Campos |
| --- | --- | --- |
| MED 03 | Profissional | ID, NOME, CPF, TELEFONE, E-MAIL, FUNÇÃO (Atendente, Cozinheiro, Expedidor, Entregador, Gerente), CNH, PLACA, STATUS (Ativo, Inativo) |

### Formatos aceitos

| Campo | Formato | Exemplo |
| --- | --- | --- |
| NOME | 3 a 100 caracteres, com nome e sobrenome | Maria da Silva |
| CPF | 11 dígitos com dígitos verificadores válidos | 529.982.247-25 |
| TELEFONE | DDD + 8 ou 9 dígitos | (22) 98824-1488 |
| E-MAIL | nome@dominio | maria@email.com |
| CNH | 11 dígitos | 12345678901 |
| PLACA | `ABC1234` ou `ABC1D23` | RIO2A18 |

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
| MSG 20 | Lote de entrega formado com sucesso. |
| MSG 21 | Pedido isolado encaminhado para rota exclusiva. |
| MSG 22 | Rota otimizada gerada. |
| MSG 23 | Rota enviada ao entregador. |
| MSG 50 | Falha na comunicação com o GPS. Despacho manual necessário. |
