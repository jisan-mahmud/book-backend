from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "is_superuser" SET DEFAULT False;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "is_superuser" SET DEFAULT True;"""


MODELS_STATE = (
    "eJztmGtv2jAUhv8KyqdO6iqg0FbTNIlbVdYCUwvb1KqKTGKCh2PT2GmLKv77bJMLuZCRDi"
    "iV+gUlr32w/fhyXudFs6kJMTsaMOhoXwovGgE2FA8R/bCggek0VKXAwRCriq6ooRQwZNwB"
    "BhfiCGAGhWRCZjhoyhElQiUuxlKkhqiIiBVKLkEPLtQ5tSAfq47c3QsZERM+Q+a/Tif6CE"
    "FsRvqJTNm20nU+myptMGg3z1VN2dxQNyh2bRLWns74mJKguusi80jGyDILEugADs2lYche"
    "esP1pUWPhcAdFwZdNUPBhCPgYglD+zpyiSEZFFRL8qfyTcuBx6BEokWESxYv88WowjErVZ"
    "NNNS5q1wfHJ5/UKCnjlqMKFRFtrgIBB4tQxTUEKedRPSdwNsbASce5HBODKjq8Bk4PVg6a"
    "PqXXodNs8KxjSCw+Fq/VYgbKn7VrRbNaVDSpWNqLBd/1SsqqSEINIUIbIJyHYBDwKnyvWI"
    "2b5FdeC2A5g2A5iXAM2Bia+hQw9kSdlN29GmZK6Gaw+kLINTzhtgO2uhbYagbYahzsSDSs"
    "593hkaCNbPGdsyyutUiLGYu0mFikiOki06HHFJZ1SjEEZEX+WY6L4RyKwG0tzuAY2HTCqf"
    "d6V7LTNmMPWAntfozjoFNvXR+UFF5RCXElt7v9JFPmTqHjepYjH9ZI6A7J5rU6b4L2D0VE"
    "9EIXyT9lxTaFypEN09nGY2NsTS/4yH/Y0/PVgcDsETzzNkMG936707rp1zo/IvCbtX5Llp"
    "SVOoupByex0yP4k8Kvdv+iIF8Lt71uK27Mgnr9W032Cbic6oQ+6cBcSt++6oOJTC4GjOuY"
    "Wojkndpo5AYmdvdn/TuZR3/YiYmU95rRZMmQS2EIjMkTcEw9UhLOuDjPJizliPTCzi+vIQ"
    "aKZHJavXudOE4n+7lT5/4q9VV/x0oytExXsUoW2WU7rgACLNVr2bZsaRlHyvXXx7T6+hvM"
    "xf5cf9uE57j9SsKxheBt4ze9aFiylc/lUuW0cnZ8UjkTVVRPAuU0Y+v7GXD1bTevD/4vC/"
    "zm94nSWh64lOGBS0kPLM6yMU1xaqshhhEfGAOMhnAmYsg64HnTdzTyw5ftmS/zp2c40/N9"
    "pEwEbvJ75Ztasn98nkyYoTSYSZLn1IHIIpdwpni2RW8AMdKO69hH7b1llzA/QnbAU5D/k0"
    "tEDFIMDS4ugI3aTaPWbGnz1WZym2aqBh1kjNPslFeSaahAWOfDUb0jR/UIHeZdOdb1A0sh"
    "79MQbOU7rdwaeUzVovr7BLgdR0UJhyTFTn2/6XVXpNwwJAZyQMQA70xk8MMCRozf7yfWDI"
    "py1BHL5MM76NR+x7k2rnr1eHaWf1BPS8+7TC/zv9kV1Xw="
)
