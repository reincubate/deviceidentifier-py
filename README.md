# DeviceIdentifier API Python library

Utils to manipulate and learn from assorted device identifier formats via Reincubate's [DeviceIdentifier API](https://www.reincubate.com/deviceidentifier-api/).

Technical documentation is available on [Reincubate's site](https://docs.reincubate.com/deviceidentifier/?utm_source=github&utm_medium=deviceidentifier-py&utm_campaign=deviceidentifier).

## Getting started

Try these:

```bash
$ pip install deviceidentifier
```

Calls to the API through this client then become easy:

```python
from deviceidentifier import api

# Look up an Apple serial number
api.lookup( api.TYPE_APPLE_SERIAL, 'C8QH6T96DPNG' )

# Identify the type of an identifier
api.identify_identifier( 'iPhone5,3' )

# Triangulate a bunch of data from a collection of identifiers
api.enhance_metadata(
    apple_identifier='iPhone5,3',
    apple_serial='C8QH6T96DPNG',
    gsma_imei='013554006297015',
    gsma_iccid='8965880812100011146'
)
```

The API supports anonymous access, and provides limited, rate-limited data when doing so. Tokens can be obtained by contacting [Reincubate](mailto:enterprise@reincubate.com), and either by setting an environment variable:

```bash
$ export RI_DEVID_TOKEN='api-authentication-token'
```

Or by passing the token value directly into the code:

```python
from deviceidentifier import api

# Look up an Apple serial number
api.lookup( api.TYPE_APPLE_SERIAL, 'api-authenticaton-token', 'C8QH6T96DPNG' )
```

## Using the command-line interface

### Apple

#### Apple serial numbers: legacy (80s & 90s), old (early 2000s) and post-2010 formats

```bash
$ python -m deviceidentifier.cli.apple_serial C8QH6T96DPNG
```

```json
{
    "anonymised": "C8QH6•••DPNG",
    "configurationCode": {
        "code": "DPNG",
        "image": {
            "height": 120,
            "url": "https://di-api.reincubate.com/resource-159c9e87a3d6bbf5075bb030fa2925a0/",
            "width": 120
        },
        "skuHint": "iPhone 4 CDMA (8GB)"
    },
    "coverageUrl": "https://checkcoverage.apple.com/gb/en?sn=C8QH6T96DPNG",
    "id": "C8QH6T96DPNG",
    "manufacturing": {
        "city": "",
        "company": "",
        "country": "China",
        "date": "2012-02-05",
        "flag": "🇨🇳",
        "id": "C8Q"
    },
    "serialType": "2010",
    "uniqueId": {
        "productionNo": 31524,
        "value": "T96"
    }
}
```

#### Apple model numbers

```bash
$ python -m deviceidentifier.cli.apple_model MC605FD/A
```
```json
{
    "anonymised": "C605",
    "appleIdentifier": {
        "id": "iPhone3,1",
        "image": {
            "height": 330,
            "url": "https://di-api.reincubate.com/resource-26b007e1007180a28e272036775a48a0/",
            "width": 450
        },
        "product": {
            "line": "iPhone",
            "sku": "iPhone 4"
        },
        "variant": "GSM"
    },
    "id": "C605",
    "region": {
        "flags": "🇦🇹🇱🇮🇨🇭",
        "name": "Austria, Liechtenstein, Switzerland"
    },
    "specification": {
        "case_size": "",
        "colour": "Black",
        "material": "",
        "storage": "32 GB"
    },
    "type": "Retail"
}
```

#### Apple identifiers

```bash
$ python -m deviceidentifier.cli.apple_identifier iPhone5,3
```
```json
{
    "id": "iPhone5,3",
    "image": {
        "height": 330,
        "url": "https://di-api.reincubate.com/resource-775ac9634280be8d7dfb0b75b4727f69/",
        "width": 450
    },
    "product": {
        "line": "iPhone",
        "sku": "iPhone 5c"
    },
    "variant": "GSM + CDMA"
}
```

#### Apple internal names

```bash
$ python -m deviceidentifier.cli.apple_internal_name N92AP
```
```json
{
    "appleIdentifier": {
        "id": "iPhone3,3",
        "image": {
            "height": 330,
            "url": "https://di-api.reincubate.com/resource-1e7820cb714e3d477534f291c0f87e83/",
            "width": 450
        },
        "product": {
            "line": "iPhone",
            "sku": "iPhone 4"
        },
        "variant": "CDMA"
    }
}
```

#### Apple IDFA / IDFV

```bash
$ python -m deviceidentifier.cli.apple_idfa 002ebf12-a125-5ddf-a739-67c3c5d20177
```
```json
{
    "anonymised": "••••••••-••••-••••-••••-••••••••••••",
    "formatted": "002ebf12-a125-5ddf-a739-67c3c5d20177"
}
```

#### Apple UDIDs

```bash
$ python -m deviceidentifier.cli.apple_udid db72cb76a00cb81675f19907d4ac2b298628d83c
```
```json
{
    "anonymised": "••••••••••••••••••••••••••••••••••••••••",
    "compromised": false,
    "formatted": "db72cb76a00cb81675f19907d4ac2b298628d83c"
}
```

#### Apple "A" numbers

```bash
python -m deviceidentifier.cli.apple_anumber A1784
```
```json
{
    "appleIdentifier": {
        "id": "iPhone9,4",
        "image": {
            "height": 330,
            "url": "https://di-api.reincubate.com/resource-d8c14fc2a4dfcf27d5a217fb5e4c0cc4/",
            "width": 450
        },
        "product": {
            "line": "iPhone",
            "sku": "iPhone 7 Plus"
        },
        "variant": "GSM"
    }
}
```

### CDMA

#### Mobile Equipment Identifier (MEIDs)

```bash
$ python -m deviceidentifier.cli.cdma_meid 354403064522046
```

```json
{
    "anonymised": "35440306••••••6",
    "checksum": "6",
    "id": "354403064522046",
    "manufacturer": "440306",
    "pESN": "808D1904",
    "regionCode": {
        "code": "35",
        "group": "Comreg",
        "origin": "Ireland"
    },
    "serial": "452204"
}
```

### GSMA

#### IMEIs (enriched with data from Apple's GSX service for clients with access)

```bash
$ python -m deviceidentifier.cli.gsma_imei 013554006297015
```

```json
{
    "anonymised": "01355400••••••5",
    "checksum": "5",
    "gsmaTac": {
        "appleModel": {
            "anonymised": "D298",
            "appleIdentifier": {
                "id": "iPhone5,2",
                "image": {
                    "height": 330,
                    "url": "https://di-api.reincubate.com/resource-c2aac9e5e3695fca1090633a4ea1b60d/",
                    "width": 450
                },
                "product": {
                    "line": "iPhone",
                    "sku": "iPhone 5"
                },
                "variant": "CDMA + LTE"
            },
            "id": "D298",
            "region": {
                "flags": null,
                "name": null
            },
            "specification": {
                "case_size": "",
                "colour": "White",
                "material": "",
                "storage": "16 GB"
            },
            "type": "Retail"
        },
        "id": "01355400",
        "manufacturer": "Apple",
        "product": {
            "line": "iPhone",
            "sku": "iPhone 5"
        }
    },
    "gsx": {
        "appleSerial": {
            "anonymised": "F2TK4•••DTWF",
            "configurationCode": {
                "code": "DTWF",
                "image": {
                    "height": 120,
                    "url": "https://di-api.reincubate.com/resource-4cb3c6fe7c62f327cd11712196c221b0/",
                    "width": 120
                },
                "skuHint": "iPhone 5 (GSM, CDMA)"
            },
            "coverageUrl": "https://checkcoverage.apple.com/gb/en?sn=F2TK4TZ7DTWF",
            "id": "F2TK4TZ7DTWF",
            "manufacturing": {
                "city": "Zhengzhou",
                "company": "Foxconn",
                "country": "China",
                "date": "2013-01-22",
                "flag": "🇨🇳",
                "id": "F2T"
            },
            "serialType": "2010",
            "uniqueId": {
                "productionNo": 32341,
                "value": "TZ7"
            }
        },
        "sale": {
            "estimatedPurchaseDate": "2013-04-10",
            "initialCarrier": "Sweden Tele2.",
            "realPurchaseDate": "2013-04-10",
            "saleRegion": "Sweden",
            "saleRegionFlag": "🇸🇪",
            "seller": "TELE2 SVERIGE AB"
        },
        "skuHint": "IPHONE 5",
        "specifications": [
            "WHITE",
            "16GB",
            "GSM"
        ],
        "status": {
            "appleId": null,
            "coverage": "Out Of Warranty (No Coverage)",
            "sim": "Locked"
        }
    },
    "id": "013554006297015",
    "reportingBodyIdentifier": {
        "code": "01",
        "group": "PTCRB",
        "origin": "United States"
    },
    "serial": "629701",
    "svn": null,
    "type": "IMEI"
}
```

#### Type allocation codes (TAC)

```bash
$ python -m deviceidentifier.cli.gsma_tac 01326300
```
```json
{
    "appleModel": {
        "anonymised": "D198",
        "appleIdentifier": {
            "id": "iPhone3,1",
            "image": {
                "height": 330,
                "url": "https://di-api.reincubate.com/resource-26b007e1007180a28e272036775a48a0/",
                "width": 450
            },
            "product": {
                "line": "iPhone",
                "sku": "iPhone 4"
            },
            "variant": "GSM"
        },
        "id": "D198",
        "region": {
            "flags": "🇮🇳",
            "name": "India"
        },
        "specification": {
            "case_size": null,
            "colour": "White",
            "material": null,
            "storage": "8 GB"
        },
        "type": "Retail"
    },
    "id": "01326300",
    "manufacturer": "Apple",
    "product": {
        "line": "iPhone",
        "sku": "iPhone 4"
    }
}
```

#### ICCIDs

```bash
$ python -m deviceidentifier.cli.gsma_iccid 8965880812100011146
```

```json
{
    "anonymised": "896588••••••••••••6",
    "atiiccid": null,
    "checksum": "6",
    "issuer": {
        "code": "88",
        "country": {
            "code": "65",
            "flag": "🇸🇬",
            "name": "Singapore"
        },
        "name": null
    },
    "majorIndustry": {
        "code": "89",
        "industry": "Telecommunications administrations and private operating agencies",
        "type": "Healthcare, telecommunications and other future industry assignments"
    },
    "month": "08",
    "simNumber": "001114",
    "switch": "10",
    "year": "12"
}
```

### Identifying an identifier

```bash
$ python -m deviceidentifier.cli.identify_identifier iPhone5,3
```

```json
{
    "iPhone5,3": [
        "apple_identifier"
    ]
}
```

## Troubleshooting

See the [support & service status](https://docs.reincubate.com/ricloud/status/?utm_source=github&utm_medium=deviceidentifier-py&utm_campaign=deviceidentifier) page.

## <a name="more"></a>Need more functionality?

Reincubate's vision is to provide data access, extraction and recovery technology for all app platforms - be they mobile, desktop, web, appliance or in-vehicle.

The company was founded in 2008 and was first to market with both iOS and iCloud data extraction technology. With over half a decade's experience helping law enforcement and security organisations access iOS data, Reincubate has licensed software to government, child protection and corporate clients around the world.

The company can help users with:

* iCloud access and data recovery
* Recovery of data deleted from SQLite databases
* Bulk iOS data recovery
* Forensic examination of iOS data
* Passcode, password, keybag and keychain analysis
* Custom iOS app data extraction
* Advanced PList, TypedStream and Mbdb manipulation

Contact [Reincubate](https://www.reincubate.com/?utm_source=github&utm_medium=deviceidentifier-py&utm_campaign=deviceidentifier) for more information.

## Terms & license

See the `LICENSE` file for details on this implementation's license. Users must not use the API in any way that is unlawful, illegal, fraudulent or harmful; or in connection with any unlawful, illegal, fraudulent or harmful purpose or activity.
