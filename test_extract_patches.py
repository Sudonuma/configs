import cv2
import numpy as np
import pytest
from src.bright_patches import extract_patches


# add more test.
# add tests for corners calculations.

def test_extract_patches_5x5image(sample_image_path) -> None:
    # if we have an image of 5x5 pixels, the total extracted patches should be 1
    

    patches = []
    patch_coordinates = []
    patch_mean_intensities = []

    extract_patches(sample_image_path, patches, patch_coordinates, patch_mean_intensities)

    
    expected_num_patches = 1 
    assert len(patches) == expected_num_patches

    # patch coordinates are correctly stored
    assert len(patch_coordinates) == expected_num_patches


def test_extract_patches_20x20image() -> None:
    # the test image is 20x20 pixels, if we are extracting all the patches of 5x5 pixels 
    # the total number of patches extracted should be 256
    
    image_path = './images/img.png'
    patches = []
    patch_coordinates = []
    patch_mean_intensities = []

    extract_patches(image_path, patches, patch_coordinates, patch_mean_intensities)

    expected_num_patches = 256
    assert len(patches) == expected_num_patches

    # patch coordinates are correctly stored
    assert len(patch_coordinates) == expected_num_patches


    
