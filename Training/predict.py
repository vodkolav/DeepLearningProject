import os
import random

import numpy as np

from cog import BasePredictor, Input, Path


class DummyPredictor(BasePredictor):
    def setup(self, model_name="basic", device="auto"):
        print("setup nothing")

    def predict(self,
        input_file: Path = Input(description="Dummy input"),
    ) -> Path:
        return Path("Dummy output")


if __name__ == "__main__":
    p = DummyPredictor()
    p.setup()
    out = p.predict(
        "Bunch of nothin"
    )