import numpy as np
import pytest
from typing import List, Tuple
import cv2

# Dummy data for test four brightest.
@pytest.fixture
def patches() -> List[np.ndarray]:
    return [np.array([[100, 250], [100, 250]]), 
            np.array([[10, 25], [10, 25]]), 
            np.array([[150, 250], [150, 250]]),
            np.array([[160, 250], [160, 250]]),
            np.array([[90, 250], [90, 250]])]

# Dummy data for test four brightest.
@pytest.fixture
def patch_coordinates() -> List[Tuple]:
    return [(0, 0, 2, 2), (2, 2, 4, 4), (4, 4, 6, 6), (6, 6, 8, 8), (3, 5, 5, 7)]

# Dummy data for test four brightest.
@pytest.fixture
def patch_mean_intensities() -> List[float]:
    return [175, 17.5, 200, 205, 170]


@pytest.fixture
def sample_image_path():

    # if we have an image of 5x5 pixels, the total extracted patches should be 1
    sample_image = np.array([[1, 2, 3, 4, 5],
                            [6, 7, 8, 9, 10],
                            [11, 12, 13, 14, 15],
                            [16, 17, 18, 19, 20],
                            [21, 22, 23, 24, 25]], dtype=np.uint8)

    # Save the sample image: (should be saved to a temporary file)
    image_path = './images/sample_image.png'
    cv2.imwrite(str(image_path), sample_image)
    return str(image_path)


@pytest.fixture
def test_image_path() -> str:
    return './images/img.png'


@pytest.fixture
def ten_by_ten_pixels_white_image() -> str:
    return './images/picw1.png'