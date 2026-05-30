"""Thread and message persistence service — MongoDB backed."""

from __future__ import annotations

from datetime import datetime, timezone

import pymongo

from app.core.config import load_settings
from app.schemas.threads import MessageRecord, ThreadRecord, ThreadListRequest, ThreadCreateRequest

_mongo_client: pymongo.MongoClient | None = None


def _db():
    global _mongo_client
    settings = load_settings()
    if _mongo_client is None:
        _mongo_client = pymongo.MongoClient(settings.mongo_uri)
    return _mongo_client[settings.mongo_db_name]


class ThreadService:
    def get_or_create_thread(self, thread_id: str | None, user_id: str, title: str = "") -> ThreadRecord:
        db = _db()
        if thread_id:
            doc = db.threads.find_one({"thread_id": thread_id, "user_id": user_id})
            if doc:
                doc.pop("_id", None)
                return ThreadRecord(**doc)

        record = ThreadRecord(
            thread_id=thread_id or f"thread_{__import__('uuid').uuid4().hex}",
            user_id=user_id,
            title=title,
        )
        db.threads.insert_one(record.model_dump())
        return record

    def update_thread(self, thread_id: str, user_id: str, **kwargs) -> None:
        db = _db()
        kwargs["updated_at"] = datetime.now(timezone.utc)
        db.threads.update_one(
            {"thread_id": thread_id, "user_id": user_id},
            {"$set": kwargs},
        )

    def list_threads(self, request: ThreadListRequest) -> list[ThreadRecord]:
        db = _db()
        docs = list(
            db.threads.find(
                {"user_id": request.user_id},
                sort=[("updated_at", -1)],
                limit=request.limit,
            )
        )
        for doc in docs:
            doc.pop("_id", None)
        return [ThreadRecord(**doc) for doc in docs]

    def save_message(self, message: MessageRecord) -> None:
        db = _db()
        db.messages.insert_one(message.model_dump())
        db.threads.update_one(
            {"thread_id": message.thread_id},
            {
                "$inc": {"message_count": 1, "total_tokens": message.token_count},
                "$set": {"updated_at": datetime.now(timezone.utc)},
            },
        )

    def get_thread_messages(self, thread_id: str, limit: int = 40) -> list[MessageRecord]:
        db = _db()
        docs = list(
            db.messages.find(
                {"thread_id": thread_id},
                sort=[("created_at", 1)],
                limit=limit,
            )
        )
        for doc in docs:
            doc.pop("_id", None)
        return [MessageRecord(**doc) for doc in docs]

    def generate_title(self, first_message: str) -> str:
        words = first_message.strip().split()
        title = " ".join(words[:8])
        if len(words) > 8:
            title += "..."
        return title or "Untitled thread"


thread_service = ThreadService()
