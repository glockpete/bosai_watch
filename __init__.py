# Bosai Watch init
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .secrets import load_secrets

DOMAIN = 'bosai_watch'

PLATFORMS = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Bosai Watch from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["secrets"] = load_secrets(hass)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
