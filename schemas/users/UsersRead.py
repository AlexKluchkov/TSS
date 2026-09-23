from schemas.users.User import User

class UsersRead(User):
    id: int
    class Config:
        from_attributes = True