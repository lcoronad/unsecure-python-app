# unsecure-python-app

Proyecto Python **intencionalmente vulnerable** para demos de Trivy (SCA) y OpenGrep (SAST) con el agente de triage.

## Dependencias vulnerables (Trivy → `requirements.txt`)

| Paquete | Versión | CVE demo |
|---------|---------|----------|
| `Django` | 2.2.0 | CVE-2019-14234 (SQLi en JSONField) |
| `requests` | 2.20.0 | CVE-2018-18074 |
| `cryptography` | 3.2 | CVE-2020-25659 |
| `PyYAML` | 5.1 | CVE-2020-14343 |
| `urllib3` | 1.24.1 | CVE-2019-11324 |
| `Pillow` | 8.0.1 | CVE-2020-35654 |

## Endpoints vulnerables (OpenGrep → `.semgrep/demo-python.yaml`)

| Módulo | Ruta | CWE | Descripción |
|--------|------|-----|-------------|
| `app/command.py` | `GET /util/ping?host=` | CWE-78 | Command injection (`os.system`) |
| `app/sql.py` | `GET /db/user?name=` | CWE-89 | SQL injection (f-string en `execute`) |
| `app/file_io.py` | `GET /files/read?path=` | CWE-22 | Path traversal (`open`) |
| `app/deserialization.py` | `POST /api/import/pickle` | CWE-502 | `pickle.loads` |
| `app/deserialization.py` | `POST /api/import/yaml` | CWE-502 | `yaml.load` inseguro |
| `app/crypto.py` | `POST /auth/hash` | CWE-327 | Hash MD5 débil |

## Ejecución local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Escaneo local

```bash
# SCA
trivy fs --format json --output trivy-results.json .

# SAST
semgrep scan --config=p/python --config=.semgrep/demo-python.yaml --sarif --output opengrep-results.sarif .
```

## Notas para el pipeline

- OpenGrep debe usar `p/python` + `.semgrep/demo-python.yaml` (el pack OSS no cubre todos los patrones demo).
- Incluir `requirements.txt` y módulos `app/` en el mismo PR para SCA + SAST.

**No desplegar en producción.**
