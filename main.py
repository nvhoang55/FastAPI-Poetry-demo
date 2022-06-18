import uvicorn
from decouple import config

if __name__ == '__main__':
    HOST = config('HOST')
    PORT = config('PORT', cast=int)

    # uvicorn.run("app:app", host="0.0.0.0", port=8000)
    uvicorn.run("app.app:app", host=HOST, port=PORT, reload=True)
