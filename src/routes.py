

from src import api
from src.resources.index import Index_page

api.add_resource(Index_page, '/', strict_slashes=False)
