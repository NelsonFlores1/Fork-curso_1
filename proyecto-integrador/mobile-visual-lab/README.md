# mobile-visual-lab — Sesión 9

Laboratorio de **emulación móvil** + **regresión visual** (Etapa 9 del gate).
Corre con `uv` + Playwright en Windows, macOS y Linux — **sin emulador Android
ni Appium en clase**.

## Por qué estas herramientas (y no las del temario literal)

| Tema | Temario | Hands-on | Por qué |
|---|---|---|---|
| Móvil | Appium / Maestro | Playwright viewport móvil | Emulador + drivers no son multiplataforma “sin trucos” en 45 min |
| Escritorio nativo | FlaUI / Pywinauto | Mapa | Windows-only |
| Visual IA | Applitools / Percy | Playwright + baselines PNG | Ya están en el stack; sustituyen Recheck (PLAN_MAESTRO) |

Appium, Maestro, Espresso, XCUITest, FlaUI, Pywinauto, Applitools y Percy
quedan en el **mapa** de la sesión.

## Setup

```bash
cd proyecto-integrador/mobile-visual-lab
uv sync --group dev
uv run playwright install chromium
    python scripts/capture_baselines.py
```
Usá `uv run python scripts/capture_baselines.py` si `python` no ve el venv.

## Tasks / comandos

| Comando | Esperado |
|---|---|
| `uv run pytest tests -v` | **exit 0** · smoke + visual vs baselines |
| `uv run pytest gate -v` | **exit 1** · UI `?broken=1` vs baseline sana |
| `python scripts/capture_baselines.py` | Reescribe PNG en `tests/baselines/` |

Atajos desde la raíz: `task setup:mobile` · `task test:mobile` · `task test:mobile:gate`.

## App demo

`app/index.html` — login + producto, responsive y modo oscuro.
`?broken=1` activa el banner de regresión (solo para el gate).
`?theme=dark` fuerza modo oscuro.
