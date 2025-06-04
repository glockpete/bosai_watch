"""Utility functions for loading Bosai Watch secrets."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict

import yaml
from homeassistant.core import HomeAssistant


def load_secrets(hass: HomeAssistant) -> Dict[str, Any]:
    """Load secrets from ``bosai_watch_secrets.yaml`` in the config directory."""
    secrets_file = Path(hass.config.path("bosai_watch_secrets.yaml"))
    if not secrets_file.is_file():
        return {}
    try:
        with secrets_file.open("r", encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}
    except Exception as exc:  # pragma: no cover - best effort
        logging.getLogger(__name__).warning("Failed to read Bosai Watch secrets: %s", exc)
        return {}


def get_secret(hass: HomeAssistant, key: str, default: Any | None = None) -> Any:
    """Return a single secret value."""
    secrets = hass.data.get("bosai_watch", {}).get("secrets")
    if secrets is None:
        secrets = load_secrets(hass)
        hass.data.setdefault("bosai_watch", {})["secrets"] = secrets
    return secrets.get(key, default)
