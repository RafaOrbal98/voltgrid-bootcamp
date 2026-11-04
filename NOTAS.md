# 📓 Notas: Bootcamp Python · VoltGrid

## Sesión 1 · Setup pro y primer procesador de lecturas
**Fecha:** miércoles 4 de noviembre de 2026
**Fase:** 0, De PHP a Python y de la idea al código

---

### 🎯 Qué logré hoy
- Instalé y configuré el entorno de desarrollo: `uv`, Git, VS Code y Ruff.
- Creé el proyecto `voltgrid-bootcamp` con layout profesional (`src/`).
- Escribí mi primer pseudocódigo y lo traduje a una función de Python que funciona.
- Pasé el código por Ruff: **All checks passed!** ✅

---

### 🛠️ Herramientas

| Herramienta | Para qué sirve | Su gemelo en PHP |
|---|---|---|
| `uv` | Instala Python, maneja dependencias y entornos | Composer + administrador de versiones de PHP |
| Git | Control de versiones | Igual |
| VS Code + extensión Python | Editor | Igual |
| Ruff | Formatea el código y detecta malas prácticas | PHP-CS-Fixer + PHPStan |
| pytest | Pruebas automáticas (lo usamos pronto) | PHPUnit |

---

### ⌨️ Comandos clave

```bash
# Crear un proyecto nuevo
uv init nombre-proyecto
uv python pin 3.13          # fija la versión de Python del proyecto
uv add libreria             # agrega una dependencia
uv add --dev libreria       # dependencia solo para desarrollo (como require-dev)
uv sync                     # sincroniza el entorno con pyproject.toml

# Ejecutar el proyecto
uv run voltgrid-bootcamp

# Antes de CADA commit
uv run ruff format          # acomoda el estilo
uv run ruff check           # busca malas prácticas

# Git
git add .
git commit -m "mensaje"
```

---

### 📁 Estructura del proyecto

```
voltgrid-bootcamp/
├── pyproject.toml              ← configuración y dependencias (composer.json)
├── uv.lock                     ← versiones exactas (composer.lock)
├── .python-version             ← versión de Python del proyecto (3.13)
├── .gitignore                  ← lo que Git ignora (incluye .venv/)
├── .venv/                      ← entorno aislado (vendor/ + su propio Python)
└── src/
    └── voltgrid_bootcamp/      ← el PAQUETE (como un namespace PSR-4)
        ├── __init__.py         ← la "recepción" del paquete; aquí vive main()
        └── medidor.py          ← un MÓDULO con la lógica de lecturas
```

**¿Por qué `main()` arranca desde `__init__.py`?** No es por el nombre del archivo, es porque `pyproject.toml` lo dice:

```toml
[project.scripts]
voltgrid-bootcamp = "voltgrid_bootcamp:main"
#  nombre del comando   paquete : función
```

---

### 🐍 Conceptos de Python que vi hoy

| Python | PHP | Qué hace |
|---|---|---|
| `def nombre(x: int) -> str:` | `function nombre(int $x): string` | Define una función. `def` = *define* |
| `x: list[float]` | `array $x` | Type hint. Es una guía, Python no lo valida al ejecutar |
| `"""Texto"""` | `/** PHPDoc */` | Docstring: documentación de la función |
| `for x in lista:` | `foreach ($lista as $x)` | Recorre una lista |
| `for i, x in enumerate(lista):` | `foreach ($lista as $i => $x)` | Recorre con índice y valor |
| `range(0, 8, 4)` | `range(0, 7, 4)` | Genera 0, 4. **El fin NO se incluye** |
| `lista[0:4]` | `array_slice($lista, 0, 4)` | Rebana posiciones 0, 1, 2, 3. **El fin NO se incluye** |
| `sum(lista)` | `array_sum($lista)` | Suma una lista |
| `lista.append(x)` | `$lista[] = $x;` | Agrega al final |
| `[i for i, x in enumerate(l) if x < 0]` | `array_keys(array_filter(...))` | List comprehension: filtra y transforma en una línea |
| `f"{total:,.2f}"` | `number_format($total, 2)` | Formato dentro de un f-string |
| `MAYUSCULAS = ...` | `const MAYUSCULAS` | Convención de constante (no se bloquea) |
| `None` | `null` | Ausencia de valor |
| Indentación | `{ }` y `;` | La sangría ES la sintaxis |

📌 **Regla de oro:** en `range` y en slicing, el número final **nunca se incluye**. Piénsalo como marcas en una regla: `[0:4]` corta desde la marca 0 hasta la marca 4.

---

### 🧠 Método: de la idea al código

1. **Entender:** qué entra, qué sale y qué puede salir mal.
2. **Descomponer:** pasos chiquitos, en español, sin código.
3. **Pseudocódigo:** la receta de cocina. Ya lo hago en mis flujos y escenarios Gherkin.
4. **Test primero:** cómo voy a saber que funciona.
5. **Código:** ahora sí, y el pseudocódigo se queda como comentarios.

**Ejemplo de hoy, con el pseudocódigo como comentarios:**

```python
def totales_por_hora(lecturas: list[float]) -> list[float]:
    """Agrupa lecturas de 15 min en bloques de 4 y regresa el total de cada hora."""
    # 1. Preparo una lista vacía para los resultados
    totales: list[float] = []

    # 2. Recorro las lecturas de 4 en 4
    for i in range(0, len(lecturas), 4):
        # 3. Tomo el grupo de 4 lecturas
        grupo = lecturas[i : i + 4]
        # 4. Lo sumo y lo guardo en la lista
        totales.append(sum(grupo))

    # 5. Regreso la lista con las sumas
    return totales
```

**En cámara lenta:**

| Vuelta | `i` | Rebanada | Suma | `totales` |
|---|---|---|---|---|
| 1 | 0 | `[0:4]` | 479.6 | `[479.6]` |
| 2 | 4 | `[4:8]` | 373.3 | `[479.6, 373.3]` |
| — | 8 | ya no entra (8 es el límite) | — | se regresa ✅ |

---

### 🔧 Problemas que resolví (troubleshooting)

| Error | Causa | Solución |
|---|---|---|
| `zsh: command not found: uv` | La terminal no conocía el nuevo PATH | `source $HOME/.local/bin/env` o abrir una terminal nueva |
| `command not found: $` | Copié el `$` de una guía | El `$` solo indica el prompt; no se copia |
| `command not found: brew` | Homebrew no está instalado | Para Git usé `xcode-select --install` |
| `command not found: code` | VS Code no instala ese comando por defecto | `Cmd+Shift+P` → "Shell Command: Install 'code' command in PATH" |
| `Failed to spawn: main.py` | Esta versión de `uv` creó un paquete, no un script suelto | Ejecutar con `uv run voltgrid-bootcamp` |
| `requires-python = ">=3.9"` | `uv init` tomó el Python viejo del Mac | Cambiar a `">=3.13"` y correr `uv sync` |

💡 **Lección:** antes de asumir cómo quedó algo que generó una herramienta, **primero inspecciono** (`find`, `cat`) y luego actúo.

---

### ❓ Pregunta abierta para la próxima sesión
¿Qué pasa si el medidor manda **10 lecturas** en lugar de 8? Python no truena: `lecturas[8:12]` regresa solo 2 y las suma como si fueran una hora completa.
**El bug más peligroso es el que no truena.** ¿Cómo lo detectarías o lo evitarías?

---

### ✅ Pendientes
- [ ] Publicar el repo en GitHub (Source Control → Publish Branch).
- [ ] Guardar este archivo como `NOTAS.md` en la raíz del repo y hacer commit.
