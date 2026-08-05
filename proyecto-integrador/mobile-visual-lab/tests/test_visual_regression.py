"""Regresión visual contra baselines versionadas (Sesión 9).

Generar / actualizar baselines:
    python scripts/capture_baselines.py
"""

from pathlib import Path

from playwright.sync_api import Page

from conftest import DESKTOP_VIEWPORT, MOBILE_VIEWPORT
from visual_utils import assert_matches_baseline

REPORTS = Path(__file__).resolve().parents[1] / "reports"
MAX_DIFF = 120


def _shot(page: Page, name: str) -> Path:
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / name
    page.screenshot(path=path, full_page=True)
    return path


def test_home_desktop_light(page: Page, app_url: str) -> None:
    page.set_viewport_size(DESKTOP_VIEWPORT)
    page.goto(app_url)
    actual = _shot(page, "actual-desktop-light.png")
    assert_matches_baseline("home-desktop-light.png", actual, max_diff_pixels=MAX_DIFF)


def test_home_mobile_light(page: Page, app_url: str) -> None:
    page.set_viewport_size(MOBILE_VIEWPORT)
    page.goto(app_url)
    actual = _shot(page, "actual-mobile-light.png")
    assert_matches_baseline("home-mobile-light.png", actual, max_diff_pixels=MAX_DIFF)


def test_home_desktop_dark(page: Page, app_url_dark: str) -> None:
    page.set_viewport_size(DESKTOP_VIEWPORT)
    page.goto(app_url_dark)
    actual = _shot(page, "actual-desktop-dark.png")
    assert_matches_baseline("home-desktop-dark.png", actual, max_diff_pixels=MAX_DIFF)
