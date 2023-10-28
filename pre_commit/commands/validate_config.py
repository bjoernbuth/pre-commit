from __future__ import annotations

from collections.abc import Sequence

from pre_commit import clientlib


def validate_config(filenames: Sequence[str]) -> int:
    ret = 0

    for filename in filenames:
        try:
            clientlib.load_config(filename)
        except clientlib.InvalidConfigError as e:
            print(e)
            ret = 1

    return ret
