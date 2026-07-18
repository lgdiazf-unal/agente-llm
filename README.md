# Memory Lab

> Un proyecto educativo para comprender cómo funcionan las memorias de un agente basado en LLM, implementando cada componente desde cero y sin utilizar frameworks.

## Objetivo

El objetivo de este proyecto es construir un agente paso a paso para entender cómo funcionan internamente las distintas memorias que utilizan los agentes modernos.

Cada versión agrega una nueva capacidad, manteniendo el código simple y fácil de seguir.

El foco no es construir el mejor agente, sino comprender su funcionamiento.

---

# Principios del proyecto

- Sin frameworks de agentes.
- Código explícito.
- Arquitectura incremental.
- Cada versión es un tag de Git.
- Todo el proceso es visible.
- Fácil de ejecutar en una máquina Ubuntu sin GPU.
- Uso de modelos gratuitos mediante OpenRouter.

---

# Roadmap

| Versión | Objetivo |
|----------|----------|
| v0.1 | Cliente LLM |
| v0.2 | Conversación |
| v0.3 | PromptContext |
| v0.4 | Working Memory |
| v0.5 | Memoria episódica |
| v0.6 | Recuperación de episodios |
| v0.6.1 | Refactor del PromptBuilder utilizando Prompt Sections |
| v0.6.2 | Context Assembler |
| v0.6.3 | Context Renderer |
| v0.7 | Cognitive Pipeline |
| v0.8 | Memoria semántica |
| v0.9 | Memoria procedimental |
| v1.0 | Agente con memorias completas |

---

# Arquitectura actual (v0.6.1)

```
                    Agent
                      │
                      ▼
               Working Memory
                      │
                      ▼
            Episode Retriever
                      │
                      ▼
              PromptContext
                      │
                      ▼
              PromptBuilder
                      │
                      ▼
             Prompt Sections
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 SystemSection EpisodicMemory ConversationSection
                      │
                      ▼
                   Prompt
                      │
                      ▼
                 LLM Service
                      │
                      ▼
                 OpenRouter
```

---

# Flujo de ejecución

```
Usuario

↓

Working Memory

↓

Episode Retriever

↓

PromptContext

↓

PromptBuilder

↓

LLM

↓

Respuesta

↓

Episode Extractor

↓

Episode Repository
```

---

# Estructura del proyecto

```
src/
└── memory_lab/

    agent/

    llm/

    memories/

    models/

    prompts/
    ├── prompt_builder.py
    └── sections/
        ├── base.py
        ├── conversation.py
        ├── episodic_memory.py
        ├── helpers.py
        └── system.py

    repositories/

    services/

    views/
```

---

# Prompt Sections

A partir de la versión **v0.6.1**, el PromptBuilder deja de construir el prompt directamente.

Ahora utiliza un pipeline de secciones independientes.

```
PromptBuilder

↓

SystemSection

↓

EpisodicMemorySection

↓

ConversationSection

↓

Prompt
```

Cada sección es responsable de construir únicamente una parte del prompt.

Todas implementan la misma interfaz.

```python
class PromptSection(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def is_enabled(
        self,
        context,
    ) -> bool:
        ...

    @abstractmethod
    def build(
        self,
        context,
    ) -> str:
        ...
```

Esto permite agregar nuevas memorias sin modificar el PromptBuilder.

Por ejemplo:

```
SystemSection

↓

ProceduralMemorySection

↓

SemanticMemorySection

↓

EpisodicMemorySection

↓

ConversationSection
```

---

# Próximo paso

La siguiente versión eliminará la responsabilidad del PromptBuilder de conocer las distintas memorias.

Se introducirán tres nuevos componentes:

```
Conversation

↓

Context Assembler

↓

Agent Context

↓

Context Renderer

↓

Prompt Factory

↓

Prompt
```

Con esta arquitectura, el agente primero reconstruirá su contexto y solo después construirá el prompt.

---

# Requisitos

- Python 3.12+
- Ubuntu Server
- Cuenta de OpenRouter
- API Key de OpenRouter

---

# Instalación

```bash
git clone https://github.com/<usuario>/memory-lab.git

cd memory-lab

python -m venv .venv

source .venv/bin/activate

pip install -e .
```

---

# Ejecutar

```bash
python main.py
```

---

# Filosofía

Este proyecto intenta mostrar cómo "piensa" un agente.

Cada versión mantiene el código lo más simple posible y evita ocultar la lógica detrás de frameworks.

La idea es que cualquier desarrollador pueda recorrer el historial de Git y comprender cómo evoluciona un agente desde una conversación simple hasta un sistema con memoria de trabajo, memoria episódica, memoria semántica y memoria procedimental.