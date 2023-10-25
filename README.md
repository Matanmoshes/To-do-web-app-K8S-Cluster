# todo_web_app1

This is a simple Todo application built with Python and Streamlit. The application allows you to maintain a list of to-do items, and you can deploy and run it within a Docker container.

## Project Structure

- `web.py`: The main Streamlit application file.
- `functions.py`: Contains utility functions for handling the to-do list, like reading from and writing to a file.
- `Dockerfile`: Instructions to Docker for how to build the image for this application.
- `requirements.txt`: Lists all the Python libraries that are required for this application.

## Setup & Run

### Using Docker

1. Make sure you have Docker installed on your machine.
2. Navigate to the project directory.
3. Build the Docker image:
   ```bash
   docker build -t todo-app .
   ```
4. Run the application:
   ```bash
   docker run -p 8501:8501 todo-app
   ```
5. Open a web browser and navigate to `http://localhost:8501` to access the app.

### Without Docker

1. Ensure you have Python installed.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run web.py
   ```
4. Open a web browser and navigate to the link provided in the terminal.

## Contributions

If you would like to contribute or have any suggestions, please fork the repository or open an issue. 



