# 🐖 Sistema de Pesagem Inteligente de Suínos

Sistema desenvolvido para monitoramento de peso de suínos utilizando sensores e integração com aplicação web, permitindo coleta, armazenamento e visualização de dados em tempo real.

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo automatizar o processo de pesagem de suínos, reduzindo erros manuais e facilitando o acompanhamento do crescimento dos animais.

A solução utiliza sensores de peso integrados a um microcontrolador, que envia os dados para uma aplicação responsável por processar, armazenar e exibir as informações.

---

## 🚀 Funcionalidades

- 📊 Coleta automática de peso
- 🔄 Atualização de dados em tempo real
- 💾 Armazenamento em banco de dados
- 📈 Visualização dos dados (dashboard)
- 🔐 Possibilidade de autenticação de usuários

---

## 🛠️ Tecnologias Utilizadas

### 🔌 Hardware
- Célula de carga (Load Cell)
- Módulo HX711
- Microcontrolador (Esp 8266)

### 💻 Software
- Python
- Flask
- MySQL
- BootsTrap


---

## ⚙️ Arquitetura do Sistema

```text
[ Célula de Carga ]
        ↓
     [ HX711 ]
        ↓
 [ Microcontrolador ]
        ↓
   (Envio de dados)
        ↓
   [ API / Backend ] -> [front-end]
        ↓
 [ Banco de Dados ]
