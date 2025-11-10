from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings  # ✅ Import the instance, not the class
from routers import story, job

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application with custom metadata.",
    version="1.0.0",
    docs_url="/doc",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ✅ Include routers
app.include_router(story.router, prefix=f"{settings.API_PREFIX}/stories", tags=["stories"])
app.include_router(job.router, prefix=f"{settings.API_PREFIX}/jobs", tags=["jobs"])

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)