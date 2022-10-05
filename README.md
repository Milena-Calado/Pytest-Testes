# Pytest-Testes

Pytest é uma ferramenta que lhe ajuda a escrever programas melhores, facilitando a escrita de testes pequenos e legíveis para dar supoerte a testes funcionais complexos para aplicativos e bibliotecas.

Requer Python 3.7+ ou PyPy3.

Nome do pacote PyPI : pytest

# Um exemplo básico: 

content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
Para executá-lo:

$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================


Características:

- Informações detalhadas sobre falhas nas declarações assert (sem necessidade de lembrar self.assert*nomes);
- Descoberta automática de módulos e funções de teste;
- Acessórios modulares para gerenciar recursos de teste pequenos ou parametrizados de longa duração;
- Pode executar testes unitários e conjuntos de testes prontos para uso;

Python 3.7+ ou PyPy 3

Arquitetura de plugins rica, com mais de 800 plugins externos e comunidade próspera

Documentação 

- Instale o pytest e entenda o básico em apenas vinte minutos; https://docs.pytest.org/en/7.1.x/getting-started.html#get-started
- Guias de instruções - guias passo a passo, cobrindo uma vasta gama de casos de uso e necessidades: https://docs.pytest.org/en/7.1.x/how-to/index.html#how-to
- Guias de referência - inclui a referência completa da API pytest, listas de plugins e muito mais: https://docs.pytest.org/en/7.1.x/reference/index.html#reference
- Explicação - antecedentes, discussão de tópicos-chave, respostas a perguntas de nível superior: https://docs.pytest.org/en/7.1.x/explanation/index.html#explanation

Bugs/Solicitações 

- Use o rastreador de problemas do GitHub para enviar bugs ou solicitar recursos: https://github.com/pytest-dev/pytest/issues

Segurança

Pytest nunca foi associado a uma vulnerabilidade de segurança, mas em qualquer caso, para relatar uma vulnerabilidade de segurança, use o contato de segurança do Tidelift . [A Tidelift coordenará a correção e divulgação.](https://tidelift.com/docs/security)
