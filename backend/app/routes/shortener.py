from fastapi import APIRouter, Depends, status, Request, HTTPException
from ..database import get_db
from ..services.shortener_services import ShortenerService
from sqlalchemy.orm import Session
from ..exeptions import shortener_exeptions



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
    try:
      long_url = service.get_long_url_by_slug(slug=slug)
      return long_url
    except shortener_exeptions.NoLongUrlFoundError:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No long URL found with slug \'{slug}\'')