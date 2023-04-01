from fastapi import FastAPI

app = FastAPI()

@app.get("/number/{n}")
async def table(n: str):
    n = int(n)

    result = []
    
    for i in range(1, 11):
        result.append(f"{n} x {i} = {n*i}")
    
    return {"table": result}