from sqlmodel import Session, SQLModel, create_engine

from src.configs import configs

engine = create_engine(
    configs.DATABASE_URL, connect_args={"check_same_thread": False}
)


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
