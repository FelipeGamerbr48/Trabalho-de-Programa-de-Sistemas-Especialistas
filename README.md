# Sistema Especialista – Assistência Técnica de Computadores

## 1. Sobre o Projeto

Este projeto consiste no desenvolvimento de um **Sistema Especialista utilizando a linguagem Python**, com a finalidade de auxiliar na identificação de possíveis problemas e falhas em computadores, considerando sintomas relacionados aos componentes internos do gabinete e ao monitor.

O sistema realiza uma consulta interativa com o usuário, apresentando perguntas sobre o funcionamento do computador e coletando informações sobre os sintomas observados. Com base nas respostas fornecidas, o programa utiliza uma base de conhecimento composta por **22 regras de produção** para analisar os fatos identificados e gerar possíveis diagnósticos.

O processo de análise é realizado por meio de um motor de inferência que utiliza a técnica de **encadeamento para frente (Forward Chaining)**, permitindo relacionar os sintomas informados às hipóteses de problemas cadastradas na base de conhecimento.

O objetivo principal é demonstrar a aplicação dos conceitos de Inteligência Artificial e Sistemas Especialistas na resolução de problemas práticos, simulando parte do processo de análise realizado em uma assistência técnica de computadores.

**Importante:** Os diagnósticos apresentados pelo sistema possuem caráter exclusivamente orientativo. Eles representam possíveis causas para os problemas identificados e não substituem uma avaliação técnica presencial. Para confirmar qualquer defeito, recomenda-se procurar um profissional especializado.

---

## 2. Tecnologias e Conceitos Utilizados

O desenvolvimento do projeto utiliza as seguintes tecnologias e conceitos:

- **Linguagem de programação:** Python 3.
- **Ambiente de desenvolvimento (IDE):** PyCharm.
- **Estruturas de dados:** Conjuntos (`set`) e listas.
- **Estruturas de controle:** Condicionais e estruturas de repetição.
- **Modularização:** Organização do código por meio de funções.
- **Representação do conhecimento:** Base de conhecimento estruturada em regras de produção.
- **Motor de inferência:** Encadeamento para frente (Forward Chaining).

---

## 3. Funcionamento do Sistema

O funcionamento da aplicação ocorre por meio das seguintes etapas:

1. **Coleta de informações:** O sistema apresenta perguntas ao usuário sobre os sintomas e o comportamento do computador.
2. **Identificação dos fatos:** As respostas fornecidas são armazenadas como fatos na base de conhecimento.
3. **Aplicação das regras:** O motor de inferência verifica quais regras de produção correspondem aos fatos identificados.
4. **Processamento das informações:** O sistema relaciona os sintomas e identifica possíveis causas para os problemas apresentados.
5. **Apresentação dos resultados:** Ao final da consulta, são exibidas as hipóteses de diagnóstico encontradas.

---

## 4. Como Executar o Projeto

Para executar o sistema, siga as etapas abaixo:

1. Certifique-se de que o **Python 3** esteja instalado em seu computador.
2. Baixe o repositório ou obtenha o arquivo `Assistencia Rio Tech.py`.
3. Abra o projeto no PyCharm ou em outro ambiente de desenvolvimento compatível com Python.
4. Execute o arquivo pelo terminal utilizando o comando:



Após a execução, o sistema iniciará a interação com o usuário, apresentando as perguntas necessárias para realizar a análise dos possíveis problemas do computador.

---

## 5. Objetivo Acadêmico

O projeto tem como finalidade aplicar, na prática, os conhecimentos adquiridos sobre Sistemas Especialistas, Inteligência Artificial, representação do conhecimento e mecanismos de inferência.

Além disso, busca demonstrar como regras lógicas podem ser utilizadas para organizar informações, interpretar sintomas e auxiliar na tomada de decisões em situações específicas.
