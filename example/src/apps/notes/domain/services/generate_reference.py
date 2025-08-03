import uuid


def generate_reference():
    """
    Generates a unique reference for an entity.
    The reference is a UUID4 string.
    """
    return str(uuid.uuid4())
