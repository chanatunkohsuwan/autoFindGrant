# gotta read the docs more

from sqlalchemy import ForeignKey, DeclarativeBase, Mapped, mapped_column, relationship
import sqlalchemy # for sqlalchemy.null instead of just 'null'

VALUES_TO_NULL = {"N/A", "null", "none", "", None}


class Base(DeclarativeBase):

    def purge_null_data(self, data: dict):
        for key, value in data:
            if type(value) == str: value = value.lower()
            if VALUES_TO_NULL[value]: data[key] = sqlalchemy.null
        return data


class team(Base):
    __tablename__ = "team"
    # team data
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    website_url: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()
    industry: Mapped[str] = mapped_column()
    latitude: Mapped[float] = mapped_column()
    longitude: Mapped[float] = mapped_column()
    worlds: Mapped[str] = mapped_column()
    state: Mapped[str] = mapped_column()
    tier: Mapped[str] = mapped_column()

class sponsor(Base):
    # sponsor
    __tablename__ = "sponsor"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    website_url: Mapped[str] = mapped_column()
    industry: Mapped[str] = mapped_column()
    latitude: Mapped[float] = mapped_column()
    longitude: Mapped[float] = mapped_column()

class events(Base):
    __tablename__ = "events"
    # event data given team
    id: Mapped[int] = mapped_column(primary_key=True)
    event_code: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
