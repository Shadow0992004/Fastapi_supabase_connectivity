from fastapi import FastAPI
import random
from supabase import create_client,Client
from pydantic import BaseModel

app=FastAPI()


s_url="https://vxkudlgnvribozwuhitm.supabase.co"  #"https://uabnsdldcohmgagcnmrk.supabase.co"
s_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ4a3VkbGdudnJpYm96d3VoaXRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDc1MDA5MDgsImV4cCI6MjAyMzA3NjkwOH0.qqhHK0yR75GrDCQueYnwIbYlbjB_WuDeZYginVdCfaQ"
#"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVhYm5zZGxkY29obWdhZ2NubXJrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyMzAwNjMsImV4cCI6MjAyMjgwNjA2M30.uKdN_AYzjv9jABwf5fw9P3PabmmXMVZPboKB1tx_WaQ"
supabase: Client=create_client(s_url,s_key)

@app.get('/')
async def root():
    return {'example':"this is an example",'data':99}

@app.get("/fetch")
async def fetch():
    fetch = supabase.table('table1').select('*').execute()
    return fetch

@app.get("/fetch/{id}")
async def get(id:int):
    get = supabase.table('table1').select('*').eq("id",id).execute()
    return get

class Base(BaseModel):
    title: str
    description: str

@app.post('/insert')
def insertion(a:Base):
    id=2
    a=supabase.table("table1").insert({
        "id":id,
        "title":a.title,
        "description":a.description
    }).execute()
    return a

@app.put("/update/{id}")
async def update_item(id: int, updated_data: Base):
    updated_data_dict = updated_data.model_dump()
    update_query = supabase.table("table1").update(updated_data_dict).eq("id", id).execute()
    return update_query

@app.delete('/delete/{id}')
def deletion(id:str):
    a =supabase.table('table1').delete().eq("id",id).execute()
    return {"msg":"Deleted"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
