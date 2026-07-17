"""
llm.py

Responsabilidad:
    Comunicarse con el modelo LLM a través de OpenRouter.

Entrada:
    messages (list[dict])

Salida:
    Texto generado por el modelo.
"""

from openai import OpenAI

from memory_lab.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    OPENROUTER_MODEL,
)
from memory_lab.utils.printer import (
    print_json,
    print_step,
    print_text,
    print_title,
)


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
)


def call_llm(messages: list[dict]) -> str:
    """
    Envía una conversación al modelo y devuelve la respuesta.

    Parameters
    ----------
    messages:
        Lista de mensajes con el formato esperado por la API.

    Returns
    -------
    str
        Texto generado por el asistente.
    """

    print_step("Construyendo solicitud")

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": messages,
    }

    print_title("PAYLOAD")

    print_json(payload)

    print_step("Enviando solicitud al LLM")

    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=messages,
    )

    print_title("RESPUESTA")

    print_text(f"Modelo: {response.model}")

    if response.usage:
        print_text(f"Prompt tokens     : {response.usage.prompt_tokens}")
        print_text(f"Completion tokens : {response.usage.completion_tokens}")
        print_text(f"Total tokens      : {response.usage.total_tokens}")

    message = response.choices[0].message.content or ""

    print_title("MENSAJE EXTRAÍDO")

    print_text(message)

    return message