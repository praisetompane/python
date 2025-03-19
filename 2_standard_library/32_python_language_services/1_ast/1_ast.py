import ast
import inspect
import pprint
from hello import hello


pprint.pprint(ast.dump(ast.parse(inspect.getsource(hello))))
