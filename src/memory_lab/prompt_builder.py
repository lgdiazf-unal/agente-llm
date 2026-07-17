from memory_lab.models.prompt_context import PromptContext


class PromptBuilder:

    def __init__(self):

        self.system_prompt = (
            "Eres un asistente útil y preciso."
        )

    def build(
        self,
        context: PromptContext,
    ) -> list[dict]:

        messages = []

        messages.append(
            {
                "role": "system",
                "content": self.system_prompt,
            }
        )

        messages.append(
            {
                "role": "user",
                "content": context.user_message,
            }
        )

        return messages