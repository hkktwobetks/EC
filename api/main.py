from fastapi import FastAPI

app = FastAPI()

# ここに各種エンドポイントを追加します。
@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String, index=True)
    # 他のフィールドも追加...

@app.get("/products/")
async def read_products(skip: int = 0, limit: int = 10):
    # データベースから商品を取得して返す
    return products[skip : skip + limit]

@app.get("/products/{product_id}")
async def read_product(product_id: int):
    # データベースから特定の商品を取得して返す
    return product


from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuthForm):
    # ユーザー認証を行い、JWT トークンを生成して返す
    return {"access_token": token, "token_type": "bearer"}


@app.post("/cart/")
async def add_to_cart(product_id: int, quantity: int, user: User = Depends(get_current_user)):
    # 商品をカートに追加するロジック
    return {"message": "Product added to cart"}


@app.post("/favorites/")
async def add_to_favorites(product_id: int, user: User = Depends(get_current_user)):
    # 商品をお気に入りに追加するロジック
    return {"message": "Product added to favorites"}

@app.post("/pay/")
async def pay(order_id: int, payment_details: PaymentDetails):
    # 支払い処理を行うロジック
    return {"message": "Payment successful"}

