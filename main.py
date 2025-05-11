from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(title="Test Bot")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Root endpoint that serves the welcome page
    """
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "title": "Welcome to Test-Bot"}
    )

@app.get("/api/welcome")
async def welcome_message():
    """
    API endpoint that returns a welcome message
    """
    return {"message": "Features will add soon !!!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
