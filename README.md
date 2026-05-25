# Actividad 3 grupal — Diseño de pruebas de software

[![codecov](https://codecov.io/github/chuso/unir-procesos-actividad-3/graph/badge.svg?token=NM71JRV9EW)](https://codecov.io/github/chuso/unir-procesos-actividad-3)

Asignatura: **Procesos en Ingeniería del Software**

## Contenido

- `calculadora.py` — Implementación de la clase `Calculadora` con las cuatro operaciones aritméticas básicas (sumar, restar, multiplicar, dividir).
- `test_calculadora.py` — Pruebas unitarias con `unittest` (21 casos de prueba).

## Requisitos

- Python 3.9 o superior.
- [`uv`](https://docs.astral.sh/uv/) para gestión de dependencias y entorno virtual.

## Configuración del entorno

```bash
uv sync --group dev
```

## Ejecución

### Ejecutar la calculadora (demo manual)

```bash
uv run python calculadora.py
```

### Ejecutar las pruebas

```bash
uv run python -m unittest discover -s tests -v
```

### Linting y formato

```bash
uv run ruff check .
uv run ruff format .
```

### Comprobación de tipos

```bash
uv run mypy src/ tests/
```

## Diseño de las pruebas

Para cada operación se han definido varios casos siguiendo el material del Tema 7 (Pruebas):

- **Partición de equivalencia** (slide 27): positivos, negativos, cero.
- **Gestión de errores** (slide 9): la división por cero lanza `ValueError`.
- **Patrón Arrange-Act-Assert** y nombrado `test_metodo_escenario_resultadoEsperado` (slide 10).

### Resumen de casos

| Operación | Nº de casos | Cubre |
|-----------|-------------|-------|
| Suma | 5 | positivos, negativos, cero, signos opuestos, decimales |
| Resta | 5 | positivos, negativos, cero a la derecha, cero a la izquierda, resultado negativo |
| Multiplicación | 5 | positivos, negativos, cero (absorbente), signos opuestos, uno (neutro) |
| División | 6 | positivos, negativos, dividendo cero, decimales, divisor cero (`ValueError`), 0/0 (`ValueError`) |
| **Total** | **21** | |
