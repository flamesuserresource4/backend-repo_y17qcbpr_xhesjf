import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from database import db, create_document, get_documents
from schemas import Profile, Project, CollectionItem, Experience, Service, ContactMessage

app = FastAPI(title="Aryan Gupta Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Aryan Gupta Portfolio API running"}

@app.get("/test")
def test_database():
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Available",
        "database_url": None,
        "database_name": None,
        "connection_status": "Not Connected",
        "collections": []
    }
    try:
        if db is not None:
            response["database"] = "✅ Available"
            response["database_url"] = "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set"
            response["database_name"] = getattr(db, 'name', None) or "Unknown"
            response["connection_status"] = "Connected"
            try:
                response["collections"] = db.list_collection_names()
                response["database"] = "✅ Connected & Working"
            except Exception as e:
                response["database"] = f"⚠️ Connected but Error: {str(e)[:80]}"
        else:
            response["database"] = "⚠️ Available but not initialized"
    except Exception as e:
        response["database"] = f"❌ Error: {str(e)[:80]}"
    return response

# ----- Profile Endpoints -----
@app.get("/api/profile", response_model=List[Profile])
def get_profile():
    return get_documents("profile")

@app.post("/api/profile")
def create_profile(profile: Profile):
    try:
        _id = create_document("profile", profile)
        return {"inserted_id": _id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----- Projects Endpoints -----
@app.get("/api/projects", response_model=List[Project])
def list_projects():
    return get_documents("project")

@app.post("/api/projects")
def create_project(project: Project):
    try:
        _id = create_document("project", project)
        return {"inserted_id": _id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----- Collections Endpoints -----
@app.get("/api/collections", response_model=List[CollectionItem])
def list_collections():
    return get_documents("collectionitem")

@app.post("/api/collections")
def create_collection_item(item: CollectionItem):
    try:
        _id = create_document("collectionitem", item)
        return {"inserted_id": _id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----- Experience Endpoints -----
@app.get("/api/experience", response_model=List[Experience])
def list_experience():
    return get_documents("experience")

@app.post("/api/experience")
def create_experience(exp: Experience):
    try:
        _id = create_document("experience", exp)
        return {"inserted_id": _id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----- Services Endpoints -----
@app.get("/api/services", response_model=List[Service])
def list_services():
    return get_documents("service")

@app.post("/api/services")
def create_service(service: Service):
    try:
        _id = create_document("service", service)
        return {"inserted_id": _id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----- Contact Messages -----
@app.post("/api/contact")
def submit_contact(msg: ContactMessage):
    try:
        _id = create_document("contactmessage", msg)
        return {"inserted_id": _id, "status": "received"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
