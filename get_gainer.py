"""
get_gainer.py

Main pipeline using Template Method Pattern to process gainers.
"""

from bin.gainers.factory import GainerFactory

class GainerPipeline:
    """Handles the end-to-end process for a gainer source."""

    def __init__(self, processor):
        self.processor = processor

    def run(self):
        print("[Pipeline] Starting normalization...")
        self.processor.normalize()

        print("[Pipeline] Saving to file...")
        self.processor.save_with_timestamp()

        print("[Pipeline] Process complete.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Run gainer processing pipeline for a supported source."
    )
    parser.add_argument(
        "--src",
        required=True,
        choices=["yahoo", "wsj", "mock"],
        help="Specify the gainer source to process (yahoo or wsj)",
    )

    args = parser.parse_args()

    factory = GainerFactory(args.src)
    processor = factory.create_processor()

    pipeline = GainerPipeline(processor)
    pipeline.run()
