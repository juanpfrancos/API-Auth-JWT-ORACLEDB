import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.login import login
from routes.signup import signup
from routes.protected import protected_router
app = FastAPI(title="Authentication - API", description="Developed with ❤ by @Juanpfrancos")

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    'http://127.0.0.1:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login)
app.include_router(signup)
app.include_router(protected_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)