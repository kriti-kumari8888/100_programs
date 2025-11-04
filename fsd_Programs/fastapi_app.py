"""
fastapi_app.py
Tiny FastAPI example. To run: pip install fastapi uvicorn && uvicorn fastapi_app:app --reload
"""
try:
    from fastapi import FastAPI
    from pydantic import BaseModel
    app = FastAPI()

    class Item(BaseModel):
        name: str
        price: float

    @app.get('/')
    def read_root():
        return {'msg': 'Hello from FastAPI'}

    @app.post('/items')
    def create_item(item: Item):
        return {'item_received': item}

except Exception:
    if __name__ == '__main__':
        print('FastAPI or pydantic not installed. Install with: pip install fastapi pydantic uvicorn')
