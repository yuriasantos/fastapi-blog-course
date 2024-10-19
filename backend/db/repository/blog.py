from sqlalchemy.orm import Session
from schemas.blog import CreateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(title=blog.title,
                slug=blog.slug,
                content=blog.content,
                author_id=author_id)
    try:
        db.add(blog)
        db.commit()
        db.refresh(blog)
    except Exception as e:
        db.rollback()
    return blog

def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        return None
    return blog
