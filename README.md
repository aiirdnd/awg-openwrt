### API Receiver

Minimal FastAPI server to receive API requests (JSON webhooks) and echo data.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

Or run directly:

```bash
python server.py
```

### Endpoints

- `GET /health`: Health check
- `POST /webhook`: Accepts JSON, logs it, returns `{received: true, payload: ...}`
- `POST /echo`: Returns the same JSON back

### Examples

```bash
curl -s http://localhost:8000/health

curl -s -X POST http://localhost:8000/webhook \
  -H 'Content-Type: application/json' \
  -H 'X-Signature: test-signature' \
  -d '{"event":"ping","data":{"foo":"bar"}}'

curl -s -X POST http://localhost:8000/echo \
  -H 'Content-Type: application/json' \
  -d '{"hello":"world"}'
```

