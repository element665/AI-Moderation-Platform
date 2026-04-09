from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Comment(Base):
    __tablename__ = "comments"

    id = Column(String, primary_key=True)
    text = Column(String)
    platform = Column(String)
    label = Column(String)
    confidence = Column(Float)

def init_db():
    Base.metadata.create_all(engine)

def save_comment(comment, result):
    db = SessionLocal()

    record = Comment(
        id=str(hash(comment["text"])),
        text=comment["text"],
        platform=comment["platform"],
        label=result["label"],
        confidence=result["confidence"],
    )

    db.add(record)
    db.commit()
    db.close()