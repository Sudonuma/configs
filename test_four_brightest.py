import cv2
import numpy as np
import pytest
from typing import List, Tuple

from src.bright_patches import four_brightest_patches
from src.bright_patches import is_overlapping

# Test case for comparing patches based on brightness
def test_four_brightest_patches(patches: List[np.ndarray], patch_coordinates: List[Tuple], patch_mean_intensities: List[float]) -> None:
    

    brightest_four, brightest_patch_coordinates, mean_brightness = four_brightest_patches(patches, patch_coordinates, patch_mean_intensities)

    assert len(brightest_four) == 4
    assert len(brightest_patch_coordinates) == 4
    assert len(mean_brightness) == 4

    
    # check that they are sorted
    assert all(mean_brightness[i] >= mean_brightness[i+1] for i in range(len(mean_brightness) - 1))

    # Check that the selected patches are not overlapped
    for i in range(len(brightest_patch_coordinates)):
        for j in range(i + 1, len(brightest_patch_coordinates)):
            assert not is_overlapping(range(len(patch_mean_intensities)), brightest_patch_coordinates, i, j)
