"""Fixtures del lab S9: URL file:// de la app demo + helpers de viewport."""

from pathlib import Path

import pytest

APP_HTML = Path(__file__).resolve().parents[1] / "app" / "index.html"

# Viewport tipo teléfono (aprox. iPhone 14)
MOBILE_VIEWPORT = {"width": 390, "height": 844}
DESKTOP_VIEWPORT = {"width": 1280, "height": 720}


@pytest.fixture
def app_url() -> str:
    """URL file:// de app/index.html (sin query)."""
    return APP_HTML.as_uri()


@pytest.fixture
def app_url_broken() -> str:
    """Misma app con ?broken=1 — cambia layout a propósito (gate visual)."""
    return APP_HTML.as_uri() + "?broken=1"


@pytest.fixture
def app_url_dark() -> str:
    return APP_HTML.as_uri() + "?theme=dark"
