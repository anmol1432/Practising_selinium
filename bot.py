from booking_bot.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
