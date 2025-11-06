from core.env import config
from core.settings.base import *


DEBUG = config("DEBUG")
DEFAULT_RENDERER_CLASSES = (
    "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
    "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
)
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = DEFAULT_RENDERER_CLASSES
"""
Static files storage configuration for production.
"""
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
