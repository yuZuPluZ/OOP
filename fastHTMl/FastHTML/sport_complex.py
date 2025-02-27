from fasthtml.common import *
from typing import List, Tuple, Optional
from datetime import datetime, time, timedelta

app, rt = fast_app()

class TimeSlot:
    def __init__(self, start_time: time, end_time: time):
        self.__start_time = start_time
        self.__end_time = end_time
        self.__is_booked = False
        self.__is_pending = False  # ✅ เพิ่มตัวแปรสถานะรอตรวจสอบ

    @property
    def is_booked(self):
        return self.__is_booked

    @property
    def is_pending(self):
        return self.__is_pending

    def set_booked(self, status: bool):
        """ ใช้เปลี่ยนสถานะการจอง """
        self.__is_booked = status

    def set_pending(self, status: bool):
        """ ใช้เปลี่ยนสถานะรอตรวจสอบ """
        self.__is_pending = status

    def __str__(self):
        return f"{self.__start_time.strftime('%H:%M')} - {self.__end_time.strftime('%H:%M')}"

class Field:
    def __init__(self, name: str):
        self.__field_name = name
        self.__time_slots: List[TimeSlot] = []

    @property
    def field_name(self):
        return self.__field_name
    
    def add_time_slot(self, time_slot: TimeSlot):
        self.__time_slots.append(time_slot)
    
    def get_available_time_slots(self) -> List[TimeSlot]:
        return [slot for slot in self.__time_slots if not slot.is_booked]

    def show_time_slots(self):
        print(f"Time slots for {self.__field_name}:")
        for slot in self.__time_slots:
            status = "🔴 Booked" if slot.is_booked else "🟢 Available"
            print(f"  {slot} - {status}")

class FieldType:
    def __init__(self, field_type: str, capacity: int, is_long_duration: bool = False):
        self.__field_type = field_type
        self.__capacity = capacity
        self.__is_long_duration = is_long_duration
        self.__fields: List[Field] = []

    @property
    def field_type(self):
        return self.__field_type
    
    @property
    def capacity(self):
        return self.__capacity
    
    @property
    def fields(self):
        return self.__fields
    
    @property
    def long_duration(self):
        return self.__is_long_duration
    
    def add_field(self, field: Field):
        self.__fields.append(field)
        self._initialize_time_slots(field)
    
    def _initialize_time_slots(self, field: Field):
        start = time(16, 0)  # 16:00
        end = time(20, 0)    # 20:00
        duration = timedelta(hours=2 if self.__is_long_duration else 1)
        
        current = datetime.combine(datetime.today(), start)
        end_datetime = datetime.combine(datetime.today(), end)
        
        while current < end_datetime:
            next_slot = current + duration
            if next_slot <= end_datetime:
                time_slot = TimeSlot(current.time(), next_slot.time())
                field.add_time_slot(time_slot)
            current = next_slot

class SportComplex:
    def __init__(self, name):
        self.__name = name
        self.__field_types: List[FieldType] = []
    
    def add_field_type(self, field_type: FieldType):
        self.__field_types.append(field_type)

    def get_field_type_names(self) -> List[str]:
        return [ft.field_type for ft in self.__field_types]
    
    def show_all_fields(self):
        print(f"\n=== {self.__name} Sports Complex ===")
        for field_type in self.__field_types:
            duration = "2 hours" if field_type.long_duration else "1 hour"
            print(f"\nField Type: {field_type.field_type}")
            print(f"Capacity: {field_type.capacity} fields")
            print(f"Booking Duration: {duration}")
            for field in field_type.fields:
                field.show_time_slots()

def add_data():
    stedium = SportComplex("KMITL")
    
    # Long duration sports (2 hours)
    football_type = FieldType("สนามฟุตบอลหญ้าเทียม", 2, is_long_duration=True)
    futsal_type = FieldType("ฟุตซอล", 2, is_long_duration=True)
    volleyball_type = FieldType("วอลเลย์บอล", 2, is_long_duration=True)
    
    # Short duration sports (1 hour)
    badminton_type = FieldType("แบดมินตัน", 4, is_long_duration=False)
    pingpong_type = FieldType("ปิงปอง", 6, is_long_duration=False)
    petanque_type = FieldType("เปตอง", 2, is_long_duration=False)
    
    # Add fields for each type
    football_type.add_field(Field("สนามฟุตบอลหญ้าเทียม1"))
    football_type.add_field(Field("สนามฟุตบอลหญ้าเทียม2"))
    
    for i in range(1, 5):
        badminton_type.add_field(Field(f"แบดมินตัน{i}"))
    
    for i in range(1, 7):
        pingpong_type.add_field(Field(f"ปิงปอง{i}"))
    
    for i in range(1, 3):
        petanque_type.add_field(Field(f"เปตอง{i}"))
        futsal_type.add_field(Field(f"ฟุตซอล{i}"))
        volleyball_type.add_field(Field(f"วอลเลย์บอล{i}"))
    
    # Add all field types to the sport complex
    field_types = [football_type, badminton_type, pingpong_type, 
                  petanque_type, futsal_type, volleyball_type]
    for field_type in field_types:
        stedium.add_field_type(field_type)
    
    return stedium

