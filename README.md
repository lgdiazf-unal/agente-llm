# Roadmap

El proyecto sigue Versionado Semántico (SemVer).

Formato:

MAJOR.MINOR.PATCH

- MAJOR → Cambios importantes de arquitectura o nuevas generaciones del sistema.
- MINOR → Nuevas funcionalidades compatibles.
- PATCH → Correcciones y mejoras sin cambios funcionales.

---

# Serie 0.x

Corresponde a la etapa experimental del framework.

## v0.1

- Infraestructura base.
- Cliente LLM.
- Conversación.
- Prompt básico.

---

## v0.2

- Modelos principales.
- Persistencia inicial.
- Organización del proyecto.

---

## v0.3

- Reestructuración interna.
- Separación por servicios.
- Repositorios.

---

## v0.4

- Mejoras arquitectónicas.
- Limpieza del flujo.
- Preparación para memoria.

---

## v0.5

- Primer Prompt Builder.
- Contexto de conversación.
- Flujo completo Agent → LLM.

---

## v0.6

### Episodic Memory

Se incorpora la primera memoria persistente.

Incluye:

- Episode
- EpisodeExtractor
- EpisodeRepository
- EpisodeRetriever
- Recuperación automática.

---

## v0.7

### Episodic Memory Management

La memoria deja de ser únicamente persistente y pasa a ser administrada.

Incluye:

- EpisodeManager
- EpisodeMatcher
- CREATE
- UPDATE
- Actualización automática mediante LLM.

---

## v0.8

### Semantic Memory

Se incorpora un segundo sistema de memoria.

Incluye:

- Fact
- SemanticExtractor
- SemanticRepository
- SemanticRetriever
- SemanticManager
- SemanticMatcher
- CREATE / UPDATE
- Recuperación automática.
- Integración con PromptBuilder.

---

## v0.9

### Context Assembly

La construcción del contexto deja de depender del Agent.

Incluye:

- ContextAssembler
- ContextBlock
- PromptContext desacoplado
- PromptBuilder genérico
- Arquitectura extensible para nuevos tipos de memoria.

---

# Serie 1.x

Corresponde a la primera arquitectura completa de memoria.

## v1.0

### Procedural Memory

Se incorpora el tercer tipo de memoria.

Objetivo:

Permitir que el agente aprenda procedimientos, instrucciones y secuencias de acciones reutilizables.

Componentes previstos:

- Procedure
- ProceduralExtractor
- ProceduralRepository
- ProceduralRetriever
- ProceduralManager
- ProceduralMatcher

Integración automática mediante ContextAssembler.

---

## v1.1

### Context Selection

Introducción del ContextSelector.

Responsabilidades:

- limitar tamaño del contexto
- seleccionar recuerdos relevantes
- controlar presupuesto de tokens
- preparar el contexto para el PromptBuilder

---

## v1.2

### Retrieval Strategies

Nuevos mecanismos de recuperación.

Ejemplos:

- Top-K
- Similaridad semántica
- Scoring híbrido
- Recencia
- Frecuencia
- Importancia

---

## v1.3

### Memory Consolidation

Optimización de la memoria.

Incluye:

- consolidación
- deduplicación
- fusión automática
- olvido controlado
- compresión de recuerdos

---

## v1.4

### Memory Importance

Cada recuerdo tendrá una importancia explícita.

Permitirá:

- priorizar recuerdos
- proteger recuerdos importantes
- mejorar la recuperación

---

## v1.5

### Temporal Memory

Se incorpora información temporal.

Ejemplos:

- última utilización
- fecha de creación
- frecuencia
- historial de modificaciones

---

# Serie 2.x

Segunda generación del framework.

En esta etapa la arquitectura estará orientada a agentes autónomos.

Objetivos:

- planificación
- reflexión
- memoria jerárquica
- aprendizaje continuo
- herramientas
- múltiples agentes
- razonamiento de largo plazo