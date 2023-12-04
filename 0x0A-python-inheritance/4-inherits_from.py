def inherits_from(obj, a_class):
    """checks for subclasses

    Args:
        obj (_obj_): fetches from main
        a_class (class): fetches from main
    """

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
