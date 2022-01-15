from blinker import signal
from flask import Flask, request, render_template

"""
Here we have an example of using blinker signals.

You have a new order and you need to tell people about it

- The office needs to know
- The customer needs an email
- Maybe something else, you can create as many listeners
  as you like!
"""

# First create a named signal for the new order event
event_new_order = signal("new-order")

# Then create your listeners (also known as 'subscribers'):


# Create a listener to tell the office
def subscriber_tell_the_office(sender):
    print(f"Hey everyone, there's a new order: {sender}")


# Create a listener to email the customer
def subscriber_email_the_customer(sender):
    print(f"Sending email to customer. {sender}")
    # Code to send email would go here


# Connect all the listeners to the signal
event_new_order.connect(subscriber_tell_the_office)
event_new_order.connect(subscriber_email_the_customer)


app = Flask(__name__)


@app.route("/")
def new_order():
    # Emmit a signal to all connected subscribers
    order = request.args.get("order")
    if order == "chocolate":
        event_new_order.send("Chocolate bars")
    elif order == "cake":
        event_new_order.send("Cake!")

    if order is not None:
        return "Order placed!"

    return render_template("new-order.html")
