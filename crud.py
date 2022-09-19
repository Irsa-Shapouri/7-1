from sqlalchemy.orm import Session

import models, schemas, exceptions

def get_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).all()


def create_category(db: Session, category: schemas.create_category):
    if not category.name:
        raise exceptions.ExceptionHandler("cat name error")

    db_category = models.Category(
        category_id = category.id,
        category_name = category.name
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
