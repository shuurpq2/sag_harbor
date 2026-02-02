from sqlalchemy.orm import Session, joinedload
from fastapi.responses import RedirectResponse
from fastapi import status
from ..models.shortener import UrlsPair


class ShortenerRepo:
    def __init__(self, db: Session):
        self.db = db


    def get_pair_by_slug(self, slug: str) -> UrlsPair:
        urls_pair = self.db.query(UrlsPair).filter(UrlsPair.slug == slug).first()
        return urls_pair
    

    def get_pair_by_long_url(self, long_url: str) -> UrlsPair:
        urls_pair = self.db.query(UrlsPair).filter(UrlsPair.long_url == long_url).first()
        return urls_pair


    def add_pair_to_db(self, slug: str, long_url: str) -> UrlsPair:
        new_urls_pair = UrlsPair(slug=slug, long_url=long_url)
        self.db.add(new_urls_pair)
        self.db.commit()
        self.db.refresh(new_urls_pair)
        return new_urls_pair
    

    def get_long_url_by_slug(self, slug: str) -> str | None:
        pair = self.get_pair_by_slug(slug=slug)
        if not pair:
            return None
        long_url = pair.long_url
        return long_url