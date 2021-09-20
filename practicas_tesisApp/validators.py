from django.forms import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'El archivo debe ser un pdf o docx.')