from solver import CodeMentor
from gui import run_gui

def main():
    print("🧠 Welcome to CodeMentor!")
    user_input = input("📝 Your Problem: ")
    mentor = CodeMentor()
    mentor.solve_problem(user_input)

if __name__ == "__main__":
    # Prefer GUI if available, fallback to CLI if GUI fails or is not desired
    try:
        run_gui()
    except Exception as e:
        print(f"⚠️ GUI could not be started ({e}). Falling back to CLI mode.\n")
        main()