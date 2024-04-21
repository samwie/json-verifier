json_false = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": ["iam:ListRoles", "iam:ListUsers"],
                "Resource": "*",
            }
        ],
    },
}

json_true = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": ["iam:ListRoles", "iam:ListUsers"],
                "Resource": "123",
            }
        ],
    },
}
