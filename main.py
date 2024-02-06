from fastapi import FastAPI
import random
from supabase import create_client

app=FastAPI()


s_url="https://uabnsdldcohmgagcnmrk.supabase.co"
s_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVhYm5zZGxkY29obWdhZ2NubXJrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyMzAwNjMsImV4cCI6MjAyMjgwNjA2M30.uKdN_AYzjv9jABwf5fw9P3PabmmXMVZPboKB1tx_WaQ"
sup=create_client(s_url,s_key)

@app.get('/')
async def root():
    return {'example':"this is an example",'data':99}

@app.get('/random')
async def get_random():
    rn=random.randint(0,100)
    return {'number':rn,'limit':100}

@app.get('/random/{limit}')
async def get_random(limit:int):
    rn=random.randint(0,limit)
    return {'number':rn,'limit':limit}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)