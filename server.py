from fastapi import FastAPI, Request, Header
from typing import Optional, Dict, Any
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = FastAPI(title="API Receiver", version="1.0.0")


@app.get("/health")
async def health() -> Dict[str, str]:

    return {"status": "ok"}


@app.post("/webhook")
async def webhook(request: Request, x_signature: Optional[str] = Header(default=None)) -> Dict[str, Any]:

    payload: Dict[str, Any] = await request.json()
    logging.info("Received /webhook: signature=%s payload=%s", x_signature, payload)
    return {"received": True, "payload": payload}


@app.post("/echo")
async def echo(body: Dict[str, Any]) -> Dict[str, Any]:

    return {"echo": body}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)

