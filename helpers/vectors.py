import numpy as np
import json
import os
from requests import put
from requests import Response

EIGENDB_ENDPOINT = os.getenv('EIGEN_DB_INSTANCE_URL')

def insert(vector: np.ndarray, id: int, api_key: str) -> Response:
    res = put(
        url=EIGENDB_ENDPOINT + "/vector/insert",
        data=json.dumps({
            "vector": {
                "embedding": vector.tolist(),
                "id": id
            }
        }),
        headers={
            "Content-Type": "application/json",
            "X-Eigen-API-Key": api_key
        }
    )
    
    return res