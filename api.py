from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse
from PIL import Image
import requests
from io import BytesIO
from transformers import ViltProcessor, ViltForQuestionAnswering

app = FastAPI(title="Visual Question Answering API", version="0.0.1")

#ViLT code
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def get_answer(image, text):
    try:
        #load and process the image
        img = Image.open(BytesIO(image)).convert('RGB')
        #prepare inputs
        encoding = processor(img, text, return_tensors="pt")

        #forward pass
        outputs = model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        answer = model.config.id2label[idx]

        return answer

    except Exception as e:
        return str(e)
    

#fastapi code
@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")

@app.post("/answer")
async def process_image(image: UploadFile = File(...), text:str = None):
    try:
        answer = get_answer(await image.read(), text)
        return JSONResponse({"Answer": answer})
    
    except Exception as e:
        return JSONResponse({"Error": str(e)})