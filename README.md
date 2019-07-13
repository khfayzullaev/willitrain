# WillItRain

An over engineered tool to deliver the weather notifications and alerts to your phone.

## Getting Started
s
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to run the tool:

- [Dark Sky API](https://darksky.net/dev) to look up the weather anywhere on the globe
- [Nexmo SMS API](https://developer.nexmo.com/) to send an SMS to your phone
- [Poetry](https://github.com/sdispater/poetry) to declare, manage and install Python dependencies

### Installing

#### Install Python dependencies

Poetry will detect if you are inside a virtualenv ( it will create a new virtualenv if one doesn't already exist)  and install the packages accordingly. Poetry uses `pyproject.toml` to replace `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and `Pipfile`.

```bash
$ poetry config settings.virtualenvs.create true
$ poetry config settings.virtualenvs.in-project true
$ poetry install
```

#### Activate virtual environment

Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory.

```bash
$ source .venv/bin/activate
```

#### Add credentials

It’s important to keep credentials such as your Dark Sky API Secret Key  by storing them in a way that prevents unauthorized access. We store them in environment variables which are then accessed from the tool. Add your credentials to `darksky/darksky.env` and `sms/nexmo.env`. You can find their templates in their directories accordingly. Source the credentials:

```bash
source ./darksky/darksky.env
source ./sms/nexmo.env
```

#### Run the tool

```bash
$ python forecast.py --lat 40.730610 --lon -73.935242 --to <your phone number> --from <nexmo virtual phone number>
```
