1. Sơ đồ cấu trúc cây thư mục (Folder Tree):
b2/
│
├── main.py
├── README.md
│
├── core/
│   ├── __init__.py
│   ├── logistics.py
│   └── manager.py
│
└── utils/
    ├── __init__.py
    ├── time_helper.py
    └── file_helper.py
2. Lý do hạn chế dùng from math import *:

Việc dùng dấu * sẽ nạp toàn bộ các hàm của thư viện math vào không gian tên hiện tại, gây ra nguy cơ trùng tên và ghi đè ngầm định lên các hàm hoặc biến do mình tự viết mà không hề báo lỗi, dẫn đến sai lệch logic hệ thống. Sử dụng import math giúp quản lý mã nguồn minh bạch và an toàn hơn.