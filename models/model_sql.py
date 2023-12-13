from db import Base
from sqlalchemy.orm  import Mapped, mapped_column
from sqlalchemy import Text
from datetime import datetime

"""   
    class Post
        id: int
        title: str
        author: str
        content: Text
        create_at: datetime 
        published_at: datetime
        published: bool
    """

class PostSql(Base):
    __tablename__ = "posts"

    id = Mapped[str] = mapped_column(primary_key=True)
    title = Mapped[str] = mapped_column(nullable=False)
    author = Mapped[str] = mapped_column(nullable=False, foreign_key="users.id")
    content = Mapped[Text] = mapped_column(Text, nullable=False)
    create_at = Mapped[datetime] = mapped_column(defatul=datetime.utcnow, nullable=False)
    published_at = Mapped[datetime] = mapped_column(defatul=datetime.utcnow, nullable=False)
    published = Mapped[bool] = mapped_column(nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<Post {self.id} title {self.title} author {self.author}>"