# Introduction 
This project is used to fetch data from the Google Analytics GA4 API using an AWS Lambda function

# Getting Started
To begin, create a virtual environment at the project directory level and install the needed dependencies, listed in the `requirements.txt` file at the same directory level. Next, add the `credentials.json` file to your project. Finally, set the environment variable for the `GOOGLE_APPLICATION_CREDENTIALS`

# Running the project
Enter `python -m run` in the terminal to run the project

# Build and Test
python -m unittest is used to run the tests. A coverage report can be generated using `coverage run -m unittest`, then running `coverage html` afterwards

