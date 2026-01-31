from knowledge_base import get_suggestions

class CodeMentor:
    def solve_problem(self, problem_text, gui=False):
        """
        Suggests algorithms for the given problem_text.
        :param problem_text: str, the problem description
        :param gui: bool, if True, returns suggestions as a list; otherwise, prints formatted output
        :return: suggestions list if gui=True, else None
        """
        suggestions = get_suggestions(problem_text)
        if gui:
            return suggestions

        if not suggestions:
            print("❌ No suitable algorithms found.")
            return

        print("\n✅ Suggested Algorithms:")
        for algo in suggestions:
            # Use .get to make robust against missing keys, and avoid KeyError
            name = algo.get('name', 'Unnamed Algorithm')
            desc = algo.get('description', 'No description available.')
            code = algo.get('code', '')
            print(f"- {name}: {desc}")
            if code:
                print(f"  🔗 Example Code:\n{code}\n")
            else:
                print("  🔗 Example Code: Not available.\n")