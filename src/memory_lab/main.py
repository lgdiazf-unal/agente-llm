from memory_lab.llm import call_llm


def main():

    print("=" * 70)
    print("LLM MEMORY LAB")
    print("FASE 0")
    print("=" * 70)

    user_prompt = input("\nUsuario: ")

    messages = [
        {
            "role": "user",
            "content": user_prompt,
        }
    ]

    response = call_llm(messages)

    print("\n" + "=" * 70)
    print("RESPUESTA FINAL")
    print("=" * 70)

    print(response)