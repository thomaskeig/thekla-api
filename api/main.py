from sanic import Sanic, redirect, request
from bs4 import BeautifulSoup
import requests

app = Sanic()

@app.route('/')
def root():
    return redirect("https://github.com/thomaskeig/thekla-api", code=302)


@app.route('/remainingTickets', methods=['GET'])
async def remainingTickets():
    event_index = request.args.get('event_index', default='0')
    date = request.args.get('date', default='2024-05-04')

    if event_index == '1':
        event = 'pop-confessional-bristol-tickets'
    else:
        event = 'pressure-bristol-tickets'

    url = f'https://www.alttickets.com/{event}/bristol-thekla/{date}-21-30'
    print(url)

    response = requests.get(url)

    # Return an error if AltTickets can't find an event
    if response.status_code != 200:
        return 'Error while finding event.', response.status_code

    soup = BeautifulSoup(response.text, 'html.parser')
    select_element = soup.find('select', class_='ticket_qty_selection')  # Find the select element

    # If tickets are available
    if select_element is not None:
        options = select_element.find_all('option')  # Get all the options
        values = [int(option['value']) for option in options]  # Extract the values as integers
        tickets_available = max(values)

    else:
        tickets_available = 0

    # Create JSON object
    json_str = {"event": event.replace('-bristol-tickets', ''), "date": date, "sold_out": (tickets_available==0), "tickets_remaining": tickets_available, "exact_amount_unknown": (tickets_available==10)}

    return json_str, 200