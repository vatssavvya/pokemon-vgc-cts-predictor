import json
import os
import time
import requests

BASE_URL = "https://championsbattledata.com"
RAW_DIR = os.path.join("data", "raw")

TEST_POKEMON = "Garchomp"
TEST_FORMAT = "Doubles"
REQUEST_DELAY_SECONDS = 1


def ensure_dirs():
    os.makedirs(RAW_DIR, exist_ok=True)


def fetch_and_save(endpoint: str, filename: str):
    url = f"{BASE_URL}{endpoint}"
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    out_path = os.path.join(RAW_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved -> {out_path}")
    return data


def main():
    ensure_dirs()

    fetch_and_save("/api", "index_sample.json")
    time.sleep(REQUEST_DELAY_SECONDS)

    fetch_and_save(
        f"/api/battle/{TEST_FORMAT}/{TEST_POKEMON}",
        f"battle_{TEST_FORMAT}_{TEST_POKEMON}.json",
    )
    time.sleep(REQUEST_DELAY_SECONDS)

    fetch_and_save(f"/api/metadata/{TEST_POKEMON}", f"metadata_{TEST_POKEMON}.json")

    print("\ncheck the real structure in raw now")


if __name__ == "__main__":
    main()