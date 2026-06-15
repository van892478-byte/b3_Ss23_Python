def hien_thi_logistics(flights):
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    if not flights:
        print("Không có chuyến bay nào.")
        return
        
    index = 1
    for f in flights:
        so_nguyen = f["passengers"] // 10
        so_du = f["passengers"] % 10
        
        if so_du > 0:
            thung_nuoc = so_nguyen + 1
        else:
            thung_nuoc = so_nguyen
            
        print(f"{index}. Mã: {f['flight_id']} | Khởi hành: {f['depart_time']} | Số khách: {f['passengers']} | Dự phòng: {thung_nuoc} thùng nước.")
        index += 1
