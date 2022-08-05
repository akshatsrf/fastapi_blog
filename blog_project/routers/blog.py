from fastapi import APIRouter, Depends, status
from typing import List
from blog_project.oauth2 import get_current_user
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def specific(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.display(id, db)
