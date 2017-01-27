# configattr
Converts a ConfigParser import to a set of attributes for ease of use. Normal configparser objects are referenced like so:
```
config['item1']['item2']
```

configattr allows you to access the same data as attributes:
```
config.item1.item2
```

## Installation
The easiest way to install is with pip from github. This will grab the correct dependencies (configparser) and install. 
```
pip install git+https://github.com/Magicked/configattr.git
```

You can also clone directly:
```
git clone https://github.com/Magicked/configattr.git
cd configattr
pip install -r requirements.txt
python setup.py install
```

## Usage
configattr can be imported into your python projects. 

```
from configattr.config import Config

config = Config('/path/to/config.ini')

# Use it however you want now
proxies = {
    'http' : config.proxy.http,
    'https' : config.proxy.https
}
```
