import aiojobs

scheduler = None

async def get_scheduler():
    global scheduler
    if scheduler is None:
        scheduler = await aiojobs.create_scheduler(limit=1)
    return scheduler

async def close_scheduler():
    global scheduler
    if scheduler is not None:
        await scheduler.close()
        scheduler = None