# FastAPI Project Template

This is a template for starting a FastAPI project.

## Setup

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Project Structure

- `app/main.py`: The entry point of the application.
- `app/routes.py`: API routes.
- `app/models.py`: Pydantic models.
- `app/config.py`: Configuration management.
- `.env`: Environment variables.
