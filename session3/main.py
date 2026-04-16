import logging
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

import pandas as pd

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def filter_emails_starting_with_a(data: pd.DataFrame):
    """Return rows where email starts with 'a'."""
    return data[data["email"].fillna("").str.startswith("a")]


def read_and_filter_csv_multithread() -> None:
    """Simple multithreading example using one worker thread."""
    start = perf_counter()
    logging.info("[Multithread] Reading CSV file...")

    data = pd.read_csv("data/data_processing_XXL.csv")

    # Simple threading: run the filtering in one separate thread
    with ThreadPoolExecutor(max_workers=5) as executor:
        future = executor.submit(filter_emails_starting_with_a, data)
        filtered_data = future.result()

    filtered_data.to_csv("data/filtered_data_multithread.csv", index=False)

    elapsed = perf_counter() - start
    logging.info("[Multithread] Filtering completed. Rows matched: %s", len(filtered_data))
    logging.info("[Multithread] Saved: data/filtered_data_multithread.csv")
    logging.info("[Multithread] Multithread time taken: %.4f seconds", elapsed)


def read_and_filter_csv_singlethread() -> None:
    """Single-thread version for timing comparison."""
    start = perf_counter()
    logging.info("[Singlethread] Reading CSV file...")

    data = pd.read_csv("data/data_processing_XXL.csv")
    filtered_data = filter_emails_starting_with_a(data)
    filtered_data.to_csv("data/filtered_data_singlethread.csv", index=False)

    elapsed = perf_counter() - start
    logging.info(
        "[Singlethread] Filtering completed. Rows matched: %s", len(filtered_data)
    )
    logging.info("[Singlethread] Saved: data/filtered_data_singlethread.csv")
    logging.info("[Singlethread] Singlethread time taken: %.4f seconds", elapsed)


if __name__ == "__main__":
    read_and_filter_csv_singlethread()
    read_and_filter_csv_multithread()
