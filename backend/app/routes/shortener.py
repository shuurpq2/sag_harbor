from fastapi import APIRouter, Depends, status, Request
from ..database import get_db
from ..services.shortener_services import ShortenerService
from sqlalchemy.orm import Session



router = APIRouter(
    prefix='/api/shortener',
    tags=['shortener']
)


@router.post('/', response_model=str, status_code=status.HTTP_200_OK)
def shorten_url(long_url: str, db: Session = Depends(get_db)):
    service = ShortenerService(db)
    return service.shorten_url(long_url=long_url)


@router.get('/{slug}', response_model=str | None, status_code=status.HTTP_200_OK)
def get_long_url(slug: str, db: Session = Depends(get_db)):
    service = ShortenerService(db)
    return service.get_long_url_by_slug(slug=slug)