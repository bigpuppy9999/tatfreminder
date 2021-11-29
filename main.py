from mee6_py_api import API
import asyncio, time

mee6API = API(263594286417838082)
async def main(id):
    id = str(id)
    leaderboard_page = await mee6API.levels.get_leaderboard_page(0)
    me = {}
    i = 0
    for user in leaderboard_page["players"]:
        i += 1
        if user["id"] == id:
            me = i
    print(me)
    if me > 20:
        # Run code to remind person
        pass

while True:
    asyncio.run(main(491348378098204672))
    time.sleep(60*60) # Wait an hour