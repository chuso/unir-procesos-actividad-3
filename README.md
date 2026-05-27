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


# 4. Calidad y métricas

La calidad del software es importante porque permite que una aplicación funcione correctamente, sea más fácil de entender y también más sencilla de mantener en el futuro. En este proyecto se ha desarrollado una calculadora en Python que realiza las cuatro operaciones básicas: suma, resta, multiplicación y división. Para asegurar que el programa funcionara bien, se han aplicado distintas pruebas y buenas prácticas durante el desarrollo.

El código está organizado mediante una clase llamada `Calculadora`, donde cada operación tiene su propio método independiente. Esto hace que el programa esté más ordenado y sea más fácil de leer. Además, cada método tiene comentarios y explicaciones que ayudan a entender qué hace cada parte del código.

También se ha tenido en cuenta el control de errores. Por ejemplo, en la operación de división se controla el caso en que un usuario intente dividir por cero. En esta situación, el programa lanza un error con un mensaje para evitar fallos inesperados.

Otro aspecto importante del proyecto ha sido el uso de Git y GitHub para el control de versiones. Gracias a ello, se pudieron registrar todos los cambios realizados durante el desarrollo y mantener un historial completo de modificaciones. El uso de commits permitió seguir la evolución del proyecto de forma organizada y facilitó el mantenimiento del código.

Además, se utilizaron herramientas de automatización mediante GitHub Actions para ejecutar pruebas y comprobaciones automáticas cada vez que se realizaban cambios en el repositorio. Esto ayudó a detectar errores rápidamente y a mejorar la estabilidad de la aplicación.

Para comprobar que todo funcionaba correctamente se realizaron pruebas unitarias utilizando la librería `unittest` de Python. Estas pruebas permiten verificar automáticamente que cada operación devuelve el resultado esperado.

Entre las métricas y aspectos de calidad que se han trabajado destacan:

- La organización y claridad del código.
- La separación de cada operación en métodos independientes.
- El uso de Git y GitHub para el control de versiones.
- El seguimiento del desarrollo mediante commits.
- La automatización de pruebas con GitHub Actions.
- El control de errores en casos especiales, como la división por cero.
- La realización de pruebas unitarias para todas las operaciones.
- La comprobación de distintos tipos de datos: positivos, negativos, cero y números decimales.

Las pruebas unitarias se diseñaron para comprobar diferentes situaciones. En la suma, por ejemplo, se probaron números positivos, negativos, decimales y cero. Lo mismo se hizo en las operaciones de resta y multiplicación. En la división, además de comprobar operaciones normales, también se verificó que el programa se comportara correctamente cuando el divisor era cero.

Otro aspecto importante es que las pruebas están organizadas siguiendo una estructura clara (*Arrange, Act y Assert*), lo que facilita entender qué se está probando en cada caso. Además, para comparar números decimales se utilizó `assertAlmostEqual`, evitando problemas de precisión con números flotantes.

Los resultados obtenidos fueron positivos, ya que todas las pruebas se ejecutaron correctamente y la calculadora respondió de manera adecuada en todos los casos probados. Gracias a estas pruebas se pudo comprobar que la aplicación es estable, funciona correctamente y gestiona bien tanto las operaciones normales como los posibles errores.
