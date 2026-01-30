import uvicorn
from app.config import settings
from app.config import host


if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        host=host,
        port=8000,
        reload=settings.debug,
        log_level='info',
    )