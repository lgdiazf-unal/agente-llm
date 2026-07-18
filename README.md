# Memory Lab

Proyecto educativo para comprender cómo funciona la memoria en un agente basado en LLM, implementando cada tipo de memoria desde cero, sin utilizar frameworks como LangChain o LlamaIndex.

El objetivo es visualizar todo el flujo interno del agente:

- Construcción del prompt.
- Recuperación de memoria.
- Llamadas al LLM.
- Actualización de memoria.
- Evolución de la arquitectura paso a paso.

---

# Objetivos

- Comprender cómo funciona un agente con memoria.
- Implementar cada componente manualmente.
- Mantener una arquitectura simple y fácilmente extensible.
- Visualizar completamente cada etapa del procesamiento.

---

# Roadmap

## v0.1

- Cliente OpenRouter.
- Primera llamada al LLM.

---

## v0.2

- Conversación.
- Historial de mensajes.

---

## v0.3

- PromptBuilder.
- Separación de responsabilidades.

---

## v0.4

- Memoria episódica manual.
- Persistencia en JSON.

---

## v0.5

- Recuperación de memoria episódica.
- EpisodicRetriever.
- Inclusión de recuerdos en el prompt.

---

## v0.6

Refactorización del PromptBuilder.

Se separó la construcción del prompt en bloques independientes.

Componentes:

- SystemBlock
- ConversationBlock
- EpisodicMemoryBlock
- PromptBuilder

---

## v0.7

Gestión automática de la memoria episódica.

El agente ya no depende del comando `/memorize` para almacenar recuerdos.

Al finalizar cada conversación:

1. Se extrae un episodio.
2. Se analiza la memoria existente.
3. El sistema decide si:
   - crear un nuevo episodio (`CREATE`)
   - actualizar un episodio existente (`UPDATE`)
4. Se actualiza automáticamente la memoria.

### Componentes incorporados

- EpisodeManager
- EpisodeMatcher

### Flujo

```text
Usuario
    │
    ▼
Conversation
    │
    ▼
EpisodeRetriever
    │
    ▼
PromptBuilder
    │
    ▼
LLM
    │
    ▼
Conversation
    │
    ▼
EpisodeExtractor
    │
    ▼
EpisodeManager
    │
    ▼
EpisodeMatcher
    │
    ├── CREATE
    │       │
    │       ▼
    │   EpisodeRepository.save()
    │
    └── UPDATE
            │
            ▼
    EpisodeRepository.update()
```

### EpisodeExtractor

Responsable de convertir una conversación completa en un episodio resumido utilizando el LLM.

Entrada:

- Conversation

Salida:

- Episode

---

### EpisodeMatcher

Responsable de decidir si un episodio debe crearse o actualizar uno existente.

Entrada:

- Episodios existentes
- Episodio candidato

Utiliza el LLM para tomar la decisión.

---

### Prompt del EpisodeMatcher

El LLM recibe:

- Lista de episodios existentes.
- Episodio candidato.

Debe responder únicamente un JSON.

CREATE

```json
{
    "action": "create"
}
```

UPDATE

```json
{
    "action": "update",
    "episode_id": "<episode_id>"
}
```

---

### EpisodeManager

Coordina toda la gestión de memoria episódica.

Responsabilidades:

- Invocar el EpisodeMatcher.
- Ejecutar CREATE.
- Ejecutar UPDATE.

---

### EpisodeRepository

Ahora soporta:

- load_all()
- save()
- update()
- clear()

---

# Arquitectura actual

```text
Agent
 │
 ├── Conversation
 │
 ├── PromptBuilder
 │
 ├── EpisodeRetriever
 │
 ├── EpisodeExtractor
 │
 ├── EpisodeManager
 │      │
 │      ▼
 │  EpisodeMatcher
 │
 └── EpisodeRepository
```

---

# Estructura del proyecto

```text
memory_lab/

├── agent.py
├── llm.py
├── prompt_builder.py
│
├── models/
│   ├── conversation.py
│   ├── episode.py
│   └── prompt_context.py
│
├── prompts/
│   ├── episode_prompt.py
│   └── episode_matcher_prompt.py
│
├── repositories/
│   └── episode_repository.py
│
├── services/
│   ├── episode_extractor.py
│   ├── episode_manager.py
│   ├── episode_matcher.py
│   └── episode_retriever.py
│
├── views/
│
├── utils/
│
└── data/
    └── episodes.json
```

---

# Estado actual

Actualmente el laboratorio implementa:

- Conversación.
- Prompt Builder.
- Memoria episódica.
- Recuperación de episodios.
- Extracción automática de episodios.
- Gestión automática de episodios.
- Decisión CREATE / UPDATE mediante LLM.

---

# Próxima versión

## v0.8

Memoria semántica.

Se incorporará una segunda memoria permanente que almacenará conocimiento consolidado derivado de múltiples episodios, manteniendo separadas la memoria episódica y la memoria semántica.