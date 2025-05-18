print("=== PYTHON SCRIPT STARTED ===")

from aiohttp import web
import os
import asyncio

async def handle_root(request):
    return web.Response(text="OK")

async def main():
    app = web.Application()
    app.router.add_route("GET", "/", handle_root)

    port = int(os.getenv("PORT", "8080"))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    print(f"=== SERVER STARTED ON PORT {port} ===")

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
