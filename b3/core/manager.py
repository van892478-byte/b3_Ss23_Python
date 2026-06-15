import datetime

def check_duplicate_id(flight_id, flight_list):
    id_chuan = flight_id.strip().upper()
    for f in flight_list:
        if f["flight_id"] == id_chuan:
            return True
    return False

def tiep_nhan_chuyen_bay(flights):
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    flight_id = input("Nhập mã chuyến bay: ").strip().upper()
    
    if check_duplicate_id(flight_id, flights):
        print("Lỗi: Mã chuyến bay đã tồn tại!")
        return

    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        depart_time = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ").strip()
        datetime.datetime.fromisoformat(depart_time)
        duration_min = int(input("Nhập số phút bay: "))
    except ValueError:
        print("Sai định dạng! Vui lòng kiểm tra lại số lượng hoặc định dạng thời gian (YYYY-MM-DD HH:MM:SS).")
        return

    new_flight = {
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time,
        "duration_min": duration_min
    }
    flights.append(new_flight)
    print(f">> Thêm chuyến bay {flight_id} thành công!")