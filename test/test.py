
from typing import Callable, Union, Tuple, Any
# http://c.biancheng.net/view/2380.html

class Line():
    def __init__(self,input,output) -> None:
        print("init")

    def __main__(self):
        print("main")
    
    def forward(self,x):
        print("forward")

    
    def _call_impl(self, *args: Any, **kwds: Any) -> Any:
        print("call")

    __call__ : Callable[..., Any] = _call_impl


m = Line("a","b")
c = m("x")

