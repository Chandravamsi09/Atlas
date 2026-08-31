import asyncio
from backend.app.core.security import generate_api_key_pair

def seed():
    raw, masked, hashed = generate_api_key_pair()
    print("========================================")
    print("Atlas Enterprise Seeding Complete")
    print(f"Sample Root API Key: {raw}")
    print(f"Masked Key:          {masked}")
    print("========================================")

if __name__ == "__main__":
    seed()
