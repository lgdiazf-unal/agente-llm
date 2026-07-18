# Memory Lab

Framework experimental para construir agentes LLM con memoria persistente.

El objetivo del proyecto es implementar, de manera incremental, una arquitectura de memoria inspirada en la memoria humana, donde cada versión agrega nuevas capacidades sin modificar la arquitectura base.

---

# Estado actual

Versión actual:

```
v0.8
```

Capacidades implementadas:

- Conversación persistente durante la sesión.
- Memoria episódica.
- Memoria semántica.
- Recuperación automática de memoria.
- Actualización automática mediante LLM.
- Construcción dinámica del prompt.

---

# Arquitectura

```
                User
                  │
                  ▼
            Conversation
                  │
                  ▼
                Agent
                  │
     ┌────────────┴────────────┐
     ▼                         ▼
EpisodeRetriever        SemanticRetriever
     │                         │
     └────────────┬────────────┘
                  ▼
           PromptContext
                  │
                  ▼
           PromptBuilder
                  │
                  ▼
                 LLM
                  │
      ┌───────────┴────────────┐
      ▼                        ▼
EpisodeExtractor      SemanticExtractor
      │                        │
      ▼                        ▼
 EpisodeManager        SemanticManager
      │                        │
      ▼                        ▼
 EpisodeMatcher       SemanticMatcher
      │                        │
      ▼                        ▼
EpisodeRepository   SemanticRepository
```

---

# Componentes

## Conversation

Mantiene el historial completo de la conversación.

---

## PromptBuilder

Construye el prompt enviado al modelo.

Actualmente incluye:

- Semantic Memory
- Episodic Memory
- Current Conversation

---

## Episodic Memory

Representa experiencias completas del agente.

Cada episodio contiene:

```
Episode
    id
    summary
```

Flujo:

```
Conversation
      │
      ▼
EpisodeExtractor
      │
      ▼
Episode
      │
      ▼
EpisodeManager
      │
      ▼
EpisodeMatcher
      │
      ├── CREATE
      └── UPDATE
```

---

## Semantic Memory

Representa conocimiento estable.

Cada hecho contiene:

```
Fact
    id
    content
```

Flujo:

```
Conversation
      │
      ▼
SemanticExtractor
      │
      ▼
Fact
      │
      ▼
SemanticManager
      │
      ▼
SemanticMatcher
      │
      ├── CREATE
      └── UPDATE
```

---

# Persistencia

La memoria se almacena en formato JSON.

```
data/

    episodes.json

    facts.json
```

---

# Recuperación

Antes de construir el prompt el agente recupera:

```
Conversation
      │
      ├── EpisodeRetriever
      │
      └── SemanticRetriever
```

Ambos resultados son incorporados al `PromptContext`.

---

# Prompt

El prompt enviado al LLM tiene la siguiente estructura:

```
SEMANTIC MEMORY

...

EPISODIC MEMORY

...

CURRENT CONVERSATION

...
```

---

# Gestión automática de memoria

Después de cada respuesta del asistente se ejecuta automáticamente:

```
Conversation
      │
      ▼
EpisodeExtractor
      │
      ▼
EpisodeManager

Conversation
      │
      ▼
SemanticExtractor
      │
      ▼
SemanticManager
```

No es necesario ejecutar comandos manuales para mantener la memoria.

---

# Matching mediante LLM

La decisión CREATE / UPDATE es realizada por el modelo.

## Episodios

Entrada:

- Episodios existentes.
- Episodio candidato.

Salida:

```json
{
    "action": "create"
}
```

o

```json
{
    "action": "update",
    "episode_id": "<id>"
}
```

---

## Hechos

Entrada:

- Facts existentes.
- Fact candidato.

Salida:

```json
{
    "action": "create"
}
```

o

```json
{
    "action": "update",
    "fact_id": "<id>"
}
```

---

# Versiones

## v0.6

- Memoria episódica.
- Recuperación de episodios.

---

## v0.7

- CREATE / UPDATE para memoria episódica.
- EpisodeMatcher.
- EpisodeManager.

---

## v0.8

- Memoria semántica.
- SemanticExtractor.
- SemanticRetriever.
- SemanticManager.
- SemanticMatcher.
- Persistencia de hechos.
- Prompt con memoria episódica y semántica.

---

# Próxima versión

## v0.9

Objetivo:

Introducir un **Context Assembler** encargado de seleccionar y ensamblar el contexto antes de construir el prompt.

Esto permitirá desacoplar la recuperación de memoria del `Agent` y preparar la arquitectura para incorporar nuevos tipos de memoria y estrategias de selección de contexto.