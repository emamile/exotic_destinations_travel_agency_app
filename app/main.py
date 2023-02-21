import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.database.db import Base, engine
from app.users.routes import user_router
from app.users.routes import traveler_router
from app.world_destinations.routes import world_destination_router
from app.arrangements.routes import arrangement_router


Base.metadata.create_all(bind=engine)


def init_app():

    app = FastAPI()
    app.include_router(user_router)
    app.include_router(traveler_router)
    app.include_router(world_destination_router)
    app.include_router(arrangement_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def itbc_student_project():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)

