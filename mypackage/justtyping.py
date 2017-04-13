from typing import Sequence
x = Sequence['xxx']  # Unable to reproduce without this line, or replace string `'xxx'` with a class (e.g. `bytes`)
