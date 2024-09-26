from inspect import Parameter, signature
from pydantic import create_model


def schema(f):
    "Return a schema for the parameters of `f`"
    kw = {
        n: (o.annotation, ... if o.default == Parameter.empty else o.default)
        for n, o in signature(f).parameters.items()
    }
    s = create_model(f"Input for `{f.__name__}`", **kw).model_json_schema()
    return dict(name=f.__name__, description=f.__doc__, parameters=s)
