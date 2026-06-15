import datetime

def tinh_eta(flights):
    print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    flight_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    
    chuyen_bay = None
    for f in flights:
        if f["flight_id"] == flight_id:
            chuyen_bay = f
            break
            
    if chuyen_bay is None:
        print("Không tìm thấy mã chuyến bay này!")
        return

    dep_time = datetime.datetime.fromisoformat(chuyen_bay["depart_time"])
    eta = dep_time + datetime.timedelta(minutes=chuyen_bay["duration_min"])
    
    print(f"-> Chuyến bay {flight_id} cất cánh lúc: {chuyen_bay['depart_time']}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {str(eta)}")