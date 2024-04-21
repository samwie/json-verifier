import json


class RolePolicyParser:
    """
    A class for parsing AWS::IAM::Role Policy JSON
    """

    def __init__(self, loc: str):
        self.loc = loc

    def load(self) -> dict:
        """
        Method to load data from a JSON file and return it as a dictionary
        """

        try:
            with open(self.loc, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error reading file: {e}")
        except ValueError as e:
            raise ValueError(f"Error processing data: {e}")

    def verify(self) -> bool:
        """
        Method to check if the role policies in the JSON file are valid.
        """

        self.data = self.load()
        try:
            policy = self.data["PolicyDocument"]
            statements = policy["Statement"]
            if not statements:
                raise KeyError("Resource")
            for statement in statements:
                resource = statement["Resource"]
                if isinstance(resource, (str, int, float)):
                    if resource == "*":
                        return False
                    else:
                        return True
                else:
                    raise TypeError(f"Resource is instance, {type(resource).__name__}")

        except KeyError as e:
            raise KeyError(f"Missing key in JSON file:{e}")
        except TypeError as e:
            raise TypeError(f"Type error occured:{e} ")
