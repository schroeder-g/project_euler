import time

from fun_with_words.wordling import PREVIOUS_ANSWERS, get_partial_wordle_solutions
from utilities.generate_prettified_sublists import generate_enumerated_sublists
from utilities.terminalprint import ts
from utilities.clear_terminal import clear

# region Texts
intro = (
    "\n     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
    "   ░░░░░░░░░░░░░░░████████╗██╗░░██╗███████╗░░░░░░░░░░░░░░░░ \n"
    "  ░░░░░░░░░░░░░░░░╚══██╔══╝██║░░██║██╔════╝░░░░░░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░░░░░░░░░██║░░░███████║█████╗░░░░░░░░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░░░░░░░░░██║░░░██╔══██║██╔══╝░░░░░░░░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░░░░░░░░░██║░░░██║░░██║███████╗░░░░░░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░░░░░░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
    "  ░░░"
    + ts.colorize(*ts.get_color("mint"), "██╗")
    + "░░░░░░░"
    + ts.colorize(*ts.get_color("mint"), "██╗")
    + "░"
    + ts.colorize(*ts.get_color("gold"), "█████╗")
    + "░"
    + ts.colorize(*ts.get_color("mint"), "██████╗")
    + "░"
    + ts.colorize(*ts.get_color("mint"), "██████╗")
    + "░"
    + ts.colorize(*ts.get_color("mint"), "██╗")
    + "░░░░░"
    + ts.colorize(*ts.get_color("mint"), "███████╗")
    + "░░\n"
    "  ░░░"
    + ts.colorize(*ts.get_color("mint"), "██║")
    + "░░"
    + ts.colorize(*ts.get_color("mint"), "██╗")
    + "░░"
    + ts.colorize(*ts.get_color("mint"), "██║")
    + ts.colorize(*ts.get_color("gold"), "██╔══██╗")
    + ts.colorize(*ts.get_color("mint"), "██╔══██╗██╔══██╗██║")
    + "░░░░░"
    + ts.colorize(*ts.get_color("mint"), "██╔════╝")
    + "░░ + \n"
    "  ░░░"
    + ts.colorize(*ts.get_color("mint"), "╚██╗████╗██╔╝")
    + ts.colorize(*ts.get_color("gold"), "██║")
    + "░░"
    + ts.colorize(*ts.get_color("gold"), "██║")
    + ts.colorize(*ts.get_color("mint"), "██████╔╝██║")
    + "░░"
    + ts.colorize(*ts.get_color("mint"), "██║██║")
    + "░░░░░"
    + ts.colorize(*ts.get_color("mint"), "█████╗")
    + "░░░░\n"
    "  ░░░░"
    + ts.colorize(*ts.get_color("mint"), "████╔═████║")
    + "░"
    + ts.colorize(*ts.get_color("gold"), "██║")
    + "░░"
    + ts.colorize(*ts.get_color("gold"), "██║")
    + ts.colorize(*ts.get_color("mint"), "██╔══██╗██║")
    + "░░"
    + ts.colorize(*ts.get_color("mint"), "██║██║")
    + "░░░░░"
    + ts.colorize(*ts.get_color("mint"), "██╔══╝")
    + "░░░░\n"
    "  ░░░░"
    + ts.colorize(*ts.get_color("mint"), "╚██╔╝")
    + "░"
    + ts.colorize(*ts.get_color("mint"), "╚██╔╝")
    + "░"
    + ts.colorize(*ts.get_color("gold"), "╚█████╔╝")
    + ts.colorize(*ts.get_color("mint"), "██║")
    + "░░"
    + ts.colorize(*ts.get_color("mint"), "██║██████╔╝███████╗███████╗")
    + "░░\n"
    "  ░░░░░"
    + ts.colorize(*ts.get_color("mint"), "╚═╝")
    + "░░░"
    + ts.colorize(*ts.get_color("mint"), "╚═╝")
    + "░░░"
    + ts.colorize(*ts.get_color("gold"), "╚════╝")
    + "░"
    + ts.colorize(*ts.get_color("mint"), "╚═╝")
    + "░░"
    + ts.colorize(*ts.get_color("mint"), "╚═╝╚═════╝")
    + "░"
    + ts.colorize(*ts.get_color("mint"), "╚══════╝╚══════╝")
    + "░░\n"
    "  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░░██████╗░███████╗███╗░░██╗██╗███████╗░░░░░░░░░░\n"
    "  ░░░░░░░░░░░██╔════╝░██╔════╝████╗░██║██║██╔════╝░░░░░░░░░░\n"
    "  ░░░░░░░░░░░██║░░██╗░█████╗░░██╔██╗██║██║█████╗░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░██║░░╚██╗██╔══╝░░██║╚████║██║██╔══╝░░░░░░░░░░░░\n"
    "  ░░░░░░░░░░░╚██████╔╝███████╗██║░╚███║██║███████╗░░░░░░░░░░\n"
    "   ░░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝╚══════╝░░░░░░░░░\n"
    "     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
)
help_text = (
    "  Welcome to the Wordle Genie. Let's keep your streak going!\n\n"
    " \u2022" + ' The input for each solution takes a format of "gue*s", '
    "\n   where an asterisk represents a letter you don't know.\n\n"
    " \u2022" + f" After that, enter the letters that are in the word, but you're \n"
    "   not sure where they belong (they're highlighted yellow).\n\n"
    " \u2022" + ' If you need to see this text again, enter "help" in the input.\n\n'
    " \u2022" + ' Enter "quit" or "q" to exit the program.\n\n'
    " \u2022"
    + f' Once you get the answer, input "solved!" to break out. good luck!\n   '
    + "\u23af" * 60
)
# endregion


