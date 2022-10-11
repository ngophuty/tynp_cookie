from motor.motor_asyncio import AsyncIOMotorClient


MONGO_DETAIL = 'mongodb://localhost:27017/'
client = AsyncIOMotorClient(MONGO_DETAIL)
create_database = client.example
collection = create_database.get_collection('exaple_mongodb')

async def example():
    data = {'example':'connect to mongodb'}
    await collection.insert_one(data)
    return
