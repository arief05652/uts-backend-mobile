from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `urls` MODIFY COLUMN `password` VARCHAR(255);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `urls` MODIFY COLUMN `password` VARCHAR(255) NOT NULL;"""


MODELS_STATE = (
    "eJztmVtPIjEUgP8K4UkTMYiAuG+IuLKusFHcNRozqdMCDZ0WOx2RGP77tmXuDKPj4gKGN+"
    "ZcZtqvPef0lNe8xSAi9n6DOVTkv+Ve8xRYSP6IKvZyeTAaBWIlEOCRaEvTN3m0BQemek8P"
    "EBtJEUS2yfFIYEallDqEKCEzpSGm/UDkUPzkIEOwPhIDxKXi/kGKMYXoBdne42ho9DAiMD"
    "JQ/XkDQzUCrTXEZKQ1jQHgZ9peffTRMBlxLBr3GU3EgFHfSY5MSfuIIg4EgqHJqLG6k/ZE"
    "s3FLgeAO8gcMAwFEPeAQhSQPa5VirdQrFyrF40qhfHRsFkC5AgoVVC32pFnvqFbNZ2BmMq"
    "p4YypsDcQCLwZBtC8G8vGwOp1NOkAys1Ij+V2/apzXr3YOq7vqg0wu2mwp266mpFVT/Qog"
    "wOwlehkC7o6NuAEkJ5GFfNRrOew9QQA/2H4efQ/jMtiWKpV3wJVWC+lqncIb4BTYQrYA1m"
    "ie5qlkodTJRCOOMaDQ9dz3fqwpXo4A7FAyceMmhW63ddm87tYvf6mZWLb9RDSherepNCUt"
    "ncSkO/Ft7r8k96fVPc+px9xdp93UBJkt+lx/MbDr3uXVmIAjmEHZ2AAwFOKeNBh8KEg4yZ"
    "iaAo/NDI7lJB6V7XvD5LzDyTzPM8YR7tMLNNFUW3KAgJooAaNb1274rIqtH86ptyM8abDT"
    "OBj7BTC0UeTs5JyQmO2s+nWjftrMa4SPwByOAYdGhKXSsBKLSXzbeZVVsuISQGUSh+4k1J"
    "DDXBPOER7vxccIx7NYySli9YH69gli/cI07XzAOO5jCohBMB3Og+2iF5EMds5xUxJhWtlq"
    "3nYjFcsjuXNZv92NVK2fnfZ3zzxEvvGzcxI7MpiOyAw37LPlmsx1BGx7zHimbBD2+RBXN9"
    "q/1qHWlAc7gQyQ0CKkH2ojjttD7UoPtRpMZFll9cZyHvADCxtz3S7tmvUrqj3PeA4KXDal"
    "oPzvjkUSWkbLIl+z6T1LsFeyNi2xCz97HuiJ63d2cYUI0FNYyNK/1twcltNPbdv03krq27"
    "xNl9K4+Sar6dzWIGV9td5NA4LoGZvoI2gjntuisChiF19w/WN227zLrU9NbnXEsTlIym6u"
    "JjW9gcBmJfktKf5adEF7nxhyeL7UuflppTmtr75SKB2Uj8q1w2q5Jk30SHzJUUoIttrdN3"
    "LYs6xKbpS8N3mFXDYza31KE69CIwNE13wzAR4Ui+8AKK0WAtS62C0IoyLxb9If1532oj+o"
    "fZcYyBsqJ3gPsSn2cgTb4mE9saZQVLNOv7OLX8/tRdtc9YKTbNV1+eVl+hfZw7IV"
)
