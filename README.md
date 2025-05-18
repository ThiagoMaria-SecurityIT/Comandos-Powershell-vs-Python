
<table>
  <tr>
    <td><img src="Images/Aba1.png" alt="Aba 1" width="300"></td>
    <td><img src="Images/Aba2.png" alt="Aba 2" width="300"></td>
    <td><img src="Images/Aba3.png" alt="Aba 3" width="300"></td>
    <td><img src="Images/Aba4.png" alt="Aba 4" width="400"></td>
  </tr>
  <tr>
    <td style="text-align: center;"> Aba 1</td>
    <td style="text-align: center;"> Aba 2</td>
    <td style="text-align: center;"> Aba 3</td>
    <td style="text-align: center;"> Aba 4 </td>
  </tr>
</table> 

## 📄 README.md 


# Guia de Comandos - Windows & Linux (PowerShell / WSL)

Um aplicativo simples e útil para facilitar a cópia e uso de comandos frequentes no PowerShell (Windows), terminal Linux/WSL e ambientes virtuais do Python.

---

## 🖼️ Visão Geral

Este projeto foi desenvolvido em Python com Tkinter, usando `ttkbootstrap` para tema escuro moderno. Ele permite que usuários copiem rapidamente comandos úteis para otimizar a produtividade!

---

## 🔧 Funcionalidades

- **Comandos Windows (PS)**: Lista de comandos do PowerShell com botões para copiar.
- **Comandos Linux / WSL**: Lista de comandos do terminal Linux/WSL.
- **Alias do PowerShell**: Tabela completa de alias + exportação como script `.ps1`.
- **Ambientes Virtuais do Python**: Dicas rápidas sobre comandos do `venv`.

---

## 🚀 Como Usar

1. Abra o app
2. Navegue entre as abas:
   - Clique nos botões para **copiar os comandos**
   - Na aba "Alias", use os botões para **exportar ou copiar o script PS1**

> 💡 **Dica:** Útil para devs que querem agilizar comandos no dia a dia no terminal.

---

## 🧰 Requisitos

- Python 3.8+
- Pacotes necessários:
  - `ttkbootstrap`
  - `pyperclip`
  - `tkinter (já vem com o Python)`
Instale as dependências com:

```bash
pip install ttkbootstrap pyperclip
```

---

## 🧪 Executar como Script

```bash
main.py
```

---

## 📦 Compilar como `.exe` (opcional)

Se quiser gerar um executável:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

O executável será gerado na pasta `dist/`.

---

## 📁 Estrutura do Projeto

```
.
├── main.py                       # Código principal
├── README.md                     # Este arquivo
├── requirements.txt              # Lista de dependências
└── Images/                       # Images é imagens em inglês da interface
```

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se quiser adicionar mais comandos, melhorar a interface ou integrar novas funcionalidades, fique à vontade.

---

## 📝 Licença

MIT License – veja [`LICENSE`](LICENSE) para mais detalhes.

---

## ❤️ Créditos

Desenvolvido com ❤️ por **Qwen3-235B-A22B** e Thiago Maria 🙋🏽! 

---

> **Ferramenta criada para facilitar a vida de quem vive no PowerShell e terminal.**

---

## ✅ Conteúdo do `requirements.txt`:

```
ttkbootstrap==1.13.7
pyperclip==1.9.0
```
