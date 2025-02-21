# thekla-api
A selfhostable API to show how many tickets are remaining for Thekla Thursday & Saturday club nights.
You can also access this API using the root domain thekla.thomaskeig.com

**UPDATE:** Due to Thekla moving their ticket sales to Fatsoma, this API no longer works, as it queries AltTickets.

## Setup:
- Create a Vercel project with [this](https://vercel.com/new/clone?s=https%3A%2F%2Fgithub.com%2Fthomaskeig%2Fthekla-api&showOptionalTeamCreation=false) link.
- Deploy your project through Vercel.

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