from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class Note:
    reference: uuid.UUID
    title: str
    content: str
    created_at: datetime = datetime.now()
