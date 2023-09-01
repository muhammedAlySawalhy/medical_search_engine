from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scrapping import router
import uvicorn

app = FastAPI()

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "python web scrapper"}


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)
