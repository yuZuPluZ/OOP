class Event:
    events = []

    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date
        self.hall = None
        Event.events.append(self)

    def get_event_details(self):
        return f"{self.name} on {self.date} at {self.hall}"

    @classmethod
    def get_all_event_details(cls):
        return "\n".join(event.get_event_details() for event in cls.events)

class Hall:

    halls = []

    def __init__(self, hall_id, name, size, max_capacity):
        self.hall_id = hall_id
        self.name = name
        self.size = size
        self.max_capacity = max_capacity
        self.status = None
        Hall.halls.append(self)

    def get_hall_details(self):
        return f"Hall {self.name} ({self.size}) - Capacity: {self.max_capacity} - Status: {self.status}"

    @classmethod
    def get_all_hall_details(cls):
        return "\n".join(hall.get_hall_details() for hall in cls.halls)

class Organizer:

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__events = []

    def create_event(self, event):
        self.__events.append(event)

    def delete_event(self, event):
        if not self.__events:
            return f"You have no event in management"

        for events in self.__events:
            if events == event:
                self.__events.remove(event)  # Remove event from organizer's list
                if event.hall:  # If the event was assigned a hall, free the hall
                    event.hall.status = "Free"
                    event.hall = None
                print(f"Event {event.name} has been deleted.")
                return  # Exit after deletion to avoid iteration issues

        print(f"Event {event.name} not found in Organizer {self.__name}'s events.")

    def link_hall(self, event, hall):
        if event not in self.__events:
            return f"Organizer {self.__name} cannot assign a hall to an event they didn't create."

        if event.hall is not None:
            return f"Event {event.name} is already assigned to {event.hall.name}."

        if hall.status is not None:
            return f"Hall {hall.name} is currently occupied!"

        event.hall = hall
        hall.status = "Occupied"
        print(f"Organizer {self.__name} assigned {event.name} to {hall.name}.")

    def unlink_hall(self, event):
        if not self.__events:  # Check if organizer has events
            return "You have no events under management."

        if event not in self.__events:
            return f"Organizer {self.__name} cannot unlink a hall from an event they didn't create."

        if not event.hall:  # Check if the event has a hall assigned
            return f"Event {event.name} is not assigned to any hall."

        hall = event.hall  # Store the hall before unlinking
        event.hall = None  # Unlink the hall
        hall.status = "Free"  # Mark the hall as available again

        return f"Hall {hall.name} has been unlinked from event {event.name}."

    def get_all_hall_details(self):
        return Hall.get_all_hall_details()

    def get_all_event_details(self):
        return Event.get_all_event_details()

    @property
    def events(self):
        return self.__events

event_list = []
hall_list = []
organizer_list = []

def create_instance():

    organizer_list.append(Organizer('001','John'))
    organizer_list.append(Organizer('002', 'Adam'))
    organizer_list.append(Organizer('003', 'Sabrina'))

    hall_list.append(Hall('001', "Main Hall", "Large", 500))
    hall_list.append(Hall('002', "Side Hall", "Medium", 300))
    hall_list.append(Hall('003', "Sub Hall", "Small", 100))

    event_list.append(Event('001','Concert','12-01-2025'))
    event_list.append(Event('002', 'Art gallery', '13-01-2025'))
    event_list.append(Event('003', 'Conference', '14-01-2025'))
    event_list.append(Event('004', 'Fashion', '15-01-2025'))


    #eventorganizer_list.append('John', )

create_instance()
# print(Hall.get_all_hall_details())
# print(Event.get_all_event_details())

#Create Events
organizer_list[0].create_event(Event('001', 'Concert', '12-01-2025'))
organizer_list[1].create_event(Event('002', 'Art gallery', '13-01-2025'))
print(organizer_list[0].events[0].get_event_details())

#Link hall
organizer_list[0].link_hall(organizer_list[0].events[0], hall_list[0])

#Link an event that they are not the creator
print(hall_list[0].status)
print(organizer_list[0].link_hall(event_list[1], hall_list[0]))

#Link an occupied hall
print(organizer_list[1].link_hall(organizer_list[1].events[0], hall_list[0]))

#Link an event that already signed to a hall
organizer_list[1].link_hall(organizer_list[1].events[0], hall_list[1])
print(organizer_list[1].link_hall(organizer_list[1].events[0], hall_list[2]))

#Delete unmanaged event
organizer_list[0].delete_event(event_list[1])

#Delete Event
organizer_list[0].delete_event(organizer_list[0].events[0])

#Unlink hall
organizer_list[0].create_event(Event('001', 'Concert', '12-01-2025'))
organizer_list[0].link_hall(organizer_list[0].events[0], hall_list[0])
print(organizer_list[0].unlink_hall(organizer_list[0].events[0]))