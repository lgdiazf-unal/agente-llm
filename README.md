# Memory Lab

Memory Lab es un laboratorio para experimentar con arquitecturas de memoria para agentes LLM.

El proyecto implementa tres sistemas de memoria inspirados en la memoria humana:

- Memoria episódica
- Memoria semántica
- Memoria procedimental

Toda la memoria se almacena localmente en archivos JSON y es administrada automáticamente por el agente.

---

# Características

- Conversación persistente
- Extracción automática de memoria
- Recuperación de contexto
- Actualización de memorias existentes
- Panel de memoria recuperada
- Dashboard de sesión
- Pipeline visual
- Arquitectura modular

---

# Tipos de memoria

## Memoria episódica

Almacena eventos ocurridos durante conversaciones.

Ejemplo:

> El usuario comenzó un proyecto de memoria para LLM.

---

## Memoria semántica

Almacena conocimientos permanentes.

Ejemplo:

> El usuario programa en Python.

---

## Memoria procedimental

Almacena procedimientos reutilizables.

Ejemplo:

> Cómo construir un extractor de memoria usando un LLM.

---

# Arquitectura

```
Conversation

        │

        ▼

Memory Retrievers

        │

        ▼

Memory Quality Layer

    Access Tracker
          │
    Decay Service
          │
    Memory Ranker
          │
    Memory Selector

        │

        ▼

Prompt Builder

        │

        ▼

LLM

        │

        ▼

Memory Extractors

        │

        ▼

Memory Managers

        │

        ▼

Repositories
```

---

# Memory Quality Layer (v1.2)

La versión 1.2 introduce una capa encargada de mejorar la calidad de la memoria enviada al modelo.

Actualmente implementa:

- Access Tracker
- Memory Decay
- Memory Ranking
- Memory Selection

Cada memoria mantiene los siguientes metadatos:

- score
- access_count
- created_at
- updated_at
- last_access

---

# Comandos

```
/memorize
```

Extrae memoria manualmente.

```
/episodes
```

Muestra la memoria episódica.

```
/stats
```

Muestra estadísticas de la sesión.

```
/help
```

Lista los comandos disponibles.

```
exit
```

Finaliza la aplicación.

---

# Estructura

```
src/
    models/
    prompts/
    repositories/
    services/
    utils/
    views/

data/
    episodes.json
    facts.json
    procedures.json
```

---

# Estado actual

Versión:

**v1.2.0**

Implementado:

- Memoria episódica
- Memoria semántica
- Memoria procedimental
- Actualización automática de memoria
- Memory Quality Layer
- Dashboard de sesión

---

# Próximas versiones

## v1.3

- Prompt Manager
- Prompts configurables desde archivos
- Cliente LLM con reintentos automáticos
- Configuración desacoplada

## Futuro

- Embeddings
- Recuperación vectorial
- Memoria híbrida
- Compresión de memoria
- Olvido automático
- Memoria de preferencias
- Plugins de memoria
- Base de datos vectorial