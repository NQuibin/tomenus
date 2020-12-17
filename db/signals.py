from datetime import datetime


def update_updated_at(_, document):
    document.updated_at = datetime.utcnow()