# Create and show the sport complex
stedium = add_data()
# stedium.show_all_fields()

# สร้างตัวเลือกวันที่ 7 วันถัดไป
months_th = ["", "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", 
             "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
available_dates = [
    f"{(date_obj := datetime.today() + timedelta(days=i)).day} {months_th[date_obj.month - 1]} {date_obj.year + 543}"
    for i in range(8)
]


@rt("/")
def get():
    return Container(
        H1("สนามกีฬา KMITL"),
        Form(method="post", action="/get_field")(
            Fieldset(
                Label("ประเภทสนามกีฬา",
                    Select(name="field_type")(
                        *[Option(ft, value=ft) for ft in stedium.get_field_type_names()]
                    )
                ),
                Label("วันที่",
                    Select(name="date")(
                        *[Option(date, value=date) for date in available_dates]
                    )
                )
            ),
            Button("จองสนาม", type="submit")
        )
    )

@rt("/get_field")
def post(field_type: str, date: str):
    selected_field_type = next((ft for ft in stedium._SportComplex__field_types if ft.field_type == field_type), None)
    
    if not selected_field_type:
        return Titled("ข้อผิดพลาด", P("ไม่พบประเภทสนามที่เลือก"))

    field_cards = []
    
    for field in selected_field_type.fields:
        time_slots = [
            Button(
                str(slot),
                type="button",
                cls=f"time-slot-button {get_slot_status(slot)}",
                onclick=f"selectTimeSlot('{field.field_name}', '{slot}')"
            )
            for slot in field._Field__time_slots
        ]

        field_cards.append(
            Div(
                P(f"{field.field_name}", cls="field-title"),
                Div(*time_slots, cls="time-slot-container"),
                cls="card-container"
            )
        )

    return Div(
        NotStr(get_style()),  # ✅ เพิ่ม Style และ JavaScript
        Div(
            P("ข้อมูลการจอง", cls="title"),
            Div(
                P(f"สนาม: {field_type}", cls="field-info"),
                P(f"วันที่: {date}", cls="field-info"),
                cls="info-container"
            ),
            *field_cards,
            Div(
                Span("⬜ ว่าง", cls="legend available"),
                Span("🟨 รอเจ้าหน้าที่ตรวจสอบ", cls="legend pending"),
                Span("🟩 มีการจอง", cls="legend booked"),
                cls="legend-container"
            ),
            cls="booking-container"
        )
    )

def get_slot_status(slot):
    if slot.is_booked:
        return "booked"
    elif slot.is_pending:
        return "pending"
    else:
        return "available"

def get_style():
    return """
    <style>
        /* ✅ Container ขนาดคงที่ */
        .booking-container {
            width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background: white;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        .title {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 15px;
        }

        .info-container {
            display: flex;
            justify-content: space-between;
            font-size: 16px;
            margin-bottom: 15px;
        }

        .card-container {
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            margin-bottom: 15px;
            background-color: #f9f9f9;
        }

        .field-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }

        /* ✅ ปุ่มช่วงเวลา */
        .time-slot-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 12px;
        }

        .time-slot-button {
            padding: 12px 16px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
            min-width: 120px;
            text-align: center;
        }

        /* ✅ สีของปุ่ม */
        .available { background-color: #f0f0f0; color: black; }
        .pending { background-color: #f4c542; color: black; }
        .booked { background-color: #4CAF50; color: white; }

        .available:hover { background-color: #e0e0e0; }
        .pending:hover { background-color: #e6b800; }
        .booked:hover { background-color: #388e3c; }

        .legend-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
        }

        .legend {
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 5px;
        }
    </style>

    <script>
        function selectTimeSlot(field, timeSlot) {
            fetch('/book_slot', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ field: field, time_slot: timeSlot })
            })
            .then(response => response.json())
            .then(data => alert(data.message))
            .catch(error => console.error('Error:', error));
        }
    </script>
    """
@rt("/book_slot")
def post():
    try:
        data = request.json  # ✅ อ่าน JSON จาก body
        field = data.get("field")
        time_slot = data.get("time_slot")

        if not field or not time_slot:
            return {"error": "Missing field or time_slot"}, 400

        return {"message": f"จอง {field} เวลา {time_slot} เรียบร้อย"}
    except Exception as e:
        return {"error": str(e)}, 500  # ✅ จับข้อผิดพลาด


serve()
