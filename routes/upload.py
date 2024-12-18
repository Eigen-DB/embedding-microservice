import logging
from fastapi import APIRouter
from fastapi import Header
from fastapi import HTTPException
from huggingface_hub import InferenceClient

from helpers import vectors
from schemas.data import Data

router = APIRouter()
inference_client = InferenceClient(
    model="sentence-transformers/all-MiniLM-L6-v2", # get from config
    token="", # use env vars
)

@router.put("/upload")
async def upload_data(data: Data, x_eigen_api_key: str = Header(None)) -> Data:
    embedding = inference_client.feature_extraction(
        text=data.data
    )

    try:
        vectors.insert(
            vector=embedding,
            id=data.id,
            api_key=x_eigen_api_key
        )
    except Exception as err:
        logging.error(err)
        raise HTTPException(status_code=500, detail="Failed to upload data")
    
    return data