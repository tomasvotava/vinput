# vinput
Console Input with Validation options


## Requirements
So far, ***vinput*** requires that you have [pformat](https://github.com/tomasvotava/pformat) installed. 

## Usage
### Install prerequisites
#### pformat
```bash
$ git clone https://github.com/tomasvotava/pformat
$ cd pformat
$ ./setup.py install
```

### Install VInput
```bash
$ git clone https://github.com/tomasvotava/vinput
$ cd vinput
$ ./setup.py install
```

### Usage
```python
from vinput import vinput, VALID_LIST
answer = vinput("Do you want to quit smoking?",default=None,validation=VALID_LIST,options=["yes","no"])
print("You answered %s."%answer)
```
