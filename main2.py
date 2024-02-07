from fastapi import FastAPI
import random
from supabase import create_client,Client

app=FastAPI()


s_url="https://uabnsdldcohmgagcnmrk.supabase.co"
s_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVhYm5zZGxkY29obWdhZ2NubXJrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyMzAwNjMsImV4cCI6MjAyMjgwNjA2M30.uKdN_AYzjv9jABwf5fw9P3PabmmXMVZPboKB1tx_WaQ"
supabase: Client=create_client(s_url,s_key)

@app.get('/')
async def root():
    return {'example':"this is an example",'data':99}

@app.get("/fetch/")
async def fetch_data():
    i = supabase.table("table1").select("*").execute()
    return i

@app.get('/insert/')
def insertion(a):
    id=2
    a=supabase.table("table1").insert({
        "id":id,
        "title":a.title,
        "description":a.description
    }).execute()
    return a
