from sqlalchemy import ForeignKey, String, DeclarativeBase, Mapped, mapped_column, relationship


class team(Base):
    __tablename__ = "team"
    # team data
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    website_url: Mapped[str] = mapped_column()
    industry: Mapped[str] = mapped_column()
    lat: Mapped[float] = mapped_column()
    lng: Mapped[float] = mapped_column()
    worlds: Mapped[str] = mapped_column()
    state: Mapped[str] = mapped_column()
    tier: Mapped[str] = mapped_column()
    source: Mapped[str] = mapped_column()
    teams_sponsored: Mapped[list[int]] = mapped_column()

class sponsor(Base):
    __tablename__ = "sponsor"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    website_url: Mapped[str] = mapped_column()
    industry: Mapped[str] = mapped_column()
    lat: Mapped[float] = mapped_column()
    lng: Mapped[float] = mapped_column()
    