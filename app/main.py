from fastapi import FastAPI

app = FastAPI(
    title="Student Attendance API",
    description="Backend API for managing student attendance",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Student Attendance API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}