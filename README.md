#  Verifier of AWS::IAM::Role Policy JSON files
## Requirements


- __python3 3.10.12__ or later

# Setup
Once the repository is cloned, the program is ready for use in console mode. You can use your own json files or those in the directory *./test/test_files*
__Example of use__
```bash
python3 verifier.py -d "./tests/test_files/IAM_Role_Policy_false.json"
python3 verifier.py --directory "./tests/test_files/IAM_Role_Policy_true.json"
```

# Display help message
When in doubt, you can prompt help message:
```bash
python3 verifier.py -h
python3 verifier.py --help
```

# Run unittest
You can use the following command in the program's root directory to run unittest
```bash
python3 -m pytest
```