from app.api.v1.users.routes import router as users_router

ROUTES = [
    (users_router , "/users", ["Users"]),


]