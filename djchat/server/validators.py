from django.core.validators import ValidationError

from PIL import Image
import os


def validate_icon_image_size(image):
    if image:
        with Image.open(image) as img:  # open(image)
            if img.height > 70 or img.width > 70:
                raise ValidationError(f"Image size {image.size} should be less than 70x70 pixels")
            else:
                return image


def validate_image_extension(image):
    ext = os.path.splitext(image.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported extension with {ext}, supported with {valid_extensions}')
    else:
        return image
