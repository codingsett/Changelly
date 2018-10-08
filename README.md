## Changelly Exchange API Client

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
![PyPI - Python Version](https://img.shields.io/badge/Python-3.4%20%2F%203.5%20%2F%203.6%20%2F%203.7-blue.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


This module helps you to interact with changelly api easily from your Python3 applications.


## Installation

Use pip to install the module:

```
pip install changelly
```

## Basic Usage

Initialize changelly client object

```
from Changelly.changelly import ChangellyApi

client = ChangellyApi('apikey','apisecret')

params={
  	"from": "eth",
  	"to": "btc",
  	"amount": "1"
  }


x=client.getExchangeAmount('1',**params)

print(x)

```
## Documentation

* The Official API documentation can be found [here](https://api-docs.changelly.com/).


## Contributing

Feel free to contribute to this project.