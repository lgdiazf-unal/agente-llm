from memory_lab.models.prompt_context import PromptContext


class PromptBuilder:
    """
    Construye la conversación que será enviada al modelo.
    """

    def __init__(self) -> None:

        self.system_prompt = (
            "Eres un asistente útil y preciso."
        )

    def build(
        self,
        context: PromptContext,
    ) -> list[dict]:

        messages: list[dict] = []

        # System Prompt
        messages.append(
            {
                "role": "system",
                "content": self.system_prompt,
            }
        )

        # Working Memory (Conversation)
        for message in context.messages:

            messages.append(
                {
                    "role": message.role,
                    "content": message.content,
                }
            )

        return messages