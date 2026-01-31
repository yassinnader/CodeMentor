import tkinter as tk
from tkinter import scrolledtext
from solver import CodeMentor

def run_gui():
    mentor = CodeMentor()

    def solve(*_):
        problem = entry.get().strip()
        result_box.config(state=tk.NORMAL)
        result_box.delete("1.0", tk.END)
        if not problem:
            result_box.insert(tk.END, "⚠️ Please enter a problem description.\n")
            result_box.config(state=tk.DISABLED)
            return

        suggestions = mentor.solve_problem(problem, gui = True)
        if not suggestions:
            result_box.insert(tk.END, "❌ No suitable algorithms found.\n")
        else:
            for algo in suggestions:
                name = algo.get('name', 'Unnamed Algorithm')
                desc = algo.get('description', 'No description available.')
                code = algo.get('code', None)
                result_box.insert(tk.END, f"✅ {name}\n")
                result_box.insert(tk.END, f"{desc}\n\n")
                if code:
                    result_box.insert(tk.END, f"{code}\n")
                else:
                    result_box.insert(tk.END, "No code available.\n")
                result_box.insert(tk.END, "-" * 40 + "\n")
        result_box.config(state=tk.DISABLED)

    window = tk.Tk()
    window.title("CodeMentor GUI")
    window.geometry("700x500")
    window.resizable(False, False)

    # Layout
    frame_input = tk.Frame(window, pady=10)
    frame_input.pack(fill=tk.X)

    label = tk.Label(frame_input, text="Describe Your Problem:", anchor="w")
    label.pack(anchor="w", padx=10)

    entry = tk.Entry(frame_input, width=60)
    entry.pack(padx=10, pady=5, fill=tk.X, expand=True)
    entry.focus_set()

    btn = tk.Button(frame_input, text="Get Solution", command=solve)
    btn.pack(padx=10, pady=5, anchor="e")

    # Allow pressing Enter to trigger solution
    entry.bind('<Return>', solve)

    frame_output = tk.Frame(window, pady=10)
    frame_output.pack(fill=tk.BOTH, expand=True)

    result_box = scrolledtext.ScrolledText(frame_output, width=80, height=20, wrap=tk.WORD, state=tk.DISABLED, font=("Consolas", 11))
    result_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    window.mainloop()