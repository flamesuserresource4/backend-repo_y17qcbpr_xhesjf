"""
Database Schemas for Aryan Gupta Portfolio

Each Pydantic model corresponds to a MongoDB collection.
Collection name is the lowercase of the class name.
"""
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import List, Optional, Literal, Dict

# ----- Core Profile -----
class Profile(BaseModel):
    name: str = Field(..., description="Full name")
    subtitle: str = Field(..., description="Short role tagline")
    bio: str = Field(..., description="Short biography")
    education: List[str] = Field(default_factory=list, description="Education timeline strings")
    skills_design: List[str] = Field(default_factory=list, description="Design skills")
    skills_tech: List[str] = Field(default_factory=list, description="Tech skills")
    philosophy: str = Field("", description="Creative philosophy statement")
    portrait_url: Optional[HttpUrl] = Field(None, description="Portrait or abstract self image URL")
    email: Optional[EmailStr] = None
    resume_url: Optional[HttpUrl] = None
    socials: Dict[str, str] = Field(default_factory=dict, description="Map of social platform → URL")

# ----- Projects -----
class Project(BaseModel):
    title: str
    slug: str = Field(..., description="URL-safe unique slug")
    summary: str = Field("", description="Short summary/tagline")
    tags: List[str] = Field(default_factory=list)
    cover_image: Optional[HttpUrl] = None
    problem_context: str = Field("", description="Problem context")
    research: str = Field("", description="Primary + secondary research insights")
    ideation: str = Field("", description="Ideation narrative")
    process_images: List[HttpUrl] = Field(default_factory=list)
    outcomes: str = Field("", description="Final outcomes")
    reflection: str = Field("", description="Reflection / learnings")

# ----- Collections / Galleries -----
class CollectionItem(BaseModel):
    category: Literal[
        "Visual Design", "Typography", "Photography", "Motion", "Trend Research"
    ]
    title: str
    image_url: HttpUrl
    alt: Optional[str] = None

# ----- Experience -----
class Experience(BaseModel):
    type: Literal["Internship", "Leadership", "Volunteering", "Achievement"]
    role: str
    org: str
    start: str
    end: Optional[str] = None
    description: Optional[str] = None

# ----- Services -----
class Service(BaseModel):
    title: str
    description: str

# ----- Contact Messages -----
class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str
