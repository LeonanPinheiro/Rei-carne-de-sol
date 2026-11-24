# O Rei da Carne de Sol · Sistema de Gestão de Pedidos e Delivery Urbano

Trabalho A2 da disciplina **Análise Orientada a Objetos** (Universidade Veiga de Almeida), feito pelo grupo **Os 4 Devs** para o restaurante O Rei da Carne de Sol, no bairro Fazendinha, em Araruama (RJ).

O sistema centraliza os pedidos do restaurante e organiza o delivery: agrupa os pedidos prontos por proximidade e gera rotas para os motoboys. Este repositório guarda as estórias de usuário e o protótipo em Python que as implementa.

## Equipe

| Integrante | Papel Scrum | Função técnica |
| --- | --- | --- |
| Matheus Frazão | Product Owner | Arquiteto de Software e Integrações |
| Leonan Costa | Scrum Master | Desenvolvedor Backend e Banco de Dados |
| Angel Moreira | Desenvolvedor | Desenvolvedor Web (Frontend) |

## Product Backlog

| Estória | Título | Prioridade | Situação |
| --- | --- | --- | --- |
| US 01 | Recepção de Pedidos e Geocodificação de Endereço | 1-Alta | Especificada no documento do trabalho |
| US 02 | Agrupamento e Roteirização de Pedidos (GPS) | 1-Alta | Especificada no documento do trabalho |
| [US 03](docs/estorias/US-03-cadastro-de-profissionais.md) | Cadastro de Profissionais | 1-Alta | Especificada e implementada |

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
