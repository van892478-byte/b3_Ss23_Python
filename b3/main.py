from core.logistics import hien_thi_logistics
from core.manager import tiep_nhan_chuyen_bay
from utils.time_helper import tinh_eta
from utils.file_helper import khoi_tao_thu_muc

def main():
    flights = [
        {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
        {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
    ]

    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần")
        print("2. Tiếp nhận chuyến bay mới")
        print("3. Tính thời gian hạ cánh dự kiến (ETA)")
        print("4. Khởi tạo thư mục lưu trữ log hệ thống")
        print("5. Thoát chương trình")
        print("==================================================")
        
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()

        match lua_chon:
            case "1":
                hien_thi_logistics(flights)
            case "2":
                tiep_nhan_chuyen_bay(flights)
            case "3":
                tinh_eta(flights)
            case "4":
                khoi_tao_thu_muc()
            case "5":
                print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
                break
            case _:
                print("Lỗi: Lựa chọn không hợp lệ. Vui lòng nhập lại số từ 1 đến 5.")

if __name__ == "__main__":
    main()