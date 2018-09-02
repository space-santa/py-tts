import settings

if settings.WRITER == settings.POST:
    from .post import write
else:
    from .console_writer import write
