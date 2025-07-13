from PIL import Image
import io

def check_image_quality(uploaded_file):
    """
    Basic checks: format, resolution, aspect ratio, file size.
    Returns a dict of results.
    """
    result = {}
    # Read image
    img = Image.open(uploaded_file)
    result['format'] = img.format
    result['width'], result['height'] = img.size
    # File size
    uploaded_file.seek(0, io.SEEK_END)
    size_kb = uploaded_file.tell() / 1024
    result['size_kb'] = round(size_kb, 2)
    # Aspect ratio check (square or rectangular)
    result['aspect_ratio'] = round(result['width'] / result['height'], 2)
    # Simple warnings
    result['warnings'] = []
    if result['format'] not in ['PNG', 'JPEG', 'JPG']:
        result['warnings'].append('Unsupported format. Use PNG or JPEG.')
    if result['width'] < 800 or result['height'] < 600:
        result['warnings'].append('Low resolution: should be at least 800×600.')
    if size_kb > 5000:
        result['warnings'].append('File size large: optimize to <5 MB.')
    return img, result
