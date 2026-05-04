# =============================================================================
# DCA PRACTICE SIMULATOR - PARTIE 2 : MOTEUR D'EXAMEN
# =============================================================================
# Ce fichier contient uniquement la logique du simulateur.
# Les questions sont importées depuis dca_questions.py
#
# Usage :
#   python dca_simulator.py              -> Examen complet
#   python dca_simulator.py --section Swarm  -> Section spécifique
#   python dca_simulator.py --random 20  -> 20 questions aléatoires
#   python dca_simulator.py --domc-only  -> DOMC uniquement
#   python dca_simulator.py --mcq-only   -> MCQ uniquement
# =============================================================================

import random
import sys
import argparse
from dca_questions import MCQ_QUESTIONS, DOMC_QUESTIONS


# =============================================================================
# HELPERS
# =============================================================================

def print_separator(char="=", width=60):
    print(char * width)

def print_header(title):
    print_separator()
    print(f"  {title}")
    print_separator()

def get_sections(questions):
    return sorted(set(q["section"] for q in questions))


# =============================================================================
# MOTEUR MCQ
# =============================================================================

def run_mcq(questions: list, show_explanations: bool = True) -> int:
    """
    Présente une liste de questions MCQ à l'utilisateur.
    Retourne le nombre de bonnes réponses.
    """
    correct = 0
    total = len(questions)

    for i, item in enumerate(questions, 1):
        print(f"\n[{i}/{total}]  [{item.get('section', '')}]")
        print(f"Q: {item['q']}")
        print()
        for opt in item['opts']:
            print(f"   {opt}")
        print()

        while True:
            user_ans = input("Your answer (A/B/C/D): ").strip().upper()
            if user_ans in ("A", "B", "C", "D"):
                break
            print("  ⚠  Please enter A, B, C or D.")

        if user_ans == item['ans']:
            print("  ✅  Correct!")
            correct += 1
        else:
            print(f"  ❌  Wrong. Correct answer: {item['ans']}")

        if show_explanations and item.get("explanation"):
            print(f"  💡  {item['explanation']}")

    return correct


# =============================================================================
# MOTEUR DOMC
# =============================================================================

def run_domc(questions: list) -> int:
    """
    Présente une liste de questions DOMC à l'utilisateur.
    Dans le format DOMC réel, chaque option est présentée individuellement
    et l'utilisateur indique si elle est correcte ou non.
    Retourne le nombre de questions entièrement correctes.
    """
    correct_questions = 0
    total = len(questions)

    for i, item in enumerate(questions, 1):
        print(f"\n[{i}/{total}]  [{item.get('section', '')}]")
        print(f"Q: {item['q']}")
        print()

        opts = list(item['opts'])
        random.shuffle(opts)

        all_correct = True
        results = []

        for stmt, is_true in opts:
            while True:
                ans = input(f"  ▶  '{stmt}'  —  Correct? (y/n): ").strip().lower()
                if ans in ("y", "n"):
                    break
                print("     ⚠  Please enter y or n.")

            expected = "y" if is_true else "n"
            if ans == expected:
                results.append(("✅", stmt))
            else:
                all_correct = False
                label = "TRUE" if is_true else "FALSE"
                results.append((f"❌ (was {label})", stmt))

        print()
        for icon, stmt in results:
            print(f"    {icon}  {stmt}")

        if all_correct:
            print("\n  ✅  Question fully correct!")
            correct_questions += 1
        else:
            print("\n  ❌  Question incorrect (all options must be right).")

    return correct_questions


# =============================================================================
# AFFICHAGE DES RÉSULTATS
# =============================================================================

def print_results(mcq_score, mcq_total, domc_score, domc_total):
    total_q = mcq_total + domc_total
    total_score = mcq_score + domc_score
    pct = round(total_score / total_q * 100, 1) if total_q > 0 else 0

    print()
    print_separator()
    print("  FINAL RESULTS")
    print_separator()
    if mcq_total > 0:
        mcq_pct = round(mcq_score / mcq_total * 100, 1)
        print(f"  MCQ  : {mcq_score}/{mcq_total}  ({mcq_pct}%)")
    if domc_total > 0:
        domc_pct = round(domc_score / domc_total * 100, 1)
        print(f"  DOMC : {domc_score}/{domc_total}  ({domc_pct}%)")
    print_separator()
    print(f"  OVERALL : {total_score}/{total_q}  ({pct}%)")

    if pct >= 55:
        print("\n  🎉  PASS — You meet the DCA passing threshold (55%)!")
    else:
        gap = 55 - pct
        print(f"\n  📚  Keep studying — you need {gap:.1f}% more to pass.")
    print_separator()


# =============================================================================
# POINT D'ENTRÉE
# =============================================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description="Docker DCA Practice Exam Simulator",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--section", type=str, default=None,
        help="Run only questions from a specific section (e.g. 'Swarm', 'Networking')"
    )
    parser.add_argument(
        "--random", type=int, default=None, metavar="N",
        help="Pick N random MCQ questions instead of the full set"
    )
    parser.add_argument(
        "--mcq-only", action="store_true",
        help="Run MCQ section only"
    )
    parser.add_argument(
        "--domc-only", action="store_true",
        help="Run DOMC section only"
    )
    parser.add_argument(
        "--no-explain", action="store_true",
        help="Hide explanations after each MCQ answer"
    )
    parser.add_argument(
        "--list-sections", action="store_true",
        help="List available sections and exit"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.list_sections:
        sections = get_sections(MCQ_QUESTIONS + DOMC_QUESTIONS)
        print("Available sections:")
        for s in sections:
            print(f"  - {s}")
        sys.exit(0)

    print_header("DOCKER DCA PRACTICE EXAM SIMULATOR")
    print("  Press Ctrl+C at any time to quit.\n")

    # --- Filtrage par section ---
    mcq_pool = MCQ_QUESTIONS
    domc_pool = DOMC_QUESTIONS

    if args.section:
        mcq_pool  = [q for q in MCQ_QUESTIONS  if q.get("section") == args.section]
        domc_pool = [q for q in DOMC_QUESTIONS if q.get("section") == args.section]
        if not mcq_pool and not domc_pool:
            print(f"  ⚠  No questions found for section '{args.section}'.")
            print("  Run with --list-sections to see available sections.")
            sys.exit(1)

    # --- Mode aléatoire ---
    if args.random:
        mcq_pool = random.sample(mcq_pool, min(args.random, len(mcq_pool)))

    # --- Shuffle ---
    random.shuffle(mcq_pool)
    random.shuffle(domc_pool)

    show_explain = not args.no_explain

    mcq_score = mcq_total = 0
    domc_score = domc_total = 0

    try:
        # --- Section MCQ ---
        if not args.domc_only and mcq_pool:
            print_header(f"MCQ SECTION — {len(mcq_pool)} question(s)")
            mcq_score = run_mcq(mcq_pool, show_explanations=show_explain)
            mcq_total = len(mcq_pool)

        # --- Section DOMC ---
        if not args.mcq_only and domc_pool:
            print_header(f"DOMC SECTION — {len(domc_pool)} question(s)")
            domc_score = run_domc(domc_pool)
            domc_total = len(domc_pool)

    except KeyboardInterrupt:
        print("\n\n  Session interrupted by user.")

    print_results(mcq_score, mcq_total, domc_score, domc_total)


if __name__ == "__main__":
    main()
