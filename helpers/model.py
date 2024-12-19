import numpy as np
from huggingface_hub import InferenceClient

def perform_inference(inference_client: InferenceClient, model_type: str, data: any) -> np.ndarray: 
    if model_type == "text":
        return inference_client.feature_extraction( # use the hugging face API to find the supported embedding task for the chosen model
            text=data
        )
    elif model_type == "image":
        pass
    elif model_type == "video":
        pass
    else:
        raise Exception("invalid model type") # validate .env at startup