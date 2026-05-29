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

La calidad del software, según el modelo ISO/IEC 25010, queda definida por un conjunto de atributos (funcionalidad, fiabilidad, usabilidad, eficiencia, mantenibilidad, portabilidad, compatibilidad y seguridad) que pueden medirse de forma cuantitativa mediante métricas. En este apartado se describe cómo se han abordado los atributos relevantes para el proyecto y se aportan las métricas obtenidas sobre el código entregado.

## 4.1 Atributos de calidad aplicados

Dada la naturaleza acotada del proyecto (una calculadora con cuatro operaciones), los atributos de la ISO/IEC 25010 con repercusión directa son los siguientes:

| Atributo (ISO/IEC 25010) | Aplicación en este proyecto |
|-----------|-------------|
| Funcionalidad (corrección) | Las 21 pruebas unitarias verifican que las cuatro operaciones devuelven el resultado matemáticamente correcto en todos los casos diseñados. |
| Fiabilidad (tolerancia a fallos) | La división controla explícitamente el divisor nulo y lanza una excepción _ValueError_ descriptiva en lugar de propagar la _ZeroDivisionError_ nativa. |
| Mantenibilidad (analizabilidad y capacidad de prueba) | Complejidad ciclomática baja (media 1,4), métodos independientes y autodocumentados con docstrings, suite de pruebas reproducible con un único comando.|

## 4.2 Decisiones de diseño orientadas a la calidad

Dentro de este apartado se han tomado las siguientes decisiones:

•	Encapsulación: las cuatro operaciones se ofrecen como métodos de la clase Calculadora, lo que separa responsabilidades y facilita las pruebas unitarias.

•	Métodos puros: no se almacena estado entre llamadas. Cada operación depende únicamente de sus argumentos, lo que elimina efectos colaterales y aísla cada prueba.

•	Documentación _inline_: todos los métodos disponen de _docstrings_ con descripción de parámetros, valor devuelto y excepciones.

•	Gestión explícita de errores: la división por cero se valida antes de operar y lanza una excepción _ValueError_ con un mensaje descriptivo, en lugar de propagar la _ZeroDivisionError_ nativa de Python.

## 4.3 Estrategia de pruebas unitarias

Se han diseñado un total de 21 pruebas unitarias con la librería unittest (biblioteca estándar de Python), aplicando las técnicas de caja negra:

•	Partición de equivalencia: se identifican clases de equivalencia para cada operación (operandos positivos, negativos, cero, decimales y combinaciones de signo) y se selecciona al menos un caso representativo de cada una.

•	Valores límite y casos especiales: se prueban explícitamente los elementos neutros (0 en suma/resta, 1 en multiplicación), el absorbente (0 en multiplicación) y el caso límite de la división por cero.

•	Patrón _Arrange_ / _Act_ / _Assert_: cada prueba sigue las tres fases, con nombrado de métodos en formato test_<operacion>_<escenario>_<resultado>.

•	Aislamiento: mediante el método _setUp__()_, cada prueba recibe una instancia nueva de Calculadora, evitando compartir estado.

•	Comparación de flotantes: para evitar falsos negativos derivados de la representación binaria de los decimales se utiliza _assertAlmostEqual_ en lugar de _assertEqual_.

## 4.4 Métricas obtenidas

Las siguientes métricas se han calculado de forma automática sobre el código fuente con la herramienta _radon_ (análisis estático de código Python).

| Métrica | Valor medido | Interpretación |
|---|---|---|
| SLOC (calculadora.py) | 17 | Líneas de código fuente sin comentarios ni líneas en blanco. |
| SLOC (test_calculadora.py) | 73 | Volumen de pruebas muy superior al del código a probar. Indicador de buena cobertura por diseño. |
| Complejidad ciclomática media (VG) | 1.4 (A) | Métrica de McCabe. Categoría A según radon (complejidad muy baja, fácil de probar y mantener). |
| VG por método | 1, 1, 1, 2 | Sumar, restar y multiplicar carecen de ramas; dividir tiene una rama (control de divisor cero). |
| WMC (Weighted Methods per Class) | 5 | Métrica CK: suma de la complejidad ciclomática de los métodos de la clase Calculadora. |
| Nº de pruebas unitarias | 21 | 5 para suma, 5 para resta, 5 para multiplicación y 6 para división (2 de ellas de gestión de errores). |
| Ratio pruebas/método | 5.25 | Más de cinco casos por método; por encima del mínimo aceptado (3 por operación). |
| Cobertura de métodos | 100 % | Los 4 métodos de la clase Calculadora se ejecutan en las pruebas. |
| Cobertura de ramas (decisiones) | 100 % | La única decisión existente (`b == 0` en dividir) se ejecuta tanto en verdadero como en falso. |

Los resultados de ejecución han sido los siguientes: De las 21 pruebas ejecutadas, 21 han sido superadas, produciéndose 0 fallos y 0 errores, con un tiempo de ejecución inferior a 10 ms.

## 4.5 Control de versiones e integración continua

Para el seguimiento del desarrollo se ha utilizado un repositorio alojado en GitHub. Además, se ha configurado un flujo de integración continua mediante GitHub Actions que ejecuta automáticamente la suite de pruebas en cada _push_ al repositorio. Esta automatización es coherente con la noción de prueba como parte del diseño aproximándose al enfoque de _Test-Driven Development_.

Enlace al repositorio: https://github.com/chuso/unir-procesos-actividad-3

## 4.6 Conclusión

El proyecto cumple con los requisitos de calidad más importantes para su envergadura. Así su complejidad ciclomática es mínima (media de 1,4), se cubre al 100 % tanto los métodos como las ramas, hay ratio de 5,25 pruebas por método y se gestiona de forma explícita el único caso de error posible. Se ha aplicado de forma combinada el marco ISO/IEC 25010, con métricas y técnicas de prueba.


