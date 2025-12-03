from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" UUID NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) UNIQUE,
    "email" VARCHAR(250) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(255) NOT NULL,
    "full_name" VARCHAR(200),
    "is_active" BOOL NOT NULL DEFAULT True,
    "is_superuser" BOOL NOT NULL DEFAULT True,
    "joining_date" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "last_login" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "books" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "author" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "created_by_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmGtv2jAUhv8KyicmdRVQaKtpmgSUqqwFpha2qVUVmcQED8emsdMWVfz32SYXciEjHb"
    "RU4gtKXvvg48e313nRbGpCzA4HDDral8KLRoANxUNEPyhoYDoNVSlwMMSqoitqKAUMGXeA"
    "wYU4AphBIZmQGQ6ackSJUImLsRSpISoiYoWSS9CDC3VOLcjHKpG7eyEjYsJnyPzX6UQfIY"
    "jNSJ7IlG0rXeezqdIGg/bZuaopmxvqBsWuTcLa0xkfUxJUd11kHsoYWWZBAh3AobnUDZml"
    "111fWmQsBO64MEjVDAUTjoCLJQzt68glhmRQUC3Jn+o3LQcegxKJFhEuWbzMF70K+6xUTT"
    "bVvKhfF4+OP6leUsYtRxUqItpcBQIOFqGKawhSjqN6TuBsjoGTjnM5JgZVJLwGTg9WDpo+"
    "pdeh02zwrGNILD4Wr7VSBsqf9WtFs1ZSNKmY2osJ3/VKKqpIQg0hQhsgnIdgEPAqfK+YjZ"
    "vkV1kLYCWDYCWJcAzYGJr6FDD2RJ2U1b0aZkroZrD6Qsg13OG2A7a2FthaBthaHOxINKzn"
    "XeGRoI0s8TdnWVprkpYyJmkpMUkR08VJhx5TWDYoxRCQFefPclwM51AEbmtyBtvApg+cRq"
    "93JZO2GXvASmj3YxwHnUbrulhWeEUlxJXc7vaTTJk7hY7rWY58WCOhe7IRsn8oIiILXZz9"
    "KRP2TKgc2TAdbTw2htb0gg/9hx3dXh0IzB7BM2/EMrj3253WTb/e+RGBf1bvt2RJRamzmF"
    "o8jm0ewZ8UfrX7FwX5WrjtdVtxXxbU699qMifgcqoT+qQDc+n09lUfTGRwMWBcx9RCJO/Q"
    "RiM3MLBvv9V/kHH0u50YSHmtGU2W/LgUhsCYPAHH1CMl4YiL7WzCUnZIL+z88hpioEgmh9"
    "W71onddLKbK3Xuz1Jf9VesJEMrdBWrZJFdseMKIMBSWcu2ZUvLOFJuvz6m1bffYCx25/bb"
    "JjzH5VcSjk0Ebxm/6z3Dkq18rpSrJ9XTo+PqqaiiMgmUk4yl75+Aqy+7eW3wfzngd79OlN"
    "eywOUMC1xOWmCxl41pilFbDTGM2GMMMBrCmYgu64DnPb6jkXtftmO+zB+e4UzP940yEbjJ"
    "z5Xvasn+8XUyYYbSYCZJnlMHIotcwpni2RbZAGKkbdexb9o7yy5hfoTsgKfg/E9OEdFJ0T"
    "W4uAA26zfN+llLm682k9s0U3XoIGOcZqe8kkxDBcI6e0f1gRzVI3SYd+VY1w8shXxMQ7CV"
    "z7RyaeQxVYvqHxPgdhwVJRySFDv1/abXXXHkhiExkAMiOnhnIoMfFDBi/H43sWZQlL2OWC"
    "YfXrFT/x3n2rzqNeKns/yDRtrx/JbHy/wvmkDVMQ=="
)
