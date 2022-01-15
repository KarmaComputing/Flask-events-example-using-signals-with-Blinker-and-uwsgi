# Flask events example using signals with Blinker and uwsgi 

Here we have an example of events in Flask using blinker signals and uwsgi.

> For a more minimal example see: https://github.com/chrisjsimpson/python-blinker-example

You have a new order and you need to tell people about it

- The office needs to know
- The customer needs an email
- Maybe something else, you can create as many listeners
  as you like!


# Setup 

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Run

```
source venv/bin/activate
uwsgi --ini config.ini --py-autoreload 1
```

## Help my tasks are blocking everything

Your subscribers need to be non blocking
see: 
https://github.com/chrisjsimpson/flask-background-task-queue
