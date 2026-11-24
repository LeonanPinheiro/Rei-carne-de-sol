# O Rei da Carne de Sol · Sistema de Gestão de Pedidos e Delivery Urbano

Trabalho A2 da disciplina **Análise Orientada a Objetos** (Universidade Veiga de Almeida), feito pelo grupo **Os 4 Devs** para o restaurante O Rei da Carne de Sol, no bairro Fazendinha, em Araruama (RJ).

O sistema concentra os pedidos diretos do restaurante e organiza o delivery: atendimento por um agente de IA no WhatsApp, cardápio online, cadastro automático do cliente pelo telefone, pontos e cashback, fila da cozinha e roteirização das entregas. Este repositório guarda a documentação (estórias de usuário e regras) e o código de todo o sistema.

## Equipe

| Integrante | Matrícula | Papel Scrum | Função técnica |
| --- | --- | --- | --- |
| Angel Moreira Soares Guimarães | 1250103118 | Desenvolvedor | Desenvolvedor Web (Frontend) |
| Leonan Pinheiro Costa | 1250103989 | Scrum Master | Desenvolvedor Backend e Banco de Dados |
| Maria Luiza Benevides Cunha | 1250112092 | [A DEFINIR] | [A DEFINIR] |
| Matheus Frazão Aguiar | [A CONFIRMAR] | Product Owner | Arquiteto de Software e Integrações |

## Organização do trabalho

As tarefas das Sprints ficam no quadro do Trello: [Rei da Carne de Sol · Delivery](https://trello.com/b/FnCgakIm/rei-da-carne-do-sol-delivery).

## Product Backlog

O backlog completo, com épicos, estórias candidatas e regras em discussão, está em [docs/backlog-do-produto.md](docs/backlog-do-produto.md).

| Épico | Estórias | Situação |
| --- | --- | --- |
| E1 · Pedidos e delivery | US 01, US 02 | Especificadas |
| E2 · Cadastros | [US 03 Profissionais](docs/estorias/US-03-cadastro-de-profissionais.md), US 04 Clientes pelo WhatsApp | US 03 implementada |
| E3 · Atendimento por WhatsApp (agente de IA) | US 05, US 06 | Candidatas |
| E4 · Cardápio online | US 07, US 08 | Candidatas |
| E5 · Fidelidade (pontos e cashback) | US 09 a US 12 | Candidatas |

As regras de negócio, o modelo de dados e as mensagens citadas nas estórias estão no [catálogo de referências](docs/catalogo-de-referencias.md).

## Estrutura

```
docs/
  estorias/US-03-cadastro-de-profissionais.md   estória completa (modelo da disciplina)
  estorias/US-03-cadastro-de-profissionais.pdf  a mesma estória, para entrega
  catalogo-de-referencias.md                    RNE, MED e MSG
src/rei_carne_de_sol/
  mensagens.py                                  textos das MSG
  profissionais/                                US 03: modelo, validações e regras
tests/
  test_aceitacao_us03.py                        um teste de aceitação por CPO
```

## Como rodar

Requer Python 3.10 ou mais novo.

```bash
pip install -e ".[dev]"
pytest -v
```

Cada teste tem o nome do padrão de comportamento que verifica, por exemplo `test_cpo_4_3_nao_permite_excluir_profissional_ativo`. Se todos passam, todos os critérios de aceitação da US 03 são atendidos.

## Exemplo de uso

```python
from rei_carne_de_sol.profissionais import Funcao, ServicoProfissionais

servico = ServicoProfissionais()
resultado = servico.incluir(
    "João Souza", "111.444.777-35", "(22) 99999-0000", "joao@email.com",
    Funcao.ENTREGADOR, cnh="12345678901", placa="RIO2A18",
)
print(resultado.textos)  # ['Cadastro realizado com sucesso.']
```

---

Projeto acadêmico. Os dados usados nos exemplos e testes são fictícios.
