import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.database.db import Base, engine
from app.travel_agency.routes import travel_agency_router
from app.users.routes import user_router
from app.world_destinations.routes import world_destination_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(travel_agency_router)
    app.include_router(user_router)
    app.include_router(world_destination_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def itbc_student_project():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
