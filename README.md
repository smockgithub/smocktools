# smocktools
python tools

本python tools包括
- MysqlRepository 是mysql工具类，为了特殊情况下的稳定性要求，进行了链接丢失的重新链接补偿。实现了ssh方式，但在在macos下可能存在问题，macos最好装个conda

使用方法：

pip install smocktools
from smocktools import MysqlRepository

r = MysqlRepository("localhost","root","123456","test")