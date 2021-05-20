import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from api.router import api_router
from settings import LOGGER_NAME


logger = logging.getLogger(LOGGER_NAME)


app = FastAPI()
app.include_router(api_router)
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.add_middleware(TrustedHostMiddleware,
                   allowed_hosts=["*"])


if __name__ == "__main__":
    import uvicorn

    logger.info("Init app")

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
