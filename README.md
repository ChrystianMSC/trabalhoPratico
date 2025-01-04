

# Projeto de Visualização 3D com React, TypeScript e Three.js

Autor: Chrystian Martins Soares Costa

Este projeto é uma aplicação web interativa que permite a visualização de um objeto 3D em um grid na tela, utilizando **React**, **TypeScript**, **Vite**, e **Three.js**. O objetivo principal é permitir que os usuários interajam com o objeto 3D, alterando sua cor e armazenando essas cores em um banco de dados para acessos futuros.

## Funcionalidades

- **Exibição de Objeto 3D**: Um objeto 3D é renderizado em um grid na tela utilizando **Three.js**.
- **Alteração de Cor**: O usuário pode alterar a cor do objeto 3D gerando cores aleatórias através de um botão.
- **Armazenamento de Cores**: As cores geradas aleatoriamente são armazenadas em um banco de dados, permitindo que sejam acessadas e reutilizadas em uma lista.

## Tecnologias Utilizadas

- **Frontend**:
  - **React**: Framework para a criação da interface do usuário.
  - **TypeScript**: Tipagem estática para garantir maior segurança e qualidade no código.
  - **Vite**: Ferramenta de build rápida para o desenvolvimento com React e TypeScript.
  - **Three.js**: Biblioteca JavaScript para renderizar o objeto 3D.
  - **Jest**: Framework de testes para garantir o bom funcionamento do frontend.

- **Backend**:
  - **Python**: Linguagem para o desenvolvimento da API.
  - **Django**: Framework para criação do backend e gerenciamento do banco de dados.
  - **Testes Unitários e de Sistema**: Implementação de testes para garantir a qualidade e estabilidade da API.

- **Banco de Dados**:
  - Armazenamento das cores geradas em um banco de dados **PostgreSQL** para persistência.

## Como Funciona

1. **Renderização do Objeto 3D**: O frontend renderiza um objeto 3D utilizando Three.js em um grid na tela.
2. **Gerar Cor Aleatória**: O usuário pode clicar em um botão para gerar uma cor aleatória e alterar a cor do objeto.
3. **Armazenamento de Cor**: Quando a cor é alterada, ela é automaticamente armazenada no banco de dados.
4. **Acessar Cores Armazenadas**: O usuário pode visualizar uma lista de todas as cores armazenadas previamente e selecionar uma para alterar a cor do objeto novamente.
5. **Movimentar a câmera**: O usuário pode clicar e arrastar a tela para movimentar a câmera no ambiente 3D, também pode utilizar o scroll para zum.

## Como Rodar o Projeto

### 1. **Frontend**

- Clone o repositório:
  ```bash
  git clone https://github.com/ChrystianMSC/trabalhoPratico.git
  cd trabalhoPratico
  ```

- Instale as dependências:
  ```bash
  cd portifolio
  npm install
  ```

- Inicie o servidor de desenvolvimento:
  ```bash
  npm run dev
  ```

O frontend estará disponível em `http://localhost:5173`.

### 2. **Backend**

Com o Front end rodando volte para o diretório raiz e acesse o diretório portfoliServer/backend.

- Crie um ambiente virtual:
  ```bash
  python -m venv venv
  source venv/bin/activate   # Para sistemas UNIX
  venv\Scripts\activate      # Para Windows
  ```

- Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

- Execute as migrações do banco de dados:
  ```bash
  python manage.py migrate
  ```

- Inicie o servidor backend:
  ```bash
  python manage.py runserver
  ```

### 3. **Testes**

- Para rodar os testes frontend com **Jest** no diretório raiz do front end faça:
  ```bash
  npm run test
  ```

- Para rodar os testes backend com **Django**:
  ```bash
  python manage.py test
  ```
