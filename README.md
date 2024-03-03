# NGL Spammer

This is a Flask application that uses the NGLWrapper to send questions to the NGL API. The application allows users to send a random text or a specific text multiple times.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python
- pip

### Installing

1. Clone the repository
```bash
git clone https://github.com/birdfromhell/NGL-Spammer.git
```
2. Change directory
```bash
cd NGL-Spammer
```
3. Install the requirements
```bash
pip install -r requirements.txt
```


## Running the Application

To run the application, use the following command:
```bash
python app.py
```

## Application Routes

- `/` - The home route where you can choose the mode and input the necessary details.
- `/submit` - The route where the form data is submitted and processed.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Python](https://www.python.org/) - The programming language used

## Authors

- birdfromhell

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details