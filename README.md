# LLM Memory Lab

Sistema experimental de agente LLM con arquitectura de memoria persistente.

Versión actual:

```text
v1.1.0
```

---

# Objetivo del proyecto

LLM Memory Lab es un laboratorio para construir un agente basado en modelos de lenguaje con capacidad de memoria persistente.

El objetivo principal es implementar una arquitectura donde el agente pueda:

- recordar experiencias pasadas;
- almacenar información permanente;
- aprender procedimientos reutilizables;
- recuperar información relevante antes de responder;
- construir dinámicamente el contexto enviado al LLM.

El proyecto está diseñado con una arquitectura modular donde cada tipo de memoria tiene sus propios componentes de extracción, recuperación, administración y almacenamiento.

---

# Arquitectura general

```text
                         USER
                          |
                          v

                   Conversation

                          |
                          v

                Memory Retrieval Layer

          ┌───────────────┼───────────────┐
          |               |               |
          v               v               v

     Semantic        Episodic        Procedural
      Memory          Memory          Memory

          |               |               |
          └───────────────┼───────────────┘

                          |
                          v

                    Context Blocks

                          |
                          v

                    Prompt Context

                          |
                          v

                    Prompt Builder

                          |
                          v

                         LLM

                          |
                          v

              Memory Extraction Layer

                          |
                          v

                  Memory Update Layer
```

---

# Tipos de memoria implementados

## Memoria episódica

La memoria episódica almacena eventos específicos ocurridos durante una conversación.

Representa experiencias.

Ejemplos:

- decisiones tomadas;
- problemas solucionados;
- conversaciones importantes;
- eventos realizados.

Modelo:

```text
Episode
```

Flujo:

```text
Conversation

      |

EpisodeExtractor

      |

EpisodeManager

      |

EpisodeRepository
```

---

## Memoria semántica

La memoria semántica almacena información estable y conocimiento adquirido.

Representa hechos.

Ejemplos:

- preferencias;
- datos importantes;
- información permanente;
- características del usuario o proyecto.

Modelo:

```text
Fact
```

Flujo:

```text
Conversation

      |

SemanticExtractor

      |

SemanticManager

      |

SemanticRepository
```

---

## Memoria procedimental

La memoria procedimental almacena procedimientos reutilizables.

Representa cómo realizar una tarea.

Ejemplos:

```text
Crear un proyecto FastAPI

Configurar un entorno Python

Ejecutar pruebas del sistema

Realizar un despliegue
```

Modelo:

```text
Procedure
```

Flujo:

```text
Conversation

      |

ProceduralExtractor

      |

ProceduralMatcher

      |

ProceduralManager

      |

ProceduralRepository
```

---

# Context Blocks

A partir de la versión v1.1.0 el sistema utiliza una capa intermedia llamada:

```text
ContextBlock
```

Los tipos de memoria no llegan directamente al PromptBuilder.

Cada memoria se transforma en un bloque genérico.

Ejemplo:

```text
==============================

🧠 SEMANTIC MEMORY

==============================

- El proyecto utiliza Python
- La arquitectura es modular


==============================

📖 EPISODIC MEMORY

==============================

- Se implementó memoria semántica


==============================

⚙ PROCEDURAL MEMORY

==============================

- Crear estructura inicial del proyecto
- Configurar dependencias
```

---

# Ventajas del sistema ContextBlock

Antes:

```text
PromptBuilder

 |
 ├── Episode
 ├── Fact
 └── Procedure
```

Después:

```text
PromptBuilder

        |

   ContextBlock
```

Esto permite agregar nuevos tipos de memoria sin modificar la construcción del prompt.

Ejemplos futuros:

```text
Preference Memory

Goal Memory

Project Memory

Emotional Memory

Task Memory
```

---

# Flujo completo de ejecución

Cada interacción del agente sigue el siguiente ciclo:

```text
1. Usuario envía mensaje

2. Guardar conversación

3. Recuperar memorias existentes

4. Convertir memorias en Context Blocks

5. Construir Prompt

6. Ejecutar LLM

7. Extraer nuevas memorias

8. Ejecutar CREATE / UPDATE

9. Mostrar estadísticas
```

---

# Dashboard de ejecución

