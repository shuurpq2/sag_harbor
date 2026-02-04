from sqlalchemy.orm import Session
from ..repos.shortener_repo import ShortenerRepo
from ..exeptions import shortener_exeptions
import string
import random


def generate_slug(repo: ShortenerRepo):
    new_slug = ''
    chars = string.ascii_letters + string.digits
    while new_slug == '':
        for _ in range(6):
            new_slug += chars[random.randint(0, len(chars)-1)]
        urls_pair = repo.get_pair_by_slug(slug=new_slug)
        if urls_pair:
            new_slug = ''
    return new_slug


class ShortenerService:
    def __init__(self, db: Session):
        self.repo = ShortenerRepo(db)


    def shorten_url(self, long_url: str) -> str:
        if not '://' in long_url:
            long_url = 'http://' + long_url
        if long_url.endswith('/'):
            long_url = long_url[:-1]
        urls_pair = self.repo.get_pair_by_long_url(long_url=long_url)
        if urls_pair:
            return urls_pair.slug
        slug = generate_slug(self.repo)
        self.repo.add_pair_to_db(slug, long_url)
        return slug


    def get_long_url_by_slug(self, slug: str) -> str:
      long_url = self.repo.get_long_url_by_slug(slug=slug)
      if not long_url:
          raise shortener_exeptions.NoLongUrlFoundError()
      return long_url