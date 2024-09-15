import src.bright_patches as bp


# Test case for area: provided an 10x10 pixels white image, and the area should be 25.
def test_area(ten_by_ten_pixels_white_image: str) -> None:
    patches = []
    patch_coordinates = [] 
    patch_mean_intensities = []

    bp.extract_patches(ten_by_ten_pixels_white_image, patches, patch_coordinates, patch_mean_intensities)


    brightest_four, brightest_patches_coordinates, mean_brightness = bp.four_brightest_patches(patches, patch_coordinates, patch_mean_intensities)

    corners = bp.patch_centers(brightest_patches_coordinates)

    area, best_corners = bp.compute_area(corners)
    assert area == 25