from fastapi import APIRouter, Depends, status, Request, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from ..database import get_db
from sqlalchemy.orm import Session
from ..services.img_converter_service import ImgConverterService
from PIL.Image import Image
from ..config import settings
import shutil
from pathlib import Path
import os
from uuid import uuid4


router = APIRouter(
    prefix='/api/img_converter',
    tags=['img_converter']
)


@router.post('/', status_code=status.HTTP_200_OK)
async def convert_img(uploaded_img: UploadFile, format: str, db: Session = Depends(get_db)):
  img_id = str(uuid4())[:8]
  dot_index = uploaded_img.filename.index('.')
  uploaded_img_name = uploaded_img.filename[:dot_index]
  uploaded_img_format = uploaded_img.filename[dot_index+1:]
  img_path = os.path.join(settings.static_dir, f'{uploaded_img_name}{img_id}.{uploaded_img_format}')


  with open(img_path, 'wb') as buffer:
    shutil.copyfileobj(uploaded_img.file, buffer)


  img_url = img_path
  service = ImgConverterService(db)
  return service.convert_img(img_url=img_url, format=format)