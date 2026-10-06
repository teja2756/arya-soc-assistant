# ARYA SOC Assistant

ARYA is an AI-assisted Security Operations Center (SOC) assistant concept documented by Ts.

## Project scope

The project combines:
- SOC alert analysis and triage
- AI/chatbot assistance
- Voice input/output
- Security-tool lab integration
- A web-based cyber/3D interface
- Future skill routing and automation

### Security lab

The documented lab environment includes:
- Suricata
- Wireshark
- Nmap
- Metasploit
- Kali Linux

## Repository note

This repository contains a **reconstructed portfolio implementation/starter** based on the project's supplied notes and specifications. It is not presented as the original source-code archive.

## Structure

- `app.py` — lightweight Flask API/demo
- `soc_engine.py` — rule-based SOC alert triage and risk scoring
- `templates/index.html` — simple dashboard
- `requirements.txt` — Python dependencies
- `docs/project-notes.md` — project documentation

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000
