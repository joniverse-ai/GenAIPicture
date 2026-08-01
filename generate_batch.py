import csv
import json
import zlib
from pathlib import Path

import torch
from diffusers import StableDiffusionXLPipeline


PROMPT_TEMPLATE = "{subject}, {action}, {camera}, {lighting}, {environment}, {style}"
MODEL_ID = "stabilityai/sdxl-turbo"
OUT_DIR = Path("out")


def id_to_seed(id_str: str) -> int:
    return zlib.crc32(id_str.encode())


def build_prompt(row: dict) -> str:
    return PROMPT_TEMPLATE.format(**row)


def main():
    with open("scenes.csv", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    OUT_DIR.mkdir(exist_ok=True)

    pipe = StableDiffusionXLPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        variant="fp16",
    )
    pipe.to("cuda")

    failed = []
    for i, row in enumerate(rows):
        id_ = row["id"]
        prompt = build_prompt(row)
        seed = id_to_seed(id_)
        generator = torch.Generator(device="cuda").manual_seed(seed)

        print(f"[{i+1}/{len(rows)}] {id_}: generating...")

        try:
            image = pipe(
                prompt=prompt,
                guidance_scale=0.0,
                num_inference_steps=4,
                generator=generator,
            ).images[0]

            image.save(str(OUT_DIR / f"{id_}.png"))

            meta = {
                "id": id_,
                "prompt": prompt,
                "seed": seed,
                "model": MODEL_ID,
            }
            with open(OUT_DIR / f"{id_}.json", "w") as mf:
                json.dump(meta, mf, indent=2)

            print(f"  -> saved out/{id_}.png / .json")

        except Exception as e:
            print(f"  !! FAILED: {e}")
            failed.append((id_, str(e)))

    if failed:
        print("\n=== Failed rows ===")
        for id_, reason in failed:
            print(f"  {id_}: {reason}")
    else:
        print("\nAll rows completed successfully.")


if __name__ == "__main__":
    main()
