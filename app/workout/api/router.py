from fastapi import APIRouter
from strawberry.fastapi import GraphQLRouter
from app.workout.schemas.schemas import schema

router = APIRouter()

graphql_app = GraphQLRouter(schema)

router.include_router(graphql_app, prefix="/graphql")
