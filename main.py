from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/event")
def get_event():
    return {
        "success": True,
        "data": {
            "event_name": "TechFusion 2K26",
            "date": "2026-04-08",
            "venue": "IT Auditorium",
            "entry_fee": 100,
            "slots_available": 156,
            "registration_open": True,
        },
    }


@app.get("/api/health")
def health():
    return {"success": True, "data": {"status": "ok"}}
