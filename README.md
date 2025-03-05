# Weather api displayer

## Getting Started

### Dev environment
To set up this container, you should be able to run:

```
python3 -m venv .venv ; ./.venv/bin/activate
pip install -r requirements.txt
cd weather-gov-api-client ; pip install . ; cd ..
cd app ; fastapi dev main.py
```

### Production environment

## Concept

This is a simple shim and template generator so that you can access ad-free and bloat free weather for any location in the US. It uses weather.gov's API to request forecast for a given location.
