from fastapi import FastAPI

app=FastAPI(title='SaveGo V6 AI API')

@app.get('/ai/advice')
def advice():
    return {
        'score':92,
        'recommend':'建议购买'
    }