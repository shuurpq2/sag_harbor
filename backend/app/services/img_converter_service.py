from sqlalchemy.orm import Session
from PIL import Image
from fastapi.responses import FileResponse
from uuid import uuid4


class ImgConverterService:
  def __init__(self, db: Session):
    self.db = db


  def convert_img(self, img_url: str, format: str):
    dot_index = img_url.rfind('.')
    last_slash_index = img_url.rfind('\\')
    img_id = str(uuid4())[:8]
    img_name = img_url[last_slash_index + 1:dot_index] + img_id
    new_img_url = img_url[:last_slash_index + 1]
    img = Image.open(img_url)
    if img.mode == 'RGBA':
      background = Image.new('RGB', img.size, (255, 255 ,255))
      background.paste(img, mask=img.split()[3])
      img = background
    img.save(f'{new_img_url}{img_name}.{format}')
    return FileResponse(
      path=f'{new_img_url}{img_name}.{format}',
      media_type=f'image/{format}',
      filename=f'{img_name}.{format}'
    )