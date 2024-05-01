# thekla-api
A selfhostable API to show how many tickets are remaining for Thekla Thursday & Saturday club nights.
## Setup:
- Clone the repository.
- Install the requirements with `python -m pip install -r requirements.txt`
- Edit the settings.yml file to change your server port and more.
- Run the main.py file on your webserver.

## Endpoint:
[GET] /remainingTickets
### Parameters:
**event_index:** Index from 0 to 1 for the event type. 0 is Pressure, 1 is Pop Confessional
**date:** The date of the event in the format YYYY-MM-DD (Eg: 2024-05-04)
**Example URI:** https://example.com/remainingTickets?event_index=1&date=2024-05-04
### Example Response:

    {"date": "2024-05-04", "event": "pop-confessional", "tickets_remaining": 10}
**date:** The date of the event
**event:** The event name
**tickets_remaining:** How many tickets are left.
### Limitations:
Due to how the ticket number is determined, if the tickets remaining is above 10, it is not possible to tell how many tickets are remaining. In this case the ticket count is simply shown as 10.