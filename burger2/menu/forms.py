from django import forms
from django.core.files.images import get_image_dimensions

class SVGFormImageField(forms.FileField):
    def to_python(self, data):
        f = super().to_python(data)
        if f is None:
            return None
        
        if hasattr(data, 'name') and data.name.lower().endswith('.svg'):
            if f.size > 50 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("File size exceeds 5MB.")
            return f
        else:
            # Validate raster images with Pillow
            try:
                from PIL import Image
                img = Image.open(f)
                img.verify()
                f.seek(0)
                width, height = get_image_dimensions(f)
                if width == 0 or height == 0:
                    raise forms.ValidationError("Invalid image dimensions.")
            except Exception as e:
                raise forms.ValidationError("Invalid image file: %s" % str(e))
            return f