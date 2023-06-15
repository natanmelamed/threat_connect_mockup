import uvicorn
import threat_connect
from fastapi import FastAPI

app: FastAPI = FastAPI()
base_url: str = "/api/v2"
app.include_router(threat_connect.router, prefix=base_url)

if __name__ == '__main__':
    uvicorn.run('threat_connect_main:app', host='0.0.0.0', port=80, reload=True)
