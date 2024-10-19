from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog
from db.repository.blog import create_new_blog, retrieve_blog


router = APIRouter()

@router.post(path='/', response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog

@router.get('/{id}', response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
    return blog
