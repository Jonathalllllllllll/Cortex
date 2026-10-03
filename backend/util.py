import asyncio
async def buscar_dado():
    print("buscando...")
    await asyncio.sleep(1)
    return "dado pronto"

async def main():
    resultado=await buscar_dado()
    print(resultado)

    asyncio.run(main())


def dobro (x:  int) -> int:
    return x*2


