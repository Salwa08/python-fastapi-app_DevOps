from fastapi import FastAPI

from .config import settings
# TP5: test du filtre sur app/
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)


@app.get("/")
def root():
    return {"message": "the server is now active"}


@app.get("/health")
def health():
    return {"ok": True}
