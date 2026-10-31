# Estrategia de pruebas

Las pruebas de `sumar(a, b)` están en `tests/test_bootstrap.py`, en la clase
`SumarTest`. Usan `unittest` de la biblioteca estándar y comparan el resultado
de cada llamada con un valor esperado explícito mediante `assertEqual`.
Requieren Python 3.11 o posterior, sin dependencias de terceros ni instalación
del proyecto.

## Cobertura integrada

La integración de `tests-sumar` se acredita mediante el merge
`c3aa9b2e910593c2d3cd40d2d5a6712ef2b439ed` proporcionado por el orquestador.
El archivo de pruebas presente contiene estos ocho casos:

| Prueba | Argumentos | Resultado esperado |
| --- | --- | --- |
| `test_suma_dos_enteros` | `2, 3` | `5` |
| `test_suma_dos_ceros` | `0, 0` | `0` |
| `test_suma_cero_y_positivo` | `0, 5` | `5` |
| `test_suma_positivo_y_cero` | `5, 0` | `5` |
| `test_suma_dos_negativos` | `-2, -3` | `-5` |
| `test_suma_negativo_y_positivo` | `-2, 3` | `1` |
| `test_suma_positivo_y_negativo` | `3, -2` | `1` |
| `test_suma_enteros_grandes` | `10**12, 10**12` | `2 * 10**12` |

Estos ejemplos cubren enteros positivos, cero en ambas posiciones, dos
negativos, signos mixtos en ambos órdenes y enteros grandes. No constituyen
una comprobación exhaustiva: no hay casos para otros tipos de datos, entradas
inválidas ni todas las combinaciones de enteros.

## Ejecución

Desde la raíz del proyecto, en una terminal compatible con POSIX:

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -v
```

`PYTHONPATH=src` permite importar `bootstrap`; `discover` busca las pruebas en
`tests/` y `-v` muestra cada caso. La opción `-B` evita generar cachés de
bytecode. Se espera que se descubran ocho pruebas y que todas pasen.

Esta tarea de documentación se ha verificado mediante lectura de las pruebas;
no se han ejecutado tests ni scripts y no se afirma un resultado de ejecución.
