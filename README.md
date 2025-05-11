# Test-Bot FastAPI Application

A simple FastAPI application that displays a welcome message.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Jinja2

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Run the application with:

```
python main.py
```

Or using Uvicorn directly:

```
uvicorn main:app --reload
```

The application will be available at http://localhost:8000

## Testing

This project includes automated tests using pytest. To run the tests:

```
pytest
```

For more verbose output:

```
pytest -v
```

### Pre-commit Hook

A pre-commit hook is included to run tests automatically before each commit. To set it up:

1. Run the setup script:

   ```
   powershell -ExecutionPolicy Bypass -File .\setup_hooks.ps1
   ```

2. Now tests will run automatically before each commit, preventing commits if tests fail.

### CI/CD Integration

This project includes a GitHub Actions workflow that automatically runs tests on push and pull requests to the main branch. See `.github/workflows/pytest.yml` for details.

## Docker

This application can be run in a Docker container. There are two ways to run it:

### Using Docker directly

1. Build and run the Docker container:

   ```
   powershell -ExecutionPolicy Bypass -File .\docker-build.ps1
   ```

   Or manually:

   ```
   docker build -t test-bot-app .
   docker run -d -p 8000:8000 --name test-bot-container test-bot-app
   ```

2. Access the application at http://localhost:8000

3. To stop the container:
   ```
   docker stop test-bot-container
   docker rm test-bot-container
   ```

### Using Docker Compose

1. Start the services:

   ```
   powershell -ExecutionPolicy Bypass -File .\docker-compose-up.ps1
   ```

   Or manually:

   ```
   docker-compose up -d
   ```

2. Access the application at http://localhost:8000

3. To stop the services:
   ```
   docker-compose down
   ```
