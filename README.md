# O Rei da Carne de Sol · Sistema Chatbot WhatsApp

Trabalho A2 da disciplina **Análise Orientada a Objetos** (Universidade Veiga de Almeida), feito pelo **Grupo MMLA** (Matheus, Maria, Leonan e Angel) para o restaurante O Rei da Carne de Sol, no bairro Fazendinha, em Araruama (RJ).

O sistema tem dois lados:

- **Cliente:** um chatbot no WhatsApp, com menus em árvore de decisão e linguagem nordestina, para ver o cardápio, fazer o pedido, acumular cashback, acompanhar o status, receber a localização do entregador pelo GPS nativo do WhatsApp e pedir para falar com uma pessoa a qualquer momento. O pagamento é feito na entrega.
- **Restaurante:** um painel web para organizar os pedidos, receber alertas de atendimento humano e liberar o rastreio quando o pedido sai para entrega.

O bot não usa IA generativa: as respostas são pré-configuradas, o que elimina custo por token e evita respostas erradas sobre o cardápio.

## Equipe

| Integrante | Papel Scrum | Função técnica |
| --- | --- | --- |
| Angel Moreira Soares Guimarães | Desenvolvedor | Desenvolvedor Web (Frontend) |
| Leonan Pinheiro Costa | Scrum Master | Desenvolvedor Backend e Banco de Dados |
| Maria Luiza Benevides Cunha | Desenvolvedora | Desenvolvedora de Automação e UX/UI |
| Matheus de Aguiar Maia Frazão Serrado | Product Owner | Arquiteto de Software e Integrações |

## Tecnologias

| Camada | Tecnologia |
| --- | --- |
| Canal com o cliente | WhatsApp Cloud API (oficial da Meta) |
| Fluxo do bot | n8n ou Typebot (árvores de decisão) |
| Banco de dados | PostgreSQL ou MySQL |
| Painel do restaurante | React.js, com atualização por websockets |
| Organização | Trello (Sprints), GitHub (versionamento), VS Code |

O protótipo em Python deste repositório valida as regras de negócio das estórias com testes de aceitação automáticos.

## Organização do trabalho

As tarefas das Sprints ficam no quadro do Trello: [Rei da Carne de Sol · Delivery](https://trello.com/b/FnCgakIm/rei-da-carne-do-sol-delivery).

## Product Backlog

| Estória | Tipo | Título | Situação |
| --- | --- | --- | --- |
| US 01 | História do Usuário | Fazer pedido pelo WhatsApp | Em elaboração |
| [US 02](docs/estorias/US-02-gerenciar-pedidos-e-atendimento-humano.md) | História do Profissional | Gerenciar pedidos e atendimento humano no painel | Especificada |
| [US 03](docs/estorias/US-03-cadastro-de-profissionais.md) | Estória de apoio | Cadastro de profissionais | Especificada e implementada |
| US 04 | Estória de usuário | Acumular e resgatar cashback | Candidata |
| US 05 | Estória de usuário | Identificar o cliente pelo número do WhatsApp | Candidata |

Detalhes e decisões em aberto: [docs/backlog-do-produto.md](docs/backlog-do-produto.md). Requisitos, regras de negócio e mensagens: [catálogo de referências](docs/catalogo-de-referencias.md).

## Estrutura

```
docs/
  proposta/                      Proposta de Projeto (14/11/2026)
  estorias/                      estórias no modelo da disciplina (Markdown e PDF)
  backlog-do-produto.md          estórias, prioridades e decisões em aberto
  catalogo-de-referencias.md     UC, RF, RNF, RN, MED e MSG
  gerar_pdf.py                   gera o PDF de cada estória
src/rei_carne_de_sol/
  mensagens.py                   textos das MSG
  profissionais/                 US 03: modelo, validações e regras
tests/
  test_aceitacao_us03.py         um teste de aceitação por CPO
```

## Como rodar

Requer Python 3.10 ou mais novo.

```bash
pip install -e ".[dev]"
pytest -v                  # testes de aceitação
python docs/gerar_pdf.py   # regera os PDFs das estórias
```

Cada teste tem o nome do padrão de comportamento que verifica, por exemplo `test_cpo_4_3_nao_permite_excluir_profissional_ativo`.

---

Projeto acadêmico. Os dados usados nos exemplos e testes são fictícios.
