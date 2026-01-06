#!/usr/bin/env python3
"""
Notification sensor for Afvalwijzer
"""
from homeassistant.helpers.entity import Entity
from .const.const import _LOGGER, CONF_ID

from .const.const import (
    _LOGGER,
    CONF_ID,
)

class NotificationSensor(Entity):
    """Representation of an Afvalwijzer Notification Sensor."""

    def __init__(self, hass, data, config):
        """Initialize the sensor."""
        self.hass = hass
        self._data = data
        self._config = config
        
        # Build sensor name with optional ID
        config_id = config.get(CONF_ID, "").strip()
        if config_id:
            self._name = f"afvalwijzer_{config_id}_notifications"
            self._attr_unique_id = f"afvalwijzer_{config_id}_notifications"
        else:
            self._name = "afvalwijzer_notifications"
            self._attr_unique_id = "afvalwijzer_notifications"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the number of active notifications."""
        if self._data.notification_data is None:
            return 0
        
        count = len(self._data.notification_data)
        _LOGGER.debug(f"NotificationSensor.state: returning count {count}")
        return count

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        notifications = self._data.notification_data or []
        return {
            "notifications": notifications,
            "count": len(notifications)
        }

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        if self._data.notification_data and len(self._data.notification_data) > 0:
            return "mdi:bell-alert"
        return "mdi:bell-outline"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "meldingen"

    def update(self):
        """Update is handled by the central AfvalwijzerData object."""
        _LOGGER.debug(f"Updating sensor: {self.name}")
        pass
