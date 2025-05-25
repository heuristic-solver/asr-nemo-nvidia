# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from transcriber import transcribe_file
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()
executor = ThreadPoolExecutor()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Done to check if the file exists or not
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files are supported")

    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Run blocking ASR code in a separate thread
    try:
        text = await asyncio.get_event_loop().run_in_executor(executor, transcribe_file, temp_file)
    finally:
        os.remove(temp_file)

    return JSONResponse(content={"transcription": text})
