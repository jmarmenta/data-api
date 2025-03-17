from database import Dbclient

try:
    with Dbclient().connection as connection:
        print("✅ Connected to PostgreSQL successfully!")
except Exception as e:
        print("❌ Connection failed:", e)
