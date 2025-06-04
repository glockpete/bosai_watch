import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, AREA_CODE

CONF_AREA_CODE = "area_code"

class BosaiWatchConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Bosai Watch."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Validate area code (simple check)
            area_code = user_input.get(CONF_AREA_CODE)
            if not area_code or not area_code.isdigit():
                errors[CONF_AREA_CODE] = "invalid_area_code"
            else:
                return self.async_create_entry(title="Bosai Watch", data={CONF_AREA_CODE: area_code})

        data_schema = vol.Schema({
            vol.Required(CONF_AREA_CODE, default=AREA_CODE): str
        })
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors) 