from sqlmodel import Session
from crm.db import engine
from crm.identity import User
from crm.auth import passwords

with Session(engine()) as session:
    session.add(User(
        company_id=1,
        username="admin",
        password_hash=passwords.hash("Admin12345!"),
        role="admin",
        active=True,
    ))
    session.commit()
    print("Foydalanuvchi yaratildi")