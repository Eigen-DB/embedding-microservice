import numpy as np
import json
from requests import put

EIGENDB_ENDPOINT = "http://127.0.0.1:8080"

def insert(vector: np.ndarray, id: int, api_key: str) -> None:
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

    if res.status_code != 200:
        raise Exception(f"got non-200 response: {res.content.decode()}")