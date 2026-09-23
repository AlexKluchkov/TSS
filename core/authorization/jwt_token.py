from datetime import datetime, timedelta, timezone

import jwt

# В готовом проекте SECRET_KEY нужно брать из переменных окружения, а не хранить в коде.
SECRET_KEY = "changeme"
ALGORITHM = "HS256"

def create_access_token(user_id: int) -> str:
    expires = datetime.now(timezone.utc) + timedelta(minutes=30)

    payload = {
        "sub": str(user_id),
        "exp": expires,
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)