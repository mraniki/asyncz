import pytz
from asyncz.executors import AsyncIOExecutor, ThreadPoolExecutor
from asyncz.schedulers.asyncio import AsyncIOScheduler
from asyncz.stores import MongoDBStore, RedisStore

# Define the stores
# Override the default MemoryStore to become RedisStore where the db is 0
stores = {"mongo": MongoDBStore(), "default": RedisStore(database=0)}

# Define the executors
# Override the default ot be the AsyncIOExecutor
executors = {"default": AsyncIOExecutor(), "threadpool": ThreadPoolExecutor(max_workers=20)}

# Set the defaults
job_defaults = {"coalesce": False, "max_instances": 4}

# Start the scheduler
scheduler = AsyncIOScheduler()

## Add some jobs here or anything else (for instance 3 jobs)
scheduler.add_job(...)
scheduler.add_job(...)
scheduler.add_job(...)

scheduler.configure(
    stores=stores, executors=executors, job_defaults=job_defaults, timezone=pytz.utc
)