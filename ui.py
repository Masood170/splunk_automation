import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess


class SplunkAutomationUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Enterprise Splunk Parsing Automation")
        self.root.geometry("1200x750")

        title = tk.Label(
            root,
            text="Enterprise Splunk Parsing Automation Framework",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=15)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        fetch_btn = tk.Button(
            button_frame,
            text="Fetch Real Logs From Splunk",
            width=35,
            height=2,
            bg="lightblue",
            command=self.fetch_logs
        )
        fetch_btn.grid(row=0, column=0, padx=15, pady=15)

        validate_btn = tk.Button(
            button_frame,
            text="Validate Regex Extraction",
            width=35,
            height=2,
            bg="lightgreen",
            command=self.validate_regex
        )
        validate_btn.grid(row=0, column=1, padx=15, pady=15)

        config_btn = tk.Button(
            button_frame,
            text="Generate props.conf & transforms.conf",
            width=35,
            height=2,
            bg="orange",
            command=self.generate_configs
        )
        config_btn.grid(row=1, column=0, padx=15, pady=15)

        pipeline_btn = tk.Button(
            button_frame,
            text="Run Full Parsing Pipeline",
            width=35,
            height=2,
            bg="yellow",
            command=self.run_pipeline
        )
        pipeline_btn.grid(row=1, column=1, padx=15, pady=15)

        clear_btn = tk.Button(
            button_frame,
            text="Clear Output",
            width=35,
            height=2,
            bg="tomato",
            command=self.clear_output
        )
        clear_btn.grid(row=2, column=0, columnspan=2, pady=15)

        self.output_box = ScrolledText(
            root,
            width=150,
            height=30,
            font=("Consolas", 10)
        )

        self.output_box.pack(padx=10, pady=10)

    def run_command(self, command):

        self.output_box.insert(tk.END, f"\nRunning: {command}\n\n")

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.stdout:
            self.output_box.insert(tk.END, result.stdout)

        if result.stderr:
            self.output_box.insert(tk.END, result.stderr)

        self.output_box.insert(tk.END, "\n" + "=" * 100 + "\n")

        self.output_box.see(tk.END)

    def fetch_logs(self):

        self.run_command("python splunk_log_fetcher.py")

    def validate_regex(self):

        self.run_command("python validators/regex_validator.py")

    def generate_configs(self):

        self.run_command("python generators/transforms_generator.py")

        self.run_command("python generators/props_generator.py")

    def run_pipeline(self):

        self.output_box.delete(1.0, tk.END)

        commands = [

            "python splunk_log_fetcher.py",

            "python generators/transforms_generator.py",

            "python generators/props_generator.py",

            "python validators/regex_validator.py"
        ]

        for cmd in commands:

            self.run_command(cmd)

    def clear_output(self):

        self.output_box.delete(1.0, tk.END)


root = tk.Tk()

app = SplunkAutomationUI(root)

root.mainloop()