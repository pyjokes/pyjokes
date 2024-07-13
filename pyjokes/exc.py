class PyjokesError(Exception):
    "Base class for all pyjokes exceptions"


class LanguageNotFoundError(PyjokesError):
    pass


class CategoryNotFoundError(PyjokesError):
    pass