La versión v1.1.0 incorpora un sistema de métricas de ejecución.

Ejemplo:

```text
📊 SESSION STATS


Messages        : 4


Retrieved Memory:

  🧠 Semantic    : 3
  📖 Episodic    : 2
  ⚙ Procedural  : 1


Execution:

  Retrieval     : 0.032s
  Prompt Build  : 0.004s
  LLM Call      : 1.832s
  Extraction    : 0.241s


Total Time      : 2.121s
```

Métricas actuales:

- cantidad de mensajes;
- cantidad de memorias recuperadas;
- tiempos de recuperación;
- tiempo de construcción del prompt;
- tiempo del LLM;
- tiempo de extracción.

---

# Estructura del proyecto

```text
src/memory_lab

├── agent.py
├── llm.py
├── prompt_builder.py


├── models

│   ├── conversation.py
│   ├── episode.py
│   ├── fact.py
│   ├── procedure.py
│   ├── context_block.py
│   └── prompt_context.py


├── repositories

│   ├── episode_repository.py
│   ├── semantic_repository.py
│   └── procedural_repository.py


├── services

│   ├── episode_extractor.py
│   ├── episode_manager.py
│   ├── episode_retriever.py
│
│   ├── semantic_extractor.py
│   ├── semantic_manager.py
│   ├── semantic_retriever.py
│
│   ├── procedural_extractor.py
│   ├── procedural_matcher.py
│   ├── procedural_manager.py
│   └── procedural_retriever.py


├── prompts

│   ├── chat_prompt.py
│   ├── semantic_prompt.py
│   ├── episode_prompt.py
│   └── procedural_prompt.py


├── views

│   ├── conversation_view.py
│   ├── prompt_builder_view.py
│   ├── retrieved_memory_view.py
│   └── session_stats_view.py


└── utils

    ├── console.py
    ├── pipeline.py
    └── session_stats.py
```

---

# Comandos disponibles

Ejecutar:

```bash
memory-lab
```

Comandos:

```text
exit

/memorize

/episodes

/stats

/help
```

---

# Ejemplo de interacción

Usuario:

```text
Necesito crear un proyecto FastAPI con arquitectura modular
```

Proceso interno:

```text
1. Buscar memorias relacionadas

2. Recuperar procedimientos existentes

3. Construir contexto:

⚙ PROCEDURAL MEMORY

- Crear estructura inicial
- Configurar dependencias
- Separar servicios
```

Luego:

```text
4. Enviar contexto al LLM

5. Generar respuesta

6. Extraer nuevo procedimiento

7. Actualizar memoria
```

---

# Estado del proyecto

## Implementado en v1.1.0

✅ Conversación persistente

✅ Memoria episódica

✅ Memoria semántica

✅ Memoria procedimental

✅ Extracción automática

✅ Matching CREATE / UPDATE

✅ Recuperación de memoria

✅ Context Builder desacoplado

✅ Arquitectura ContextBlock

✅ Pipeline visual

✅ Dashboard de ejecución

---

# Próxima versión

## v1.2.0 — Memory Quality Layer

Objetivo:

Mejorar la calidad de recuperación y selección de memoria.

Características planeadas:

- ranking de recuerdos;
- score de relevancia;
- prioridad de memoria;
- reducción de ruido;
- límite dinámico de contexto;
- consolidación de recuerdos;
- expiración o decaimiento temporal.

---

# Versionamiento

El proyecto utiliza versionamiento semántico:

```text
MAJOR.MINOR.PATCH
```

Ejemplo:

```text
v1.1.0
```

Significado:

```text
MAJOR

Cambios grandes de arquitectura.


MINOR

Nuevas funcionalidades compatibles.


PATCH

Correcciones y mejoras internas.
```

---

# Historial de versiones

## v1.1.0

Nueva arquitectura de contexto.

Incluye:

- ContextBlock;
- integración de memoria procedimental;
- dashboard de ejecución;
- nueva interfaz terminal.


## v1.0.0

Primera versión estable del sistema de memoria.

Incluye:

- memoria episódica;
- memoria semántica;
- recuperación básica;
- extracción automática.

---

# Licencia

Proyecto experimental de investigación y desarrollo de agentes LLM con memoria persistente.