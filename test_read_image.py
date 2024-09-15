import cv2
import numpy as np
import pytest

from src.bright_patches import read_image

def test_read_image_color(test_image_path: str) -> None:
    img = read_image(test_image_path)

    assert isinstance(img, np.ndarray)
    assert len(img.shape) == 3
    assert img.shape[0] > 0
    assert img.shape[1]  > 0

def test_read_image_gray(test_image_path: str) -> None:
    img = read_image(test_image_path, grayscale=True)

    assert isinstance(img, np.ndarray)
    assert len(img.shape) == 2
    assert img.shape[0] > 0
    assert img.shape[1]  > 0

