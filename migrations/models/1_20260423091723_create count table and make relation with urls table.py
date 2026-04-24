from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `count` (
    `count_id` VARCHAR(36) NOT NULL PRIMARY KEY DEFAULT '984fea9e-4c31-4c0d-ace3-f91e68e5aac4',
    `user_agent` VARCHAR(255) NOT NULL,
    `timestamp` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `url_id` VARCHAR(36) NOT NULL,
    CONSTRAINT `fk_count_urls_aee522f1` FOREIGN KEY (`url_id`) REFERENCES `urls` (`url_id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
        ALTER TABLE `urls` ADD `password` VARCHAR(255) NOT NULL;
        ALTER TABLE `urls` ADD `cut_link` LONGTEXT NOT NULL;
        ALTER TABLE `urls` ADD `create_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `urls` ADD `original_link` LONGTEXT NOT NULL;
        ALTER TABLE `urls` ADD `modified_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `urls` DROP COLUMN `password`;
        ALTER TABLE `urls` DROP COLUMN `cut_link`;
        ALTER TABLE `urls` DROP COLUMN `create_at`;
        ALTER TABLE `urls` DROP COLUMN `original_link`;
        ALTER TABLE `urls` DROP COLUMN `modified_at`;
        DROP TABLE IF EXISTS `count`;"""


MODELS_STATE = (
    "eJztmW1v2jgcwL8K4lUnNROEQOHeUUZv3FaYWnY3bZoiYztgNbGZ46xFE9/9bJNnAkdWeh"
    "CpbxD8Hxz7F/v/YH7VPYaw678dsICK+h+1X3UKPCy/ZBWXtTpYLhOxEggwc7UljE1mvuAA"
    "qnEc4PpYihD2ISdLQRiVUhq4rhIyKA0JnSeigJIfAbYFm2OxwFwqvn2XYkIRfsJ+9HP5YD"
    "sEuygzUf14myA1A621xWqpNYMF4DfaXj10ZkPmBh7N+yxXYsFo7CRnpqRzTDEHAqPUYtRc"
    "w0VHos28pUDwAMcTRokAYQcErkJS73UtB4MeNizYasqPBjIAxC3D6TVxp4vbAECrXoIZZF"
    "TxJlT4GogHnmwX07lYyJ+tznqz6ATJxkrN5O/+3eB9/+6i1XmjHsjkS9u8ynGoMbVqrYcA"
    "AmwG0a8h4R74mNtAchJlyGe9jsM+EiTwk+0X0Y8wHoOt2W4fAFda7aSrdQpvglMQD/sCeM"
    "ttmu8kC6UuJppxzAFFoefb6MuZ4uUYoAl1V+G52UN3Orod3k/7t5/USjzf/+FqQv3pUGlM"
    "LV3lpBf5bR4PUvtnNH1fUz9rXyfjoSbIfDHn+omJ3fRrXc0JBILZlD3aAKWOeCRNJp86JN"
    "wtGZoSj2oejuMEHhXtnYfiuMPdbZ43jGMypx/wSlMdyQkCCnEBxjCvfeabLHZ+ONfRjoik"
    "yU7j4DFOgKmNIlcn14TFZmf17wf9d8O6RjgD8OERcGRnWCoNM1lOEttuqzzTy0sAlUEchY"
    "tQU05zLagjIt67y4ggsjhJFXH6g3pABWGiqzZodhzD6jqygkBtaPQcExodp9mE1sx0mjNY"
    "oQqCcTInFLi2S+jDNvopfhLF6LccqxIq9yW24ZdpJqdFJC9u+1/eZPLax8n4z8g8RX7wcX"
    "KdKypgIErDTfu8ci3mugS+/8h4qXiR9qkK1/+h7oWy9hPYBgVdxP66N+P4WveetO7VYDKv"
    "VSZ4IteBfuPF5lxfX+2ZtTSqgy9ZKiUu1Yx8L9/USELH6GrkMFVva5K9Uravyd0J+ttAr0"
    "O/mw932AV6CTtZxjef1WG5ftHOTu+totYu2nR7ervY5DTN3RmErAPau0YLNnoYzYwO7JmG"
    "dYXaBoAzbJioNWtYADpt0KtQe6cRIvyTQPw78DOer2lj15nefUv2zPhXvRuyFw1/fcwJXB"
    "TFv1CzNwCCxOYkEbDo/I3ojhuAwiNHtpNhGMGeF/Weed7m6imG2bSurG6rY3WliZ5JLLna"
    "cwRH4+l/xLCfMm+Fp+TQ4JVyqWbUepE2Xx2NEhBD82oCbDYaBwCUVjsBal3unoRRUfhf61"
    "/3k/Guf7ljlxzIz1Qu8BsiUFzWXOKL7+eJdQ9Fter913r5G7zLbCOsBrgul12Pn17W/wLb"
    "CMRL"
)
