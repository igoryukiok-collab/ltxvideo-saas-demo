from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import uuid
import json

app = FastAPI()

# Modelo de entrada
class VideoRequest(BaseModel):
    prompt_name: str  # Nome do prompt
    output_name: str = None  # Nome do arquivo de saída opcional

# Carrega prompts pré-definidos
with open("prompts.json", "r", encoding="utf-8") as f:
    prompts = json.load(f)

@app.post("/generate")
async def generate_video(request: VideoRequest):
    # Escolhe o prompt
    prompt_text = prompts.get(request.prompt_name)
    if not prompt_text:
        return {"error": f"Prompt '{request.prompt_name}' não encontrado."}

    # Nome do arquivo de saída
    output_file = request.output_name or f"video_{uuid.uuid4().hex}.mp4"

    # Chama o script de geração de vídeo
    try:
        cmd = f"python3 ltxvideo_script.py --prompt \"{prompt_text}\" --output {output_file}"
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        return {"error": str(e)}

    return {"video_file": output_file, "message": "Vídeo gerado com sucesso!"}

@app.get("/")
async def root():
    return {"status": "Server is running!"}
