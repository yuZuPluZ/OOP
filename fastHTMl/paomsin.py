class Event:
    def __init__(self, event_id, name, date, hall):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.hall = hall  # ใช้ instance ของ Hall แทน id

    def get_event_details(self):
        return f"{self.name} on {self.date} at {self.hall.get_hall_details()}"


class Hall:
    def __init__(self, hall_id, name, size, max_capacity):
        self.hall_id = hall_id
        self.name = name
        self.size = size
        self.max_capacity = max_capacity

    def get_hall_details(self):
        return f"Hall {self.name} ({self.size}) - Capacity: {self.max_capacity}"


class Zone:
    def __init__(self, zone_id, name, base_price, seats):
        self.zone_id = zone_id
        self.name = name
        self.base_price = base_price
        self.seats = {seat: False for seat in seats}  # False = Available, True = Reserved

    def check_availability(self):
        return [seat for seat, reserved in self.seats.items() if not reserved]

    def reserve_seat(self, seat_id):
        if seat_id in self.seats and not self.seats[seat_id]:
            self.seats[seat_id] = True
            return True
        return False


class Ticket:
    def __init__(self, event, zone, seat_id):
        self.event = event
        self.zone = zone
        self.seat_id = seat_id
        self.price = zone.base_price


class Order:
    def __init__(self, user_id, ticket):
        self.user_id = user_id
        self.ticket = ticket


class BookingSystem:
    def __init__(self):
        self.events = {}
        self.zones = {}
        self.orders = []

    def add_event(self, event):
        self.events[event.event_id] = event

    def add_zone(self, zone):
        self.zones[zone.zone_id] = zone

    def browse_events(self):
        return self.events.values()

    def select_zone(self, event_id, zone_id):
        if zone_id in self.zones:
            return self.zones[zone_id].check_availability()
        return []

    def book_ticket(self, user_id, event_id, zone_id, seat_id):
        if zone_id in self.zones and event_id in self.events:
            zone = self.zones[zone_id]
            if zone.reserve_seat(seat_id):
                ticket = Ticket(self.events[event_id], zone, seat_id)
                order = Order(user_id, ticket)
                self.orders.append(order)
                return ticket
        return None


# ============= ตัวอย่างการใช้งาน =============
system = BookingSystem()

# สร้าง Hall
hall1 = Hall(1, "Main Hall", "Large", 500)

# สร้าง Event และเพิ่มเข้า BookingSystem
event1 = Event(1, "Concert A", "2025-03-10", hall1)
system.add_event(event1)

# สร้างโซนที่นั่งและเพิ่มเข้า BookingSystem
zone_vip = Zone(101, "VIP", 100.0, ["A1", "A2", "A3"])
system.add_zone(zone_vip)

# แสดงรายการ Event
for event in system.browse_events():
    print(event.get_event_details())

# แสดงที่นั่งว่าง
available_seats = system.select_zone(1, 101)
print("Available seats:", available_seats)

# จองที่นั่งถ้ามีที่นั่งว่าง
if available_seats:
    ticket = system.book_ticket(1, 1, 101, available_seats[0])
    if ticket:
        print(f"Booking confirmed: Event {ticket.event.name}, Seat {ticket.seat_id}, Price ${ticket.price}")
    else:
        print("Booking failed.")
