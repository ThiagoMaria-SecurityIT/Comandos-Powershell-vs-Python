# 📚 Guia de Comandos - Windows & Linux

> Uma ferramenta gráfica simples (e feia, mas prática) para quem vive no terminal.

---

## O que esse programa faz?

Era para ser um cheat sheet rápido com os comandos mais usados no **PowerShell (Windows)** e no **Terminal (Linux/WSL)** mas acabei me empolgando hahahaha. Tem também uma aba com os **alias do PowerShell** e outra pra ajudar com **ambientes virtuais do Python**.

É tudo feito em Python com `tkinter` e estilizado com `ttkbootstrap`. A interface não é bonita, mas funciona. Igual aquele TCC que vc faz em 2 horas e entrega só pra passar mesmo (brincadeira, jamais entreguem um TCC assim 😅). 

<table>
  <tr>
    <td><img src="imagens/aba1.png" alt="Aba 1" width="400"></td>
    <td><img src="imagens/aba2.png" alt="Aba 2" width="400"></td>
    <td><img src="imagens/aba3.jpg" alt="Aba 3" width="400"></td>
    <td><img src="imagens/aba4.jpg" alt="Aba 4" width="400"></td>
  </tr>
  <tr>
    <td style="text-align: center;"> Aba 1</td>
    <td style="text-align: center;"> Aba 2</td>
    <td style="text-align: center;"> Aba 3</td>
    <td style="text-align: center;"> Aba 4 </td>
  </tr>
</table>
---

## 🧩 Abas do Programa

### 1. **Comandos Windows (PS)**  
Lista comandos básicos do PowerShell como `dir`, `ipconfig`, `cd`, `mkdir`, etc. Cada um tem um botão pra copiar pro clipboard.

### 2. **Comandos Linux / WSL**  
Mesma coisa, mas pra quem usa Linux ou WSL. Tem `ls`, `clear`, `python3`, `apt update`, entre outros clássicos.

### 3. **Alias do PowerShell**  
Mostra uma tabela com os alias mais comuns do PowerShell (tipo `ls` pra `Get-ChildItem`) e permite exportar um script `.ps1` pra criar todos eles.

### 4. **Python - Ambientes Virtuais**  
Dá dicas de como criar, ativar e usar ambientes virtuais. Você pode digitar o nome do ambiente ou do script e ele atualiza os comandos automaticamente.

---

## ⚙️ Como rodar?

Instale as dependências:

```bash
pip install pyperclip ttkbootstrap
```

No Linux ou WSL, instale isso também:

```bash
sudo apt install xclip
```

Depois é só rodar:

```bash
python main.py
```

---

## 💡 Observação importante

Tem alguns comandos Linux que funcionam no PowerShell? Sim, porque alguns já vêm com alias padrão. Então se você rodar `ls` no PowerShell e funcionar... não é magia, é só o alias te salvando.

---

## 🖥️ Interface?

É feia, sim. Mas é funcional. Se quiser deixar mais bonita depois, dá pra trocar o tema do `ttkbootstrap`.

---

## 📄 Licença

MIT. Use, modifique, compartilhe e me avise se te ajudou.
