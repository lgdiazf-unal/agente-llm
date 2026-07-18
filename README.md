# LLM Memory Lab

Proyecto educativo para comprender cómo funcionan las memorias de un agente basado en LLM.

El objetivo **no es construir un framework**, sino implementar desde cero cada uno de los componentes de un agente moderno para entender qué hace cada pieza y por qué existe.

Cada fase del proyecto corresponde a un **tag de Git**, permitiendo recorrer la evolución del agente paso a paso.

---

# Objetivos

* Comprender cómo funciona un agente basado en LLM.
* Implementar cada tipo de memoria desde cero.
* Evitar frameworks para entender toda la arquitectura.
* Visualizar cada paso del procesamiento.
* Mantener una arquitectura limpia y fácil de extender.

---

# Tecnologías

* Python 3.12+
* OpenRouter SDK
* Ubuntu Server
* Modelos gratuitos disponibles en OpenRouter

---

# Filosofía del proyecto

Durante todo el desarrollo seguiremos algunas reglas.

## 1. Un concepto por fase

Cada versión responde una única pregunta.

Por ejemplo:

* ¿Cómo llamar un LLM?
* ¿Cómo construir un prompt?
* ¿Cómo funciona la memoria de trabajo?
* ¿Cómo se genera un episodio?

Nunca mezclaremos varios conceptos nuevos en una misma fase.

---

## 2. Cada clase tiene una única responsabilidad

Ejemplo:

| Clase             | Responsabilidad          |
| ----------------- | ------------------------ |
| Conversation      | Mantener la conversación |
| PromptBuilder     | Construir el prompt      |
| EpisodeExtractor  | Generar un episodio      |
| EpisodeRepository | Persistir episodios      |

---

## 3. El dominio no conoce la infraestructura

Los modelos del dominio (`Conversation`, `Message`, `Episode`) nunca conocen:

* OpenRouter
* JSON
* SQLite
* Embeddings

Esas responsabilidades pertenecen a otras capas.

---

# Arquitectura actual

```text
                Usuario
                   │
                   ▼
             Conversation
                   │
                   ▼
            PromptContext
                   │
                   ▼
            PromptBuilder
                   │
                   ▼
              messages[]
                   │
                   ▼
                OpenRouter
                   │
                   ▼
               Respuesta
                   │
                   ▼
            Conversation
                   │
                   ▼
           EpisodeExtractor
                   │
                   ▼
                Episode
```

---

# Estructura del proyecto

```text
memory-lab/
│
├── pyproject.toml
├── README.md
│
├── src/
│   └── memory_lab/
│       │
│       ├── models/
│       │   ├── conversation.py
│       │   ├── episode.py
│       │   ├── message.py
│       │   └── prompt_context.py
│       │
│       ├── prompts/
│       │   ├── chat_prompt.py
│       │   └── episode_prompt.py
│       │
│       ├── services/
│       │   └── episode_extractor.py
│       │
│       ├── utils/
│       │   ├── conversation_formatter.py
│       │   └── printer.py
│       │
│       ├── views/
│       │   ├── conversation_view.py
│       │   └── prompt_builder_view.py
│       │
│       ├── llm.py
│       ├── prompt_builder.py
│       └── main.py
│
└── .env
```

---

# Flujo de ejecución

Cada interacción sigue exactamente el mismo ciclo.

```text
Usuario

↓

Actualizar Conversation

↓

Construir PromptContext

↓

PromptBuilder

↓

Enviar al LLM

↓

Respuesta

↓

Actualizar Conversation
```

Cuando el usuario ejecuta:

```text
/memorize
```

se inicia un segundo flujo.

```text
Conversation

↓

EpisodeExtractor

↓

LLM

↓

Episode
```

---

# Estado actual

## ✅ Working Memory

Actualmente la memoria de trabajo corresponde a la conversación completa.

Cada nuevo mensaje del usuario y del asistente se agrega a `Conversation`.

Antes de cada llamada al modelo, toda la conversación se vuelve a enviar.

Esto permite observar que el LLM **no recuerda por sí mismo**; es el agente quien reconstruye el contexto en cada petición.

---

## ✅ Episode Extraction

Es posible generar un episodio a partir de la conversación mediante el comando:

```text
/memorize
```

El extractor utiliza un prompt distinto al del asistente para convertir la conversación en un único recuerdo resumido.

Todavía los episodios **no se almacenan**.

---

# Roadmap

## v0.1

Comunicación con un LLM.

---

## v0.2

Prompt Builder.

---

## v0.3

Working Memory.

---

## v0.4

Extracción de memoria episódica.

---

## v0.5

Persistencia de episodios.

---

## v0.6

Memoria semántica.

---

## v0.7

Recuperación semántica.

---

## v0.8

Memoria procedimental.

---

## v0.9

Administrador de memorias.

---

## v1.0

Agente completo.

---

# Próxima fase

La siguiente etapa incorporará la persistencia de episodios.

El flujo será:

```text
Conversation

↓

EpisodeExtractor

↓

Episode

↓

EpisodeRepository

↓

episodes.json
```

A partir de ese momento el agente comenzará a construir una memoria de largo plazo.
