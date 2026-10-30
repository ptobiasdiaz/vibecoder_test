# Prueba de bootstrap de vibecoder

Proyecto mínimo para validar el flujo de bootstrap de vibecoder. Incluye una función `sumar(a, b)` y una prueba unitaria con la biblioteca estándar.

## Requisitos

Python 3.11 o posterior. No requiere instalación ni dependencias de terceros, servicios externos o base de datos.

## Estructura

- `src/bootstrap.py`: función de ejemplo.
- `tests/test_bootstrap.py`: prueba con `unittest`.
- `doc/alcance.md`: alcance y decisiones para usuarios y desarrolladores.
- `.vibecoder/`: contexto operativo y memoria versionada.
- `AGENTS.md`: reglas globales para agentes.

## Ejecutar la prueba

Desde la raíz del proyecto, en una terminal compatible con POSIX:

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -v
```

La opción `-B` evita crear cachés de bytecode. La ejecución debe completar una prueba correctamente.
