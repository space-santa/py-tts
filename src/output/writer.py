import settings

# pylint: disable=unused-import
if settings.WRITER == settings.POST:
    from .post import write
else:
    from .console_writer import write
# pylint: enable=unused-import
