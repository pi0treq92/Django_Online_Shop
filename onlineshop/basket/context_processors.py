from .basket import Basket

def basket(request):
    """
    Context Processor create example of basket using request object and share this basket to all templates as
    a basket variable
    :param request:
    :return: dict of object
    """
    return {'basket': Basket(request)}