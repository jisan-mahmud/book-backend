from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "role" VARCHAR(50) NOT NULL DEFAULT 'user';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "role";"""


MODELS_STATE = (
    "eJztmW9P4jAcx98K2SMv8QygqLlcLgHEyPmHi8LdRWOWspXRo2tx7VRieO/XlnVjf9gxDx"
    "ATn5jt2/5o+2m737f1xXCpDTHb6zHoGV9KLwYBLhQPMX23ZIDxOFKlwEEfq4q+qKEU0Gfc"
    "AxYX4gBgBoVkQ2Z5aMwRJUIlPsZSpJaoiIgTST5BDz40OXUgH6qO3N0LGREbPkOmX8cjc4"
    "AgtmP9RLZsW+kmn4yV1uu1T05VTdlc37Qo9l0S1R5P+JCSsLrvI3tPxsgyBxLoAQ7tuWHI"
    "XgbD1dKsx0Lgng/DrtqRYMMB8LGEYXwd+MSSDEqqJfnn4JtRAI9FiUSLCJcsXqazUUVjVq"
    "ohm2qe1a939g8/qVFSxh1PFSoixlQFAg5moYprBFLOo3pO4WwOgZeNcz4mAVV0eAmcAawC"
    "NDWl16EzXPBsYkgcPhSvtXIOyp/1a0WzVlY0qVjaswV/FZRUVZGEGkGELkC4CMEw4FX4Xr"
    "EaV8mvuhTAag7BahrhELAhtM0xYOyJehm7ezHMjNDVYNVCxDX6wq0HbG0psLUcsLUk2IFo"
    "2Cy6w2NBK9niG2dZXmqRlnMWaTm1SBEzRaZDjxksG5RiCMiC/DMfl8DZF4HrWpzhZ2DVCa"
    "fR6VzITruMPWAltLsJjr3LRut6p6LwikqIK7l91U0zZf4Yen5gOYphjYVukGxRq/MmaD3B"
    "rsiu1/U39/U09NRtaWL/QxER7ZvCPmWQPBEqRy7MppmMTVC1g+A9/bClGcqDwO4QPAk+Jz"
    "mEu+3L1k23fvkjtnxP6t2WLKkqdZJQdw4TsxH+SOlXu3tWkq+l285VK2ltw3rdW0P2Cfic"
    "moQ+mcCeM0Ba1WBik4sB4yamDiJFpzYeuYKJ3Xy2fCfzqIedmkh5MhyM5o40UugDa/QEPN"
    "uMlUQzLjLCiGUkmSDs9PwaYqBIpqc1OBmLhDTazp061atUq3rHSjK0ShexShe5VTepAAIc"
    "1WvZtmxpHkfGBYLGtPgCIZyL7blAaBNe4P5AEk4shGAbv+lRzZGtfK5WDo4OjvcPD45FFd"
    "WTUDnK2fraQyy+Lyh6kvivQ8Sbn8gqS50iKjmniEr6FCG+ZUOa4XUXQ4wiPjCGGC3hTMSQ"
    "TcCLpu945Icv2zJfpqenPzGLXfOmAld54/umluwfF7wpM5QFM03ylHoQOeQcThTPtugNIF"
    "bW5zrxb4GtZZcyP0L2wFOY/9NLRAxSDA3OjtDN+k2zftIypovN5DrNVB16yBpm2amgJNdQ"
    "gajOh6N6R47qEXosOHIs6wfmQt6nIVjLTbfcGkVM1az6+wS4HkdFCYckw059v+lcLUi5UU"
    "gCZI+IAd7ZyOK7JYwYv99OrDkU5ahjlknD27ms/05ybV50GsnsLH+gkZWeN5lepn8B48M7"
    "UA=="
)
