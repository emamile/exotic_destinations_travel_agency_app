import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.arrangements.routes import accommodation_router, arrangement_router, excursion_router
from app.database.db import Base, engine
from app.users.routes import mandatory_check_router, traveler_router, user_router
from app.world_destinations.routes import state_router, world_destination_router

Base.metadata.create_all(bind=engine)


def init_app():
    """
    `init_app()` is a function that creates an instance of FastAPI and then includes all the routers that we created in the
    previous step
    :return: The app is being returned.
    """
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(traveler_router)
    app.include_router(world_destination_router)
    app.include_router(state_router)
    app.include_router(arrangement_router)
    app.include_router(accommodation_router)
    app.include_router(excursion_router)
    app.include_router(mandatory_check_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def itbc_student_project():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
