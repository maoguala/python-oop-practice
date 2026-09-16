class Car:
    def __init__(self, brand, color, speed, plate_number):
        self.brand = brand
        self.color = color
        # 透過 setter 設定初始速度，確保資料驗證生效
        self.speed = speed
        # 私有化車牌，避免外部隨意篡改
        self._plate_number = plate_number

    # 1. speed 屬性的封裝 (Getter & Setter)
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        # 轉型並進行邏輯驗證
        try:
            val = int(value)
            if val < 0:
                raise ValueError("Speed cannot be negative.")
            self._speed = val
        except ValueError as e:
            print(f"Invalid speed input: {value}. Setting speed to 0.")
            self._speed = 0

    # 2. plate_number 只讀屬性 (只提供 Getter，防止被修改)
    @property
    def plate_number(self):
        return self._plate_number

    # 3. 封裝行為邏輯：傳回 boolean，不做 print，提高代碼重用性
    def is_out_of_speed_limit(self, limit=60) -> bool:
        return self._speed > limit


# --- 外部呼叫與應用 ---

s = input("Input brand, color, speed and plate_number (With Space): ").split()

if len(s) == 4:
    vehicle = Car(*s)

    # 邏輯判斷與顯示分離
    if vehicle.is_out_of_speed_limit(60):
        print(f"\nYes, Get Slowly {vehicle.plate_number}!\n")
    else:
        print(f"\nSafe! {vehicle.plate_number}\n")
else:
    print("Invalid input format. Please provide exactly 4 arguments.")