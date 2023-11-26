from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt import PyJWTError as JWTError
import datetime
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 支払い詳細モデルの例
class PaymentDetails(BaseModel):
    card_number: str
    expiration_date: datetime.date
    cvv: str

# ユーザーモデルの例
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = False

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# 現在のユーザーを取得する関数
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return User(username=username)
    except JWTError:
        raise credentials_exception


@app.get("/products/")
async def read_products(skip: int = 0, limit: int = 10):
    # データベースから商品を取得して返す
    return products[skip : skip + limit]

@app.get("/products/{product_id}")
async def read_product(product_id: int):
    # データベースから特定の商品を取得して返す
    return product


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # ユーザー認証を行う
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

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

