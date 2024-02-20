from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session
from packages.models import Blog, User
from packages.dependency import get_db
from sqlalchemy.orm import selectinload, joinedload
from packages import sqlmodel_schemas
from packages.jwttoken import get_current_user
from sqlmodel import select
from typing import Generator, TypeVar

# from packages import schemas


router = APIRouter()


@router.post("/create_blog/")
async def create_blog(blog: Blog, db: Session = Depends(get_db),
                      current_user: sqlmodel_schemas.User = Depends(get_current_user)):
    try:
        existing_user = db.exec(select(User.email == current_user.email)).first()
        if existing_user:
            new_blog = Blog(title=blog.title, content=blog.content, user_id=current_user.id)
            db.add(new_blog)
            db.commit()
            db.refresh(new_blog)
            return new_blog

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    except Exception as e:
        return e


@router.get("/user_blogs/{user_id}/")
async def get_user_blogs(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
            )

        # user_blog = db.query(User).filter(User.id == user_id).options(
        #     selectinload(User.blogs)).first().blogs.filter(Blog.title == "prasanna")

        # filtered_blogs = [
        #     blog for blog in user_blog if str(blog.title).startswith("p")
        # ]

        blog = (
            db.query(User)
            .filter(User.id == user_id, Blog.title.startswith("p"))
            .options(selectinload(User.blogs))
            .first()
        )
        filtered_blogs = blog.blogs.filter(Blog.title == "prasanna").all()

        return filtered_blogs



        # blogs = db.query(User)
        #     .options(selectinload(User.blogs))
        #     .filter(Blog.title.icontains("S"))
        #     .all()
        #
        # return blogs

    except Exception as e:
        print("Error Happening")
        return JSONResponse(
            content={"error": str(e)},
            status_code=404,
        )


@router.get("/get_blog/")
async def get_blog(db: Session = Depends(get_db), current_user: sqlmodel_schemas.User = Depends(get_current_user)) :
    try:
        blogs = db.exec(select(Blog)).all()
        print(f"current User is{current_user}")
        if blogs:
            return JSONResponse(
                content={"data": blogs},
                status_code=status.HTTP_200_OK
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zero Blog")

    except Exception as e:
        print("Error Happening")
        return JSONResponse(
            content={"error": str(e)},
            status_code=404,
        )

