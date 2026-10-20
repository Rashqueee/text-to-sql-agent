"""Cetak respons mentah OpenRouter untuk dua model pembanding."""

import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELS = (
    "openai/gpt-4o-mini",
    "meta-llama/llama-3.1-8b-instruct",
)
PESAN = (
    "Write the SQL code for: - Product table - Customer table - Order table "
    "STRICTLY generate the SQL script only. NO additional text"
)


def main() -> int:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("OPENROUTER_API_KEY belum disetel di src/.env.", file=sys.stderr)
        return 1

    failed = False
    for model in MODELS:
        # Hanya request yang diserialisasi; respons tidak di-parse atau diubah.
        payload = json.dumps(
            {
                "model": model,
                "messages": [{"role": "user", "content": PESAN}],
                "temperature": 0,
            }
        ).encode("utf-8")
        request = Request(
            OPENROUTER_URL,
            data=payload,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "Skripsi App",
            },
            method="POST",
        )

        print(f"Model: {model}", file=sys.stderr, flush=True)
        try:
            with urlopen(request, timeout=120) as response:
                raw_body = response.read()
        except HTTPError as error:
            # Respons galat dari server tetap dicetak tanpa diubah.
            raw_body = error.read()
            print(f"HTTP {error.code} untuk {model}", file=sys.stderr)
            failed = True
        except (URLError, TimeoutError) as error:
            print(f"Gagal menghubungi OpenRouter untuk {model}: {error}", file=sys.stderr)
            failed = True
            continue

        sys.stdout.buffer.write(raw_body)
        if not raw_body.endswith(b"\n"):
            sys.stdout.buffer.write(b"\n")  # Pemisah antarrespons model.
        sys.stdout.buffer.flush()

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
