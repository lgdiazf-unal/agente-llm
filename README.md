# LLM Memory Lab

Framework experimental para construir un agente LLM con memoria persistente modular.

El proyecto implementa diferentes tipos de memoria de largo plazo y las integra automáticamente dentro del contexto enviado al modelo de lenguaje.

---

# Versión

## v1.0.0 — Procedural Memory

Estado actual:

- ✅ Episodic Memory
- ✅ Semantic Memory
- ✅ Procedural Memory
- ✅ Context Assembly modular
- ✅ Persistencia en JSON
- ✅ CREATE / UPDATE mediante LLM

---

# Objetivo

LLM Memory Lab busca construir un agente con memoria persistente, donde cada tipo de memoria tenga una responsabilidad claramente definida y pueda evolucionar de forma independiente.

Actualmente el agente dispone de tres sistemas de memoria de largo plazo.

---

# Tipos de memoria

## Episodic Memory

Representa experiencias.

Responde la pregunta:

> ¿Qué ocurrió?

Ejemplo:

```
El usuario implementó un sistema de memoria para agentes LLM.
```

---

## Semantic Memory

Representa conocimiento.

Responde la pregunta:

> ¿Qué sabe el agente?

Ejemplo:

```
El usuario desarrolla aplicaciones en Python.
```

---

## Procedural Memory

Representa procedimientos.

Responde la pregunta:

> ¿Cómo realizar una tarea?

Ejemplo:

```
Cómo crear un nuevo tipo de memoria.

1. Crear el modelo.
2. Crear el repositorio.
3. Crear el extractor.
4. Crear el matcher.
5. Crear el manager.
6. Crear el retriever.
7. Integrarlo al ContextAssembler.
8. Integrarlo al Agent.
```

---

# Arquitectura

Cada tipo de memoria implementa exactamente el mismo patrón.

```
Memory

    ├── Model
    │
    ├── Extractor
    │
    ├── Matcher
    │
    ├── Manager
    │
    ├── Repository
    │
    └── Retriever
```

Esto permite agregar nuevos tipos de memoria sin modificar la arquitectura existente.

---

# Flujo general

```
                Usuario
                    │
                    ▼

             Conversation

                    │
                    ▼

          ContextAssembler

                    │
     ┌──────────────┼──────────────┐
     │              │              │
     ▼              ▼              ▼

 Episodic      Semantic      Procedural
 Retriever     Retriever      Retriever

     │              │              │
     └──────────────┼──────────────┘
                    │
                    ▼

            PromptContext

                    │
                    ▼

            PromptBuilder

                    │
                    ▼

                  LLM

                    │
                    ▼

          Assistant Response

                    │
                    ▼

       Memory Extraction

     ┌──────────────┼──────────────┐
     │              │              │
     ▼              ▼              ▼

 Episode      Semantic      Procedure
 Extractor     Extractor     Extractor

     │              │              │
     ▼              ▼              ▼

 Episode      Semantic      Procedural
 Manager       Manager        Manager

     │              │              │
     ▼              ▼              ▼

 Episode      Semantic      Procedural
 Repository    Repository    Repository
```

---

# Componentes implementados

## Episodic Memory

```
Episode
EpisodeExtractor
EpisodeMatcher
EpisodeManager
EpisodeRepository
EpisodeRetriever
```

---

## Semantic Memory

```
Fact
SemanticExtractor
SemanticMatcher
SemanticManager
SemanticRepository
SemanticRetriever
```

---

## Procedural Memory

```
Procedure
ProceduralExtractor
ProceduralMatcher
ProceduralManager
ProceduralRepository
ProceduralRetriever
```

---

# Persistencia

Cada memoria utiliza un archivo independiente.

```
data/

episodes.json

semantic_memory.json

procedures.json
```

---

# Gestión de memoria

Cada manager sigue el mismo flujo.

```
Candidate Memory
        │
        ▼

Matcher (LLM)

        │

 ┌──────┴──────┐

CREATE      UPDATE

 │             │

 ▼             ▼

save()     update()
```

El LLM decide si el nuevo elemento representa una memoria completamente nueva o una actualización de una memoria existente.

