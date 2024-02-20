from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException, status
from hashing import password_hash, verify_hashed_password
from packages.custom_exceptions import ObjectDoesNotExist
from packages.models import User
from packages.dependency import get_db
from fastapi.responses import JSONResponse
from packages import schemas
from sqlmodel import select
from packages.jwttoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
# from fastapi_pagination import Page, paginate, add_pagination, LimitOffsetPage


router = APIRouter()


@router.post("/create_user/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        if db.exec(select(User).where(User.email == user.email)).first():
            raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED, detail="Email Already Exist try another")

        hashed_pw = password_hash(user.password)
        user = User(name=user.name, email=user.email, password=hashed_pw)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=404,
        )


@router.get("/get_user/{user_id}/")
def get_user(user_id: int, db: Session = Depends(get_db)):
    # users = db.query(User).filter(User.id == user_id).first()
    # if users:
    #     return users
    # raise ObjectDoesNotExist(detail="User Not found")
    users = db.exec(select(User).where(User.id == user_id))
    if users:
        return users
    raise ObjectDoesNotExist(detail="User Not found")


# Page number pagination example
# @router.get("/get_all_user/}")
# def get_all_users(db: Session = Depends(get_db)) -> Page[User]:
#     users = db.query(User).all()
#     paginated_users = paginate(users)  # Adjust as needed
#     return paginated_users


# LimitOffset Pagination example
# @router.get("/get_all_user/}")
# def get_all_users(db: Session = Depends(get_db)) -> LimitOffsetPage[User]:
#     users = db.query(User).all()
#     paginated_users = paginate(users)  # Adjust as needed
#     return paginated_users


# Custom LimitOffset Pagination Using manually
@router.get("/get_all_user/}")
def get_all_users(db: Session = Depends(get_db), limit: int = 5, offset: int = 0):
    users = db.exec(select(User).limit(limit).offset(offset)).all()
    return users


@router.post("/update_user/{user_id}/")
def update_user(user_id: int, update_data: User, db: Session = Depends(get_db)):
    my_user = get_user(db=db, user_id=user_id)
    if my_user:
        for key, value in update_data.dict(exclude_unset=True).items():
            if key == "password":
                # Hash the new password before updating
                hashed_password = password_hash(update_data.password)
                setattr(my_user, key, hashed_password)
            else:
                setattr(my_user, key, value)
        db.commit()
        return my_user
    raise ObjectDoesNotExist(detail="User Not Updated")


@router.post("/delete_user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.id == user_id)).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None


# c--------------------------code for login --------------------------
@router.post("/login",)
async def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    my_user = db.exec(select(User).where(User.email == user.email))

    if not my_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credential")

    if not verify_hashed_password(user.password, get_user.password):
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail="Incorrect Password")
    return my_user


# Jwt Login
@router.post("/jwt_login/",)
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    my_user = db.exec(select(User).where(User.email == request.username)).first()

    if not my_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credential")

    if not verify_hashed_password(my_user.password, request.password):
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail="Incorrect Password")

    access_token = create_access_token(
        data={"sub": request.username}
    )

    return {"access_token": access_token, "token_type": "bearer"}
