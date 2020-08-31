import uuid


def get_randomcode():
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code
