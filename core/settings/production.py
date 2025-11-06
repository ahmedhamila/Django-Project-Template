from core.env import config
from core.settings.base import *


DEBUG = config("DEBUG")
DEFAULT_RENDERER_CLASSES = ("djangorestframework_camel_case.render.CamelCaseJSONRenderer",)
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = DEFAULT_RENDERER_CLASSES
