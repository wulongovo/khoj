# Khoj Self-Hosted AI Assistant

Self-hosted [Khoj](https://github.com/khoj-ai/khoj) deployment with Docker + local LLM support.

## Quick Start

### Docker Mode
```bash
docker-compose up -d
```

### Local Mode
```bash
python start.py
```

### Access
- URL: http://localhost:42110
- Default: admin@khoj.local / khoj2026

## Files
- `docker-compose.yml` — Docker config
- `start.py` — Local launcher
- `run_khoj.py` — Runner script
- `khoj_settings.py` — Settings
- `启动Khoj.bat` — Windows quick launch
