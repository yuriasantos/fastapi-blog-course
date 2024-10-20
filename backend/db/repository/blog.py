from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int):
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

def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active==True).all()
    return blogs

def update_blog_by_id(id: int, blog:UpdateBlog, db: Session, author_id: int):
    existing_blog = db.query(Blog).filter(Blog.id == id).first()
    if not existing_blog:
        return {'error': f'Blog with id {id} not found.'}
    if not existing_blog.author_id == author_id:
        return {'error': 'Not authorized to update this blog.'}
    existing_blog.title = blog.title
    existing_blog.content = blog.content
    try:
        db.add(existing_blog)
        db.commit()
        db.refresh(existing_blog)
    except Exception as e:
        db.rollback()
    return existing_blog

def delete_blog_by_id(id: int, db: Session, author_id: int):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        return {'error': f'Could not find a blog with id {id}.'}
    elif not blog.first().author_id == author_id:
        return {'error': 'Not authorized to delete this blog.'}
    else:
        blog.delete()
        db.commit()
        return {'message': f'Successfully deleted blog with id {id}.'}
