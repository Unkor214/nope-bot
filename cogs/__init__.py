import inspect, sys

from .commands import *
from .event import *


def setup(bot):
    for class_name, class_obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        bot.add_cog(class_obj(bot))
        print(f"cog - {class_name}, initialized")