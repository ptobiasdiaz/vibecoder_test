# Contexto operativo del bootstrap

## Autorización

- Persona autorizante: `@ptobiasdiaz`.
- Evento GitHub: `34735239759`.
- SHA-256 de la especificación aprobada, proporcionado por la autorización: `2cdaf9c38e5507345bca8d98594fee07a9158f40bf2925a311c74bc4f810ccad`.

La especificación aprobada es inmutable. El alcance es un proyecto mínimo Python 3.11 o posterior, sin dependencias de terceros, con `sumar(a, b)` y una prueba `unittest`.

## Configuración Git confirmada como referencia

```json
{
  "authorized_operations": [
    "CREATE_PULL_REQUEST",
    "CREATE_TECHNICAL_BASE",
    "PUBLISH_BOOTSTRAP_BRANCH"
  ],
  "base_branch_exists": false,
  "bootstrap_branch": "vibecoder/bootstrap-cde3be99",
  "confirmation": "confirmed",
  "initialization_strategy": "TECHNICAL_BASE_COMMIT",
  "integration_policy": "HUMAN_REVIEW_MERGE",
  "main_branch": "main",
  "publication_policy": "PULL_REQUEST",
  "repository_id": "3418f06e-d2ef-4a65-b019-7b0e5329356a",
  "schema_version": 1,
  "technical_commit_policy": "CREATE_MINIMAL"
}
```

Esta configuración se conserva como contexto, sin ejecutarla. La tarea actual prohíbe ejecutar Git y publicar. Las operaciones remotas quedan reservadas al orquestador o a una persona autorizada.
