import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Any, Union, Optional, Dict
from jose import jwt, JWTError
from passlib.context import CryptContext
from backend.app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(subject: Union[str, Any], claims: Optional[Dict[str, Any]] = None, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    if claims:
        to_encode.update(claims)
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return {}


def generate_api_key_pair(prefix: str = "atl") -> tuple[str, str, str]:
    """
    Generates a secure API key.
    Returns: (raw_key, masked_key, hashed_key)
    Format: atl_live_32char_random
    """
    rand_bytes = secrets.token_urlsafe(32)
    raw_key = f"{prefix}_live_{rand_bytes}"
    masked_key = f"{prefix}_live_{rand_bytes[:4]}...{rand_bytes[-4:]}"
    hashed_key = hashlib.sha256(raw_key.encode("utf-8")).hexdigest()
    return raw_key, masked_key, hashed_key


def hash_api_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()
