import math

def hien_thi_logistics(flights):
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    if not flights:
        print("Không có chuyến bay nào.")
        return
        
    index = 1
    for f in flights:
        thung_nuoc = math.ceil(f["passengers"] / 10)
        print(f"{index}. Mã: {f['flight_id']} | Khởi hành: {f['depart_time']} | Số khách: {f['passengers']} | Dự phòng: {thung_nuoc} thùng nước.")
        index += 1