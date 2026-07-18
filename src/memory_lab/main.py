"""
main.py

Punto de entrada de la aplicación.
"""

from memory_lab.agent import Agent


def main() -> None:

    agent = Agent()

    agent.run()


if __name__ == "__main__":
    main()