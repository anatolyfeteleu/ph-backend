from fastapi import FastAPI

from extensions.app import init

app = FastAPI(title="Paw Hugs")
init(app)
