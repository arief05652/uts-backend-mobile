from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `user_id` VARCHAR(36) NOT NULL PRIMARY KEY DEFAULT 'f5634236-f030-4d34-9b11-f88438058903',
    `user_device_id` VARCHAR(36) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `urls` (
    `url_id` VARCHAR(36) NOT NULL PRIMARY KEY DEFAULT '92e978e8-ddd2-4a97-84a2-56bd3d2428a8',
    `user_id` VARCHAR(36) NOT NULL,
    CONSTRAINT `fk_urls_users_c3691326` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlmFP2zAQhv8KyicmkalN0jbdt7YbGmMDqYxpEkKRG19SC8cpjgNUqP8d20mapiRdO5"
    "go0r41753tuye+N300ohgDTT5ecpoYnw4eDYYikD8q+tGBgWazUlWCQBOqE9MiY5IIjnwh"
    "tQDRBKSEIfE5mQkSM6mylFIlxr5MJCwspZSR2xQ8EYcgpsBl4OpayoRheICkeJzdeAEBii"
    "tlytM9gtX5OuaJ+UzroynixzpbHTnx/JimEauumM3FNGbLJbIqpYbAgCMBeKURVWfebyFl"
    "NUtB8BSWxeJSwBCglCocRt+Cfs8F18QYW6aD+j3TdZBldroTbGPLsVzkGjvw8mOmWBMmsn"
    "cWoQePAgvFVD7a3UXWcgkky1KV/BqMR18H40O7+0EdGMsXlr3Fszxi6dBCb4EEyjbRr2CF"
    "eQJ8V+jlktehXggl9vLSFdwLgPtDVV3j4KYR6nOixzEHErJTmGuuJ7JCxHyo4VjMq9wm2U"
    "+gi+JSFGo5KxzdL2d79a7I/mRXILLbNbgYDT5/MTTFCfJv7hHHXgWnisRWvKYsc5+HIita"
    "VxBDoe5fdaFqrpCts8gC+QaPXKa8jUnuwcBuYZNBp2s7lt01g5bdMh1sO2Z/0m6bges6tt"
    "vquP2W/d5sEsMd8eFv4FdW/jfNpplustP8X0kV+TBfdXw6Bop0c81Omu+wf5CbjHTxL+1v"
    "AJz40zr/yyMbDRCVOW/igHXzd8JE/fjVjpzCvHYbcgd7meu9cN5CdYpptZ2e49pdx5Upup"
    "Kl0tswgidnP//gYXfyu5VPybbmtbLkfbqW1elsYVsyq9G3dEyBLUGq0dgBYp7+PgG2W60t"
    "AMqsRoA6VgUoTxSQzWAV4reL87N6iCtL1kBeMtngFSa+ODqgJBHX+4l1A0XVtSo6SpJbug"
    "rv8Mfg9zrX0ffzoaYQJyLkehe9wXC3r+vrf14WT4K3Sd4="
)
