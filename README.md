# Actividad 3 grupal — Diseño de pruebas de software

Asignatura: **Procesos en Ingeniería del Software**

## Contenido

- `calculadora.py` — Implementación de la clase `Calculadora` con las cuatro operaciones aritméticas básicas (sumar, restar, multiplicar, dividir).
- `test_calculadora.py` — Pruebas unitarias con `unittest` (21 casos de prueba).

## Requisitos

- Python 3.7 o superior. No se requieren dependencias externas (`unittest` forma parte de la librería estándar).

## Ejecución

### Ejecutar la calculadora (demo manual)

```bash
python calculadora.py
```

### Ejecutar las pruebas unitarias

```bash
python -m unittest test_calculadora.py -v
```

Alternativamente:

```bash
python test_calculadora.py
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
