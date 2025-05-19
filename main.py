# Instale via: pip install pyperclip ttkbootstrap
# No Linux/WSL: sudo apt install xclip (para funcionar com pyperclip)
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pyperclip
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
from datetime import datetime
import threading
import queue

class ModernCommandReferenceTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Command Reference Tool")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 800)
        
        # Apply dark theme
        self.style = ttk.Style(theme="cyborg")
        self.style.configure("danger.TButton", foreground="white")
        
        # Setup command queue
        self.command_queue = queue.Queue()
        self.root.after(100, self.process_queue)
        
        # Initialize threat feeds
        self.threat_feeds = {}
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Header
        self.create_header()
        
        # Main content area with tabs
        self.create_tab_interface()
        
        # Status bar
        self.create_status_bar()
        
        # Start monitoring
        self.start_threat_monitor()
    
    def create_header(self):
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(fill='x', pady=(0, 10))
        
        # App title
        title_frame = ttk.Frame(header_frame)
        title_frame.pack(side='left', padx=15, pady=10)
        
        ttk.Label(
            title_frame, 
            text="🛡️ Command Reference Tool", 
            font=("Segoe UI", 18, "bold")
        ).pack(side='left')
        
        # Threat level indicator
        self.threat_level = ttk.Label(
            header_frame,
            text="🟢 THREAT LEVEL: NORMAL",
            foreground="green",
            font=("Segoe UI", 12, "bold")
        )
        self.threat_level.pack(side='right', padx=15)
        
        # Search functionality
        search_frame = ttk.Frame(header_frame)
        search_frame.pack(side='right', padx=15, pady=10)
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            width=30
        )
        search_entry.pack(side='left', padx=5)
        search_entry.insert(0, "Search commands...")
        
        ttk.Button(
            search_frame,
            text="Search",
            command=self.search_commands
        ).pack(side='left')

    def search_commands(self):
        """Placeholder for search functionality"""
        query = self.search_var.get()
        messagebox.showinfo(
            "Search", 
            f"Would search for: {query}\n(Search functionality to be implemented)",
            parent=self.root
        )

    def create_tab_interface(self):
        """Create the notebook with tabs"""
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True)
        
        # Create CyberSec tab first
        self.create_cybersec_tab()
        
        # Create other tab frames
        self.windows_frame = ttk.Frame(self.notebook)
        self.linux_frame = ttk.Frame(self.notebook)
        self.alias_frame = ttk.Frame(self.notebook)
        self.venv_frame = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.windows_frame, text="🪟 Windows")
        self.notebook.add(self.linux_frame, text="🐧 Linux/WSL")
        self.notebook.add(self.alias_frame, text="🔤 Aliases")
        self.notebook.add(self.venv_frame, text="🐍 Python")
        
        # Populate tabs
        self.create_windows_ui()
        self.create_linux_ui()
        self.create_alias_ui()
        self.create_venv_ui()

    def create_cybersec_tab(self):
        """Create cybersecurity dashboard"""
        self.cyber_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.cyber_frame, text="🛡️ CyberSec")
        
        # Main paned window
        paned = ttk.PanedWindow(self.cyber_frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # Left pane - Monitoring
        left_pane = ttk.Frame(paned)
        paned.add(left_pane, weight=2)
        
        # Network Activity
        net_frame = ttk.LabelFrame(left_pane, text="🌐 Network Activity", padding=10)
        net_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.net_activity = scrolledtext.ScrolledText(
            net_frame,
            height=10,
            wrap=tk.WORD,
            bg='black',
            fg='lime',
            font=("Consolas", 9)
        )
        self.net_activity.pack(fill=tk.BOTH)
        self.net_activity.insert(tk.END, "Initializing network monitor...\n")
        
        btn_frame = ttk.Frame(net_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(
            btn_frame,
            text="Refresh",
            command=self.refresh_connections,
            style='info.TButton'
        ).pack(side=tk.LEFT, padx=2)
        
        # Right pane - Tools
        right_pane = ttk.Frame(paned)
        paned.add(right_pane, weight=1)
        
        # Quick Actions
        action_frame = ttk.LabelFrame(right_pane, text="⚡ Quick Actions", padding=10)
        action_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        
        actions = [
            ("Port Scan", self.run_port_scan),
            ("Process Audit", self.analyze_processes),
            ("Check Firewall", self.check_firewall)
        ]
        
        for text, cmd in actions:
            ttk.Button(
                action_frame,
                text=text,
                command=cmd,
                style='info.TButton',
                width=15
            ).pack(fill=tk.X, pady=2)

    def refresh_connections(self):
        """Refresh network connections"""
        def _run():
            try:
                result = subprocess.run(
                    ["powershell", "Get-NetTCPConnection -State Established | Select-Object LocalAddress,LocalPort,RemoteAddress,RemotePort,State | Format-Table"],
                    capture_output=True,
                    text=True
                )
                output = result.stdout if result.returncode == 0 else result.stderr
                self.command_queue.put((
                    self._update_net_activity,
                    output
                ))
            except Exception as e:
                self.command_queue.put((
                    self._show_error,
                    f"Connection refresh failed: {str(e)}"
                ))
        
        threading.Thread(target=_run, daemon=True).start()

    def _update_net_activity(self, text):
        """Update network activity display"""
        self.net_activity.delete(1.0, tk.END)
        self.net_activity.insert(tk.END, f"Last updated: {datetime.now().strftime('%H:%M:%S')}\n\n")
        self.net_activity.insert(tk.END, text)
        self.net_activity.see(tk.END)

    def run_port_scan(self):
        """Run port scan"""
        self._run_powershell_command("Test-NetConnection -ComputerName localhost -Port 80", "Port Scan")

    def analyze_processes(self):
        """Analyze running processes"""
        self._run_powershell_command("Get-Process | Sort-Object CPU -Descending | Select-Object -First 10", "Process Audit")

    def check_firewall(self):
        """Check firewall status"""
        self._run_powershell_command("Get-NetFirewallProfile | Format-Table Name, Enabled", "Firewall Check")

    def _run_powershell_command(self, command, description):
        """Run PowerShell command and display results"""
        def _run():
            try:
                result = subprocess.run(
                    ["powershell", command],
                    capture_output=True,
                    text=True
                )
                output = result.stdout if result.returncode == 0 else result.stderr
                self.command_queue.put((
                    self._update_net_activity,
                    f"=== {description} ===\n{output}\n"
                ))
            except Exception as e:
                self.command_queue.put((
                    self._show_error,
                    f"{description} failed: {str(e)}"
                ))
        
        threading.Thread(target=_run, daemon=True).start()

    def _show_error(self, message):
        """Show error message"""
        messagebox.showerror("Error", message, parent=self.root)

    def process_queue(self):
        """Process commands from the queue"""
        while not self.command_queue.empty():
            func, arg = self.command_queue.get()
            func(arg)
        self.root.after(100, self.process_queue)

    def create_windows_ui(self):
        """Create Windows commands tab"""
        # Main container with scrollbar
        container = ttk.Frame(self.windows_frame)
        container.pack(fill='both', expand=True)
        
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Command categories
        categories = [
            {
                "name": "📂 File Operations",
                "commands": [
                    ("List Files", "Get-ChildItem", "List items in current directory"),
                    ("List Files (Detailed)", "Get-ChildItem | Format-Table", "Detailed list with properties"),
                    ("Create Directory", "New-Item -ItemType Directory -Name 'FolderName'", "Make new folder"),
                    ("Delete File", "Remove-Item 'FileName'", "Permanently delete a file"),
                    ("Show File Content", "Get-Content 'FileName'", "Display file contents")
                ]
            },
            {
                "name": "🌐 Network",
                "commands": [
                    ("Show IP Config", "ipconfig", "Display network configuration"),
                    ("Test Connection", "Test-NetConnection google.com", "Check internet connectivity"),
                    ("Flush DNS", "Clear-DnsClientCache", "Clear DNS resolver cache"),
                    ("Show Active Connections", "Get-NetTCPConnection", "List all TCP connections")
                ]
            }
        ]
        
        # Create category sections
        for category in categories:
            frame = ttk.LabelFrame(
                scrollable_frame,
                text=category["name"],
                padding=10
            )
            frame.pack(fill='x', padx=5, pady=5, ipady=5)
            
            for cmd_name, cmd, description in category["commands"]:
                self.create_command_button(frame, cmd_name, cmd, description)

    def create_linux_ui(self):
        """Create Linux commands tab"""
        label = ttk.Label(
            self.linux_frame,
            text="Linux commands will appear here",
            font=("Segoe UI", 12)
        )
        label.pack(pady=50)

    def create_alias_ui(self):
        """Create Aliases tab"""
        label = ttk.Label(
            self.alias_frame,
            text="PowerShell aliases will appear here",
            font=("Segoe UI", 12)
        )
        label.pack(pady=50)

    def create_venv_ui(self):
        """Create Python Virtual Env tab"""
        label = ttk.Label(
            self.venv_frame,
            text="Python virtual environment commands will appear here",
            font=("Segoe UI", 12)
        )
        label.pack(pady=50)

    def create_command_button(self, parent, name, command, description):
        """Create a uniform command button with details"""
        card = ttk.Frame(parent, padding=5)
        card.pack(fill='x', pady=2)
        
        # Command name and description
        ttk.Label(
            card,
            text=name,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor='w')
        
        ttk.Label(
            card,
            text=description,
            font=("Segoe UI", 8)
        ).pack(anchor='w', pady=(0, 5))
        
        # Command with copy button
        cmd_frame = ttk.Frame(card)
        cmd_frame.pack(fill='x')
        
        cmd_label = ttk.Label(
            cmd_frame,
            text=command,
            font=("Consolas", 9),
            foreground="#00BFFF"  # Light blue color for commands
        )
        cmd_label.pack(side='left', fill='x', expand=True)
        
        ttk.Button(
            cmd_frame,
            text="Copy",
            command=lambda c=command: self.copy_command(c),
            width=8
        ).pack(side='right')

    def create_status_bar(self):
        """Create status bar at bottom"""
        status_frame = ttk.Frame(self.main_frame, height=25)
        status_frame.pack(fill='x', pady=(10, 0))
        status_frame.pack_propagate(False)
        
        self.status_var = tk.StringVar(value="Ready")
        
        ttk.Label(
            status_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 8)
        ).pack(side='left', padx=10)
        
        ttk.Label(
            status_frame,
            text="Command Reference Tool v2.0",
            font=("Segoe UI", 8)
        ).pack(side='right', padx=10)

    def copy_command(self, command):
        """Copy command to clipboard"""
        try:
            pyperclip.copy(command)
            self.status_var.set(f"Copied: {command[:50]}...")
        except Exception as e:
            self.status_var.set(f"Copy failed: {str(e)}")

    def start_threat_monitor(self):
        """Start monitoring threat level"""
        self.evaluate_threat_level()
        self.root.after(300000, self.start_threat_monitor)  # Check every 5 minutes

    def evaluate_threat_level(self):
        """Evaluate current threat level"""
        # Placeholder - in real implementation, this would check system status
        threat_score = 0
        
        # Example checks would go here
        # if self._check_suspicious_activity():
        #     threat_score += 30
        
        if threat_score >= 70:
            self._set_threat_level("🔴 CRITICAL", "red")
        elif threat_score >= 40:
            self._set_threat_level("🟠 HIGH", "orange")
        elif threat_score >= 20:
            self._set_threat_level("🟡 ELEVATED", "yellow")
        else:
            self._set_threat_level("🟢 NORMAL", "green")

    def _set_threat_level(self, text, color):
        """Update threat level display"""
        self.threat_level.config(text=f"THREAT LEVEL: {text}", foreground=color)
        self.status_var.set(f"Threat level: {text}")

if __name__ == "__main__":
    # Initialize the application
    root = ttk.Window()
    root.style.theme_use("cyborg")  # Set the dark theme
    app = ModernCommandReferenceTool(root)
    root.mainloop()
