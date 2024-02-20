from passlib.context import CryptContext
from passlib.exc import UnknownHashError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def password_hash(password):
    return pwd_context.hash(password)


def verify_hashed_password(db_password, user_password):
    print(f"Stored Hash: {db_password}")
    print(f"User Password: {user_password}")
    try:
        return pwd_context.verify(user_password, db_password)
    except UnknownHashError as e:
        print(f"Error: Unknown Hash - {e}")
        return False
