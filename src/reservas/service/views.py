from .bookings import Fare, Booking, Pax, Buyer
from .users import User

VIEWS = [
    (r"users", User),
    (r"fares", Fare),
    (r"bookings", Booking),
    (r"pax", Pax),
    (r"buyers", Buyer),
]
