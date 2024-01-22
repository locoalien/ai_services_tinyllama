'''
##################### TinyLlama + FastAPI + Docker #########################################
Autor: Santiago Gonzalez Acevedo 
Twitter: @locoalien
github: https://github.com/locoalien/ai_services_tinyllama
Python 3.11+
'''
import json
import torch
from transformers import pipeline
from fastapi import HTTPException

class TinyLlamaLogic:
    def __init__(self, query):
        self.query = query
    
    def model_query(self):
        try:
            pipe = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", #Modelo a utilizar
            torch_dtype=torch.bfloat16,
            device_map="cpu", #Optimizacion para CPU 
            )

            #Configuracion de comportamiento del modelo
            messages = [
                {
                    "role": "system",
                    "content": "You are a friendly chatbot who always funny and interesting. You only reply with the actual answer without repeating my question.",
                },
                {"role": "user", "content": f"{self.query}"},
            ]
            #Obtener prompt para el modelo
            prompt = pipe.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            #Configuracion de exactitud del modelo
            outputs = pipe(
                prompt,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
            )
            #Resultado del modelo
            output = outputs[0]["generated_text"]
            json_results = json.dumps(output, indent=4, default=str)
            return json_results
        except Exception as e:
            self.save_log('400')
            raise HTTPException(
            status_code=400, detail=f"Error decoding PDF data: {str(e)}")
        
        

