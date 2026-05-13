import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess


class SplunkAutomationUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Splunk Automation Framework")
        self.root.geometry("1000x700")

        title = tk.Label(
            root,
            text="Enterprise Splunk Automation Framework",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        firewall_btn = tk.Button(
            button_frame,
            text="Generate Firewall Logs",
            width=25,
            command=self.generate_firewall_logs
        )
        firewall_btn.grid(row=0, column=0, padx=10, pady=10)

        linux_btn = tk.Button(
            button_frame,
            text="Generate Linux Logs",
            width=25,
            command=self.generate_linux_logs
        )
        linux_btn.grid(row=0, column=1, padx=10, pady=10)

        windows_btn = tk.Button(
            button_frame,
            text="Generate Windows Logs",
            width=25,
            command=self.generate_windows_logs
        )
        windows_btn.grid(row=0, column=2, padx=10, pady=10)

        pan_btn = tk.Button(
            button_frame,
            text="Generate PAN Logs",
            width=25,
            command=self.generate_pan_logs
        )
        pan_btn.grid(row=1, column=0, padx=10, pady=10)

        switch_btn = tk.Button(
            button_frame,
            text="Generate Switch Logs",
            width=25,
            command=self.generate_switch_logs
        )
        switch_btn.grid(row=1, column=1, padx=10, pady=10)

        router_btn = tk.Button(
            button_frame,
            text="Generate Router Logs",
            width=25,
            command=self.generate_router_logs
        )
        router_btn.grid(row=1, column=2, padx=10, pady=10)

        config_btn = tk.Button(
            root,
            text="Generate props.conf & transforms.conf",
            width=40,
            bg="lightblue",
            command=self.generate_configs
        )
        config_btn.pack(pady=10)

        validate_btn = tk.Button(
            root,
            text="Validate Regex Extraction",
            width=40,
            bg="lightgreen",
            command=self.validate_regex
        )
        validate_btn.pack(pady=10)

        pipeline_btn = tk.Button(
            root,
            text="Run Full Automation Pipeline",
            width=40,
            bg="orange",
            command=self.run_pipeline
        )
        pipeline_btn.pack(pady=10)

        self.output_box = ScrolledText(root, width=120, height=25)
        self.output_box.pack(padx=10, pady=10)

    def run_command(self, command):

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        self.output_box.insert(tk.END, result.stdout + "\n")
        self.output_box.see(tk.END)

    def generate_firewall_logs(self):
        self.run_command("python generators/firewall_generator.py")

    def generate_linux_logs(self):
        self.run_command("python generators/linux_generator.py")

    def generate_windows_logs(self):
        self.run_command("python generators/windows_generator.py")

    def generate_pan_logs(self):
        self.run_command("python generators/pan_generator.py")

    def generate_switch_logs(self):
        self.run_command("python generators/switch_generator.py")

    def generate_router_logs(self):
        self.run_command("python generators/router_generator.py")

    def generate_configs(self):

        self.run_command("python generators/transforms_generator.py")
        self.run_command("python generators/props_generator.py")

    def validate_regex(self):

        self.run_command("python validators/regex_validator.py")

    def run_pipeline(self):

        self.output_box.delete(1.0, tk.END)

        commands = [
            "python generators/firewall_generator.py",
            "python generators/linux_generator.py",
            "python generators/windows_generator.py",
            "python generators/pan_generator.py",
            "python generators/switch_generator.py",
            "python generators/router_generator.py",
            "python generators/transforms_generator.py",
            "python generators/props_generator.py",
            "python validators/regex_validator.py"
        ]

        for cmd in commands:
            self.run_command(cmd)


root = tk.Tk()
app = SplunkAutomationUI(root)
root.mainloop()