# gotta read the docs more

from sqlalchemy import ForeignKey, String, DeclarativeBase, Mapped, mapped_column, relationship

class team(Base):
    __tablename__ = "team"
    # team data
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    website_url: Mapped[str] = mapped_column()
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
    