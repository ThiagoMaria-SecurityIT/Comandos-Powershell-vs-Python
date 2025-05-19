# Instale via: pip install pyperclip ttkbootstrap
# No Linux/WSL: sudo apt install xclip (para funcionar com pyperclip)
# Old version with tab Linux and Python
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CommandReferenceTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Guia de Comandos - Windows & Linux")
        self.root.geometry("1224x768")
        self.root.resizable(True, True)

        # Aplicar tema escuro moderno (do ttkbootstrap)
        style = ttk.Style("cyborg")  # Você pode trocar por 'superhero', 'darkly', etc.

        # Notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Abas principais
        self.windows_frame = ttk.Frame(self.notebook)
        self.linux_frame = ttk.Frame(self.notebook)
        self.alias_frame = ttk.Frame(self.notebook)
        self.venv_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.windows_frame, text="Comandos Windows (PS)")
        self.notebook.add(self.linux_frame, text="Comandos Linux / WSL")
        self.notebook.add(self.alias_frame, text="Alias do PowerShell")
        self.notebook.add(self.venv_frame, text="Python - Ambientes Virtuais")

        # Criar interfaces
        self.create_windows_ui()
        self.create_linux_ui()
        self.create_alias_ui()
        self.create_venv_ui()

    def create_windows_ui(self):
        label = ttk.Label(
            self.windows_frame,
            text="📌 Comandos úteis no PowerShell (Windows):",
            font=("Segoe UI", 12),
            bootstyle="info"
        )
        label.pack(pady=10)

        button_frame = ttk.Frame(self.windows_frame)
        button_frame.pack(pady=10)

        windows_commands = [
            ("Listar Arquivos", "dir", "Mostra arquivos da pasta atual"),
            ("Listar Detalhado", "ls -l", "Mostra detalhes dos arquivos"),
            ("Ver IP da Máquina", "ipconfig", "Mostra informações de rede"),
            ("Ver Usuário Atual", "whoami", "Mostra seu nome de usuário"),
            ("Limpar Tela", "clear", "Limpa o terminal"),
            ("Mostrar Localização", "pwd", "Mostra diretório atual"),
            ("Entrar em Pasta", "cd ", "Navega para outro diretório"),
            ("Criar Pasta", "mkdir ", "Cria uma nova pasta"),
            ("Apagar Arquivo", "rm ", "Remove um arquivo"),
            ("Processo em Porta LISTENING", "Get-Process -Id (netstat -a -o | Select-String \"LISTENING\" | ForEach-Object { $_.Line.Split()[-1] })", "Mostra qual processo está usando portas abertas"),
        ]

        for idx, (btn_text, cmd, desc) in enumerate(windows_commands):
            frame = ttk.Frame(button_frame)
            frame.pack(anchor='w', pady=4)

            btn = ttk.Button(
                frame,
                text=f"{btn_text}",
                width=25,
                bootstyle="primary",
                command=lambda c=cmd: self.copy_command(c)
            )
            btn.pack(side='left', padx=10)

            cmd_label = ttk.Label(frame, text=cmd, foreground="#00BFFF", font=("Courier", 9))
            cmd_label.pack(side='left', padx=5)

            if desc:
                desc_label = ttk.Label(frame, text=f"— {desc}", foreground="#cccccc", font=("Segoe UI", 8))
                desc_label.pack(side='left', padx=5)

    def create_linux_ui(self):
        label = ttk.Label(
            self.linux_frame,
            text="📌 Comandos úteis no Terminal (Linux / WSL):",
            font=("Segoe UI", 12),
            bootstyle="info"
        )
        label.pack(pady=10)

        button_frame = ttk.Frame(self.linux_frame)
        button_frame.pack(pady=10)

        linux_commands = [
            ("Listar Arquivos", "ls", "Mostra arquivos da pasta atual"),
            ("Listar Detalhado", "ls -l", "Mostra detalhes dos arquivos"),
            ("Ver IP da Máquina", "ip a", "Mostra informações de rede"),
            ("Ver Usuário Atual", "whoami", "Mostra seu nome de usuário"),
            ("Limpar Tela", "clear", "Limpa o terminal"),
            ("Mostrar Localização", "pwd", "Mostra diretório atual"),
            ("Entrar em Pasta", "cd ", "Navega para outro diretório"),
            ("Criar Pasta", "mkdir ", "Cria uma nova pasta"),
            ("Apagar Arquivo", "rm ", "Remove um arquivo"),
            ("Copiar Arquivo", "cp ", "Copia arquivos"),
            ("Mover/Renomear", "mv ", "Move ou renomeia arquivos"),
            ("Escrever Texto", "echo ", "Escreve texto na tela"),
            ("Abrir Editor", "nano ", "Abre editor de texto no terminal"),
            ("Rodar Script Python", "python3 meu_script.py", "Executa script Python"),
            ("Modo Interativo Python", "python3", "Entra no modo interativo do Python"),
            ("Onde está o Python", "which python3", "Mostra caminho do Python"),
            ("Atualizar Pacotes", "sudo apt update", "Atualiza lista de pacotes (Ubuntu/Debian)"),
            ("Instalar Pacote", "sudo apt install <nome>", "Instala pacote no Ubuntu/Debian"),
        ]

        for idx, (btn_text, cmd, desc) in enumerate(linux_commands):
            frame = ttk.Frame(button_frame)
            frame.pack(anchor='w', pady=4)

            btn = ttk.Button(
                frame,
                text=f"{btn_text}",
                width=25,
                bootstyle="primary",
                command=lambda c=cmd: self.copy_command(c)
            )
            btn.pack(side='left', padx=10)

            cmd_label = ttk.Label(frame, text=cmd, foreground="#00BFFF", font=("Courier", 9))
            cmd_label.pack(side='left', padx=5)

            if desc:
                desc_label = ttk.Label(frame, text=f"— {desc}", foreground="#cccccc", font=("Segoe UI", 8))
                desc_label.pack(side='left', padx=5)

    def create_alias_ui(self):
        """Aba 'Alias do PowerShell' com tabela visível e exportação"""
        label = ttk.Label(
            self.alias_frame,
            text="Lista de Alias do PowerShell:",
            font=("Segoe UI", 12),
            bootstyle="info"
        )
        label.pack(pady=10)

        # Tabela de aliases
        columns = ("Alias", "Comando Original")
        self.alias_tree = ttk.Treeview(self.alias_frame, columns=columns, show='headings', height=20)
        self.alias_tree.heading("Alias", text="Alias")
        self.alias_tree.heading("Comando Original", text="Comando Original")
        self.alias_tree.column("Alias", width=100, anchor='w')
        self.alias_tree.column("Comando Original", width=300, anchor='w')
        self.alias_tree.pack(padx=10, pady=5, fill='both', expand=True)

        alias_list = [
            ("%", "ForEach-Object"), ("?", "Where-Object"), ("ac", "Add-Content"),
            ("cat", "Get-Content"), ("cd", "Set-Location"), ("clc", "Clear-Content"),
            ("clear", "Clear-Host"), ("cls", "Clear-Host"), ("compare", "Compare-Object"),
            ("copy", "Copy-Item"), ("cp", "Copy-Item"), ("echo", "Write-Output"),
            ("epcsv", "Export-Csv"), ("erase", "Remove-Item"), ("fl", "Format-List"),
            ("foreach", "ForEach-Object"), ("ft", "Format-Table"), ("gal", "Get-Alias"),
            ("gc", "Get-Content"), ("gci", "Get-ChildItem"), ("gcm", "Get-Command"),
            ("ghy", "Get-History"), ("gl", "Get-Location"), ("gm", "Get-Member"),
            ("gp", "Get-ItemProperty"), ("gps", "Get-Process"), ("group", "Group-Object"),
            ("gsn", "Get-PSSession"), ("gsv", "Get-Service"), ("history", "Get-History"),
            ("icm", "Invoke-Command"), ("iex", "Invoke-Expression"),
            ("ihy", "Invoke-History"), ("ipcsv", "Import-Csv"), ("kill", "Stop-Process"),
            ("lp", "Out-Printer"), ("ls", "Get-ChildItem"), ("man", "help"),
            ("measure", "Measure-Object"), ("move", "Move-Item"), ("popd", "Pop-Location"),
            ("ps", "Get-Process"), ("pushd", "Push-Location"), ("pwd", "Get-Location"),
            ("r", "Invoke-History"), ("ren", "Rename-Item"), ("ri", "Remove-Item"),
            ("rm", "Remove-Item"), ("rmdir", "Remove-Item"), ("select", "Select-Object"),
            ("set", "Set-Variable"), ("sort", "Sort-Object"), ("type", "Get-Content"),
            ("wget", "Invoke-WebRequest"), ("where", "Where-Object"), ("write", "Write-Output")
        ]

        for alias, command in alias_list:
            self.alias_tree.insert("", tk.END, values=(alias, command))

        # Botões de ação
        button_frame = ttk.Frame(self.alias_frame)
        button_frame.pack(pady=10)

        ttk.Button(
            button_frame,
            text="Exportar Alias para Script PS1",
            width=30,
            bootstyle="success",
            command=self.export_alias_to_script
        ).pack(side='left', padx=5)

        ttk.Button(
            button_frame,
            text="Copiar Script para Área de Transferência",
            width=30,
            bootstyle="success",
            command=self.copy_alias_script
        ).pack(side='left', padx=5)

        # Aviso
        warn_label = ttk.Label(
            self.alias_frame,
            text="⚠️ Importar pode sobrescrever aliases existentes.\nUse `-Force` para forçar substituição.",
            foreground="orange",
            justify="center"
        )
        warn_label.pack(pady=5)

    def generate_alias_script(self):
        return '''@{ "%"="ForEach-Object"; "?"="Where-Object"; "ac"="Add-Content"; "cat"="Get-Content"; "cd"="Set-Location"; "clc"="Clear-Content"; "clear"="Clear-Host"; "cls"="Clear-Host"; "compare"="Compare-Object"; "copy"="Copy-Item"; "cp"="Copy-Item"; "echo"="Write-Output"; "epcsv"="Export-Csv"; "erase"="Remove-Item"; "fl"="Format-List"; "foreach"="ForEach-Object"; "ft"="Format-Table"; "gal"="Get-Alias"; "gc"="Get-Content"; "gci"="Get-ChildItem"; "gcm"="Get-Command"; "ghy"="Get-History"; "gl"="Get-Location"; "gm"="Get-Member"; "gp"="Get-ItemProperty"; "gps"="Get-Process"; "group"="Group-Object"; "gsn"="Get-PSSession"; "gsv"="Get-Service"; "history"="Get-History"; "icm"="Invoke-Command"; "iex"="Invoke-Expression"; "ihy"="Invoke-History"; "ipcsv"="Import-Csv"; "kill"="Stop-Process"; "lp"="Out-Printer"; "ls"="Get-ChildItem"; "man"="help"; "measure"="Measure-Object"; "move"="Move-Item"; "popd"="Pop-Location"; "ps"="Get-Process"; "pushd"="Push-Location"; "pwd"="Get-Location"; "r"="Invoke-History"; "ren"="Rename-Item"; "ri"="Remove-Item"; "rm"="Remove-Item"; "rmdir"="Remove-Item"; "select"="Select-Object"; "set"="Set-Variable"; "sort"="Sort-Object"; "type"="Get-Content"; "wget"="Invoke-WebRequest"; "where"="Where-Object"; "write"="Write-Output" } | % { Set-Alias -Name $_.Key -Value $_.Value }'''

    def export_alias_to_script(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".ps1",
            filetypes=[("PowerShell Script", "*.ps1")],
            initialfile="Set-Aliases.ps1"
        )
        if file_path:
            script_content = self.generate_alias_script()
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(script_content)
                messagebox.showinfo("Exportado", f"Script salvo em:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao salvar o arquivo:\n{e}")

    def copy_alias_script(self):
        script_content = self.generate_alias_script()
        try:
            pyperclip.copy(script_content)
            messagebox.showinfo("Copiado!", "Script de alias copiado para a área de transferência.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao copiar:\n{e}")

    def create_venv_ui(self):
        label = ttk.Label(
            self.venv_frame,
            text="Guia rápido para ambientes virtuais e uso no PowerShell:",
            font=("Segoe UI", 12),
            bootstyle="info"
        )
        label.pack(pady=10)

        tip_label = ttk.Label(
            self.venv_frame,
            text="📌 Dica: Para sair do modo interativo do Python:\n"
                 "Windows: Ctrl+Z + Enter\n"
                 "Linux/WSL: Ctrl+D",
            foreground="#cccccc",
            justify="left"
        )
        tip_label.pack(pady=5)

        self.env_entry = ttk.Entry(self.venv_frame, width=40, font=("Courier", 10), bootstyle="info")
        self.env_entry.pack(pady=5)
        self.env_entry.insert(0, "<nome_do_ambiente>")

        env_button_frame = ttk.Frame(self.venv_frame)
        env_button_frame.pack(pady=5)

        ttk.Button(
            env_button_frame,
            text="Usar Nome Ambiente",
            width=20,
            bootstyle="primary",
            command=self.update_commands_with_env
        ).pack(side='left', padx=5)

        ttk.Button(
            env_button_frame,
            text="Limpar Nome Ambiente",
            width=20,
            bootstyle="danger",
            command=self.clear_env_name
        ).pack(side='left', padx=5)

        self.script_entry = ttk.Entry(self.venv_frame, width=40, font=("Courier", 10), bootstyle="info")
        self.script_entry.pack(pady=5)
        self.script_entry.insert(0, "<meu_script>.py")

        script_button_frame = ttk.Frame(self.venv_frame)
        script_button_frame.pack(pady=5)

        ttk.Button(
            script_button_frame,
            text="Usar Nome Script",
            width=20,
            bootstyle="primary",
            command=self.update_commands_with_script
        ).pack(side='left', padx=5)

        ttk.Button(
            script_button_frame,
            text="Limpar Nome Script",
            width=20,
            bootstyle="danger",
            command=self.clear_script_name
        ).pack(side='left', padx=5)

        button_frame = ttk.Frame(self.venv_frame)
        button_frame.pack(pady=10)

        self.venv_commands_base = [
            ("1. Criar Ambiente Virtual", "py -m venv <nome_do_ambiente>", "Cria um novo ambiente isolado"),
            ("2. Ativar Ambiente Virtual", "<nome_do_ambiente>\\Scripts\\activate", "Ative antes de instalar pacotes"),
            ("3. Executar Script (.py) no PS", ".\\<meu_script>.py", "Evita erro de execução no PowerShell"),
            ("4. Desativar Ambiente Virtual", "deactivate", "Volta ao ambiente global"),
            ("5. Abrir Arquivo no Notepad", "notepad <meu_script>.py", "Abre script no editor padrão do Windows"),
            ("6. Abrir Script no IDLE", "python -m idlelib <meu_script>.py", "Abre script no IDLE do Python"),
            ("7. Onde está o Python?", "python -c \"import os; import sys; print(os.path.dirname(sys.executable))\"", "Mostra caminho do Python usado"),
            ("8. Modo Interativo Python", "python", "Entre no shell interativo do Python"),
        ]

        self.venv_buttons = []
        for idx, (btn_text, cmd, desc) in enumerate(self.venv_commands_base):
            frame = ttk.Frame(button_frame)
            frame.pack(anchor='w', pady=4)

            btn = ttk.Button(
                frame,
                text=btn_text,
                width=40,
                bootstyle="primary",
                command=lambda c=cmd: self.copy_command(c)
            )
            btn.pack(side='left', padx=5)

            cmd_label = ttk.Label(frame, text=cmd, foreground="#00BFFF", font=("Courier", 9))
            cmd_label.pack(side='left', padx=5)

            if desc:
                desc_label = ttk.Label(frame, text=f"— {desc}", foreground="#cccccc", font=("Segoe UI", 8))
                desc_label.pack(side='left', padx=5)

            self.venv_buttons.append((btn, cmd_label, cmd))

    def update_commands_with_env(self):
        env_name = self.env_entry.get().strip()
        if not env_name or env_name == "<nome_do_ambiente>":
            messagebox.showwarning("Nome Inválido", "Digite um nome válido para o ambiente virtual.")
            return
        for btn, label, base_cmd in self.venv_buttons:
            new_cmd = base_cmd.replace("<nome_do_ambiente>", env_name)
            label.config(text=new_cmd)
            btn.configure(command=lambda c=new_cmd: self.copy_command(c))

    def clear_env_name(self):
        self.env_entry.delete(0, tk.END)
        self.env_entry.insert(0, "<nome_do_ambiente>")
        for btn, label, base_cmd in self.venv_buttons:
            label.config(text=base_cmd)
            btn.configure(command=lambda c=base_cmd: self.copy_command(c))

    def update_commands_with_script(self):
        script_name = self.script_entry.get().strip()
        if not script_name or script_name == "<meu_script>.py":
            messagebox.showwarning("Nome Inválido", "Digite um nome válido para o script.")
            return
        for btn, label, base_cmd in self.venv_buttons:
            new_cmd = base_cmd.replace("<meu_script>.py", script_name)
            label.config(text=new_cmd)
            btn.configure(command=lambda c=new_cmd: self.copy_command(c))

    def clear_script_name(self):
        self.script_entry.delete(0, tk.END)
        self.script_entry.insert(0, "<meu_script>.py")
        for btn, label, base_cmd in self.venv_buttons:
            label.config(text=base_cmd)
            btn.configure(command=lambda c=base_cmd: self.copy_command(c))

    def copy_command(self, cmd):
        try:
            pyperclip.copy(cmd)
            messagebox.showinfo("Copiado!", f"Comando copiado:\n{cmd}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao copiar:\n{e}")


if __name__ == "__main__":
    root = ttk.Window(themename="cyborg")  # Tema escuro moderno
    app = CommandReferenceTool(root)
    root.mainloop()
