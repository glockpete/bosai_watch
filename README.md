<<<<< WORK IN PROGRESS >>>>>>

# Bosai Watch Integration

A comprehensive disaster and safety monitoring integration for Home Assistant, tailored for Japan. Bosai Watch aggregates real-time data from government, community, and open sources to provide advanced disaster, infrastructure, and environmental monitoring.

## 🌟 Features

### Multi-Source Disaster Monitoring
- **Seismic Activity**: Real-time earthquake and seismic intensity monitoring
- **Disaster Alerts**: National and regional disaster warnings (earthquake, tsunami, typhoon, etc.)
- **Weather Emergencies**: Severe weather and emergency status from JMA and other sources
- **Radiation Monitoring**: Safecast and government radiation levels (μSv/h)
- **Infrastructure Status**: Power, water, gas, and telecom outage monitoring
- **Emergency Services**: Fire, police, medical, and coast guard load/capacity
- **Social Sentiment**: Disaster-related social media analysis
- **Community Reports**: User-generated safety and hazard reports

### Advanced Data Aggregation
- **Multiple APIs**: JMA, Safecast, government, social, and infrastructure APIs
- **Smart Data Fusion**: Aggregates and validates data from multiple sources
- **Real-Time Updates**: Frequent polling for up-to-date information
- **Comprehensive Sensors**: 30+ sensors for disaster, environment, and infrastructure

## 📊 Sensor Entities

### Core Sensors
- **Japan Seismic Activity Level**: Real-time seismic intensity
- **National Disaster Alert Level**: Aggregated disaster warnings
- **Weather Emergency Status**: Severe weather alerts
- **Transportation Disruption Index**: Rail, road, air, and port status
- **Critical Infrastructure Status**: Power, water, telecom health
- **Emergency Services Load**: Fire, police, medical, coast guard
- **Social Media Disaster Sentiment**: Social sentiment analysis
- **Population Safety Index**: Overall safety assessment
- **Economic Impact Indicator**: Disaster economic impact
- **Government Response Level**: Disaster response activation

### Extended Sensors
- **Radiation Safety Monitor**: Environmental radiation (μSv/h)
- **Air Quality Index**: PM2.5 and AQI
- **Community Safety Reports**: User hazard and help reports
- **Supply Chain Monitor**: Disruption index
- **Emergency Shelter Capacity**: Shelter availability
- **Medical System Load**: Hospital capacity
- **Cross-Border Impact Monitor**: International disaster effects

### Special Sensors
- **Safecast Radiation Level**: Latest Safecast community radiation reading (Tokyo)

## 🚨 Alert System

- **Earthquake, Tsunami, Typhoon Alerts**: Real-time government and community warnings
- **Infrastructure Outage Alerts**: Power, water, gas, telecom
- **Health & Safety Alerts**: Radiation, air quality, medical system
- **Community & Social Alerts**: Social sentiment, help requests

## 🏠 Home Assistant Integration

### Installation
1. Copy the `bosai_watch` folder to your Home Assistant `custom_components` directory.
2. Restart Home Assistant.
3. Add the Bosai Watch integration via the UI or YAML.

### Secrets File
Create ``bosai_watch_secrets.yaml`` in your Home Assistant configuration
directory to store API keys or passwords.  Each key can then be retrieved
automatically by the integration.  Example:

```yaml
twitter_bearer_token: YOUR_TOKEN
tokyo_metro_key: YOUR_KEY
```

Restart Home Assistant after creating or updating the file so the secrets are
reloaded.

### Example Dashboard Cards

#### Disaster Overview
```yaml
# Bosai Watch disaster overview
- type: entities
  title: "Bosai Watch - Disaster Overview"
  entities:
    - sensor.japan_seismic_activity
    - sensor.national_disaster_alert_level
    - sensor.weather_emergency_status
    - sensor.critical_infrastructure_status
    - sensor.safecast_radiation_level
```

#### Infrastructure & Health
```yaml
- type: entities
  title: "Infrastructure & Health"
  entities:
    - sensor.emergency_services_load
    - sensor.medical_system_load
    - sensor.air_quality_index
    - sensor.radiation_safety_monitor
```

#### Community & Social
```yaml
- type: entities
  title: "Community & Social"
  entities:
    - sensor.community_safety_reports
    - sensor.social_media_disaster_sentiment
    - sensor.supply_chain_monitor
```

## 📚 Documentation

- For detailed setup, configuration, and troubleshooting, see the [Bosai Watch Comprehensive Guide](../bosai_watch_comprehensive_guide.md).

## 🤝 Credits

- Data sources: JMA, Safecast, Japanese Government, Social APIs, Community Reports
- Integration by the Bosai Watch Team
