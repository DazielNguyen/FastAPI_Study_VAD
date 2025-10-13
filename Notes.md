# Tóm tắt phần kết nối Database
- Tài liệu tham khảo: [https://fastapi.tiangolo.com/tutorial/sql-databases/]
- FastAPI nó sẽ work với bất kỳ database nào và bất kỳ thư viện nào tương tác đến database đó
- Thuật ngữ phổ biến là họ dùng thư viện **ORM**: (object-relational-mapping) 
- Để dễ hiểu phần class PET nó sẽ convert và mapping với objects trong code và nó biểu diễn bảng SQL là pets. 
- Khi bạn tạo một bảng giống như việc khai báo 1 class
- **SQLAlchemy** là một thư viện ORM phổ biến nhất trong Python
- Dùng Table Plus để check database

## Các bước thực hiện
- STEP 1: Connecting
    + Tạo 1 file tên database.py
    + Tạo 1 file database tên blog.db
- Sau đó chúng ta bắt đầu set up kết nối 
- Cách Run Server
```
uvicorn app:main --reload
>database.py

```
from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL = 'sql:///./blog.db
engine = create_engine(SQLALCHEMY_DATABASE_UR, connect_args={"check_same_thread":False})

```

- STEP 2: Declare a Mapping
- Tiếp tục đoạn code 

>database.py
```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite URL for the database
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'  # relative path
# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) 
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a base class for declarative class definitions
Base = declarative_base()
```
- STEP 3: File model dùng để tạo bảng
    + Vào TablePlus tải về trên máy
    + Create a new connection 
    + Chọn SQLite
    + Đặt tên tuy chọn 
    + Sau đó select cái path database đã tạo có trong project. Như mình đã tạo là blog.db
    + Nhấn Connect

- Tạo 1 file tên models.py để tạo table

>models.py

```
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

# Define the Blog model, every model should inherit from Base
class Blog(Base):
    __tablename__ = 'blogs' # Tên bảng trong database
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
```
- Sau đó vô main bỏ thêm dòng này vào 
```
from. import schemas, models
from database import engine
# Create the database tables
models.Base.metadata.create_all(engine)
```
- Rồi sau đó vào TablePlus check xem có bảng hay chưa. 
- STEP 4: File schemas.py để validate data
- Tạo 1 file tên schemas.py
- Trong file models.py chúng ta khai báo các bảng trong database
- Trong file schemas.py chúng ta khai báo các class để validate 