---

# Recuperación de memoria

Antes de enviar un prompt al LLM, el agente recupera información desde las memorias persistentes.

Actualmente:

- EpisodicRetriever
- SemanticRetriever
- ProceduralRetriever

La primera implementación recupera todos los elementos almacenados.

En versiones posteriores se implementará recuperación por relevancia.

---

# ContextAssembler

El ContextAssembler centraliza la construcción del contexto.

Genera automáticamente bloques como:

```
==============================

SEMANTIC MEMORY

==============================

- ...

==============================

EPISODIC MEMORY

==============================

- ...

==============================

PROCEDURAL MEMORY

==============================

- ...
```

Posteriormente estos bloques son enviados al PromptBuilder.

---

# PromptBuilder

El PromptBuilder únicamente transforma un PromptContext en mensajes compatibles con el modelo.

No conoce ningún tipo específico de memoria.

Esto permite incorporar nuevas memorias sin modificar el PromptBuilder.

---

# JSON Parser

Todas las respuestas estructuradas del LLM son procesadas mediante:

```
utils/json_parser.py
```

Su responsabilidad es:

- eliminar bloques ```json
- extraer el JSON
- convertirlo a objetos Python

Actualmente es utilizado por:

- Extractors
- Matchers

---

# Comandos disponibles

## exit

Finaliza la aplicación.

---

## /memorize

Fuerza la extracción y almacenamiento de memoria.

---

## /episodes

Muestra la memoria episódica almacenada.

---

## /help

Lista los comandos disponibles.

---

# Estructura del proyecto

```
src/
└── memory_lab/

    ├── agent.py

    ├── models/
    │
    │   ├── conversation.py
    │   ├── context_block.py
    │   ├── episode.py
    │   ├── fact.py
    │   ├── procedure.py
    │   └── prompt_context.py

    ├── repositories/
    │
    │   ├── episode_repository.py
    │   ├── semantic_repository.py
    │   └── procedural_repository.py

    ├── services/
    │
    │   ├── context_assembler.py
    │   │
    │   ├── episode_extractor.py
    │   ├── episode_matcher.py
    │   ├── episode_manager.py
    │   ├── episode_retriever.py
    │   │
    │   ├── semantic_extractor.py
    │   ├── semantic_matcher.py
    │   ├── semantic_manager.py
    │   ├── semantic_retriever.py
    │   │
    │   ├── procedural_extractor.py
    │   ├── procedural_matcher.py
    │   ├── procedural_manager.py
    │   └── procedural_retriever.py

    ├── prompts/
    │
    │   ├── chat_prompt.py
    │   ├── episode_prompt.py
    │   ├── semantic_prompt.py
    │   ├── procedural_prompt.py
    │   └── procedural_matcher_prompt.py

    ├── utils/
    │
    │   ├── conversation_formatter.py
    │   ├── episode_formatter.py
    │   ├── procedure_formatter.py
    │   ├── semantic_formatter.py
    │   ├── json_parser.py
    │   └── printer.py

    ├── views/

    └── llm.py
```

---

# Principios del proyecto

- Arquitectura modular.
- Cada memoria es independiente.
- Persistencia transparente mediante JSON.
- Cambios incrementales por versión.
- El LLM toma las decisiones cognitivas.
- Python controla la ejecución y la persistencia.
- El PromptBuilder permanece desacoplado de los tipos de memoria.

---

# Roadmap

## v1.1.0

Terminal UI

Objetivo:

Mejorar completamente la experiencia de uso en consola.

Incluye:

- Paneles.
- Colores.
- Tablas.
- Árboles.
- Separadores.
- Mejor visualización del prompt.
- Mejor visualización de la memoria recuperada.
- Estadísticas de tokens.
- Flujo visual más claro.

No modifica la lógica del agente.

---

## Versionado

El proyecto utiliza **Semantic Versioning**.

```
MAJOR.MINOR.PATCH
```

Donde:

- **MAJOR** → cambios incompatibles o hitos importantes.
- **MINOR** → nuevas funcionalidades compatibles.
- **PATCH** → correcciones de errores.

Versión actual:

```
v1.0.0
```