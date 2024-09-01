USER_TYPE_CHOICES = [
    ("User", "User"),
    ("Admin", "Admin"),
]

PERMISSION_CODENAMES = {
    "manage_example": {
        "permissions": [
            "add_example",
            "change_example",
            "delete_example",
            "view_example",
        ],
        "otherAtt": "OtherVal",
    },
}
CODENAME_TO_RIGHTS = {
    codename: right
    for right, data in PERMISSION_CODENAMES.items()
    for codename in data["permissions"]
}
