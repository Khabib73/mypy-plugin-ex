from mypy.plugin import Plugin, FunctionContext
from mypy.types import Type


def infer_make_list_return_type(ctx: FunctionContext) -> Type:
    arg_type = ctx.arg_types[0][0] # type first argument
    # return new type list[<arg_type>]
    return ctx.api.named_generic_type('builtins.list', [arg_type])


class MyPlugin(Plugin):
    def get_function_hook(self, fullname: str):
        if fullname == 'mylib.make_list':
            return infer_make_list_return_type
        return None


def plugin(version: str):
    return MyPlugin