if __name__ == "__main__":
    clear()
    print(intro)
    print(help_text)
    input(" Hit enter to continue: ")
    time.sleep(0.2)
    clear()

    class Help(BaseException):
        """Exception when user wants to see help text"""

        pass

    class Quit(BaseException):
        """Exception when user wants to leave the program"""

        pass

    class Solved(BaseException):
        """Exception when wordle solved"""

        pass

    def handle_commands(input_):
        if input_ == "solved!":
            raise Solved
        elif input_ in {"help", "h"}:
            raise Help
        elif input_ in {"quit", "q"}:
            raise Quit

    prev_guesses = []
    guess = 2
    while guess <= 6:
        try:
            word = input(
                "\n Enter your last guess, with asterisks for unknown letters: "
            )
            handle_commands(word)

            # Get letters with an uncertain position
            inc = input(
                "\n Now enter the characters that are in the word, but you don't know where they belong: "
            )
            handle_commands(inc)
            while len(inc) + len(list(filter(lambda l: l != "*", word))) > 5:
                print(
                    "There can only be so many letters in your word. Make sure the letters "
                )

            # Get guessed letters that aren't a part of the solution
            exc = input("\n What letters aren't in the word? ")
            while any([l in word + inc for l in exc]):
                exc = input(
                    "We can only exclude letters that aren't a part of the word"
                )
            handle_commands(exc)

            # Find possible solutions
            sols = get_partial_wordle_solutions(word, excluded=exc, included=inc)
            if len(sols) > 0:
                shown = "are the top ten:" if len(sols) > 10 else "they are:"
                print(f"\n\n There are {len(sols)} possible solutions. Here {shown}")
            else:
                print(
                    "\n\nSorry, there don't seem to be any possible solutions for "
                    "the given inputs. Try a different word."
                )
                guess -= 1
                continue

            sol_gen = generate_enumerated_sublists(sols, 10)
            while True:
                try:
                    print("\n" + ts.colorize(*ts.get_color("gold"), next(sol_gen)))
                    if not input(
                        '\n Hit enter to move on to guessing. Type "more", or "c" for more solutions: '
                    ):
                        break
                except StopIteration:
                    break

            prev_guesses.append(word)
            guess += 1

        # region handle exceptions
        except Help:
            clear()
            print("\n", help_text, "\n")
        except Solved:
            if not len(prev_guesses) or "*" in prev_guesses[-1]:
                PREVIOUS_ANSWERS.append(input(" Enter the solution! "))
            else:
                PREVIOUS_ANSWERS.append(prev_guesses[-1])
            print(" Congrats on the win, smarty pants ;p")
            sleep(0.9)
            clear()
            break
        except Quit:
            clear()
            break
        # endregion
