from django.shortcuts import render
from django.http import JsonResponse
from diffusers import DiffusionPipeline
import torch

def gen_img(request):

    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp8")
    pipe.to("cpu")

    # if using torch < 2.0
    # pipe.enable_xformers_memory_efficient_attention()

    prompt = "An astronaut riding a green horse"

    images = pipe(prompt=prompt).images[0]
    
    return JsonResponse({"image": images})
    
