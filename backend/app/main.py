import os
import sys

# Ensure project root is in sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from backend.app.core.config import settings
from backend.app.core.exceptions import AppException
from backend.app.api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Enterprise Agentic AI Workforce with MCP, M365, TrekkSoft & HITL Safety Control"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API v1 Router
app.include_router(api_router, prefix=settings.API_V1_STR)

# Global Exception Handler
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.message}
    )

# Static Page Fallback Routes for Development & Classic UI
@app.get("/", response_class=HTMLResponse)
@app.get("/login", response_class=HTMLResponse)
@app.get("/login.html", response_class=HTMLResponse)
def get_login_page():
    """Serve the dedicated Login & Registration / Sign In Page on root launch."""
    login_path = os.path.join(root_dir, "login.html")
    if os.path.exists(login_path):
        return FileResponse(login_path)
    return HTMLResponse("<h1>Rishan AI Login</h1><p>Login HTML not found.</p>")

@app.get("/dashboard", response_class=HTMLResponse)
@app.get("/dashboard.html", response_class=HTMLResponse)
def get_dashboard():
    """Serve the Web Dashboard AI UI."""
    dashboard_path = os.path.join(root_dir, "dashboard.html")
    if os.path.exists(dashboard_path):
        return FileResponse(dashboard_path)
    return HTMLResponse("<h1>Rishan AI Platform</h1><p>Dashboard HTML not found.</p>")

@app.get("/apps", response_class=HTMLResponse)
@app.get("/explore-apps", response_class=HTMLResponse)
@app.get("/explore.html", response_class=HTMLResponse)
def get_explore_apps():
    explore_path = os.path.join(root_dir, "explore.html")
    if os.path.exists(explore_path):
        return FileResponse(explore_path)
    return HTMLResponse("<h1>Rishan AI Apps</h1><p>Explore HTML not found.</p>")

@app.get("/resources", response_class=HTMLResponse)
@app.get("/resources.html", response_class=HTMLResponse)
def get_resources_page():
    resources_path = os.path.join(root_dir, "resources.html")
    if os.path.exists(resources_path):
        return FileResponse(resources_path)
    return HTMLResponse("<h1>Rishan AI Resources</h1><p>Resources HTML not found.</p>")

@app.get("/enterprise", response_class=HTMLResponse)
@app.get("/enterprise.html", response_class=HTMLResponse)
def get_enterprise_page():
    enterprise_path = os.path.join(root_dir, "enterprise.html")
    if os.path.exists(enterprise_path):
        return FileResponse(enterprise_path)
    return HTMLResponse("<h1>Rishan AI Enterprise</h1><p>Enterprise HTML not found.</p>")

@app.get("/team", response_class=HTMLResponse)
@app.get("/team-solutions", response_class=HTMLResponse)
@app.get("/team.html", response_class=HTMLResponse)
def get_team_solutions_page():
    team_path = os.path.join(root_dir, "team.html")
    if os.path.exists(team_path):
        return FileResponse(team_path)
    return HTMLResponse("<h1>Rishan AI Team Solutions</h1><p>Team HTML not found.</p>")

@app.get("/{filename}.html", response_class=HTMLResponse)
def get_any_html_page(filename: str):
    target_path = os.path.join(root_dir, f"{filename}.html")
    if os.path.exists(target_path):
        return FileResponse(target_path)
    return HTMLResponse(f"<h1>404 Not Found</h1><p>Page '{filename}.html' not found.</p>", status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
