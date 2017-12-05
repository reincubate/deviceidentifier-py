# deviceidentifier

Utils to manipulate and learn from assorted device identifier formats via Reincubate's API.

## Getting started

Try these:

```bash
$ pip install deviceidentifier
$ export RI_DEVID_TOKEN='api-authentication-token'
```

## Requesting an access token

Authentication to ricloud is performed using a token provided by Reincubate, which can be obtained by contacting [enterprise@reincubate.com](mailto:enterprise@reincubate.com).

## Usage

### Enhancing metadata

#### Apple

* Apple's serial numbers: legacy (80s & 90s), old (early 2000s) and post-2010 formats

```bash
$ python -m deviceidentifier.cli.apple_serial 5K31926NDZZ
```

```json
{
    "identifiers": {
        "apple_serial": {
            "manufactureDate": "2003-05-07",
            "configurationCode": {
                "colour": null,
                "code": "DZZ",
                "size": null
            },
            "uniqueId": {
                "productionNo": 2538,
                "value": "26N"
            },
            "coverageUrl": "https://checkcoverage.apple.com/gb/en?sn=5K31926NDZZ",
            "configuration": {
                "sku": "iPhone 4",
                "image": {
                    "url": "https://di-api.reincubate.com/resource-159c9e87a3d6bbf5075bb030fa2925a0/",
                    "x": 120,
                    "y": 120
                }
            },
            "serialType": "old",
            "manufacturer": "China (refurbished)"
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

* Apple model numbers

```bash
$ python -m deviceidentifier.cli.apple_model PC605B
```
```json
{
    "identifiers": {
        "apple_model": {
            "region": "Ireland, UK, or replacement unit",
            "code": "C605",
            "type": "Personalised"
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

* Apple identifiers

```bash
$ python -m deviceidentifier.cli.apple_identifier iPhone5,3
```
```json
{
    "identifiers": {
        "apple_identifier": {
            "sku": "iPhone 5C"
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

* Apple internal names

```bash
$ python -m deviceidentifier.cli.apple_internal_name N90AP
```
```json
{
    "identifiers": {
        "apple_internal_name": {
            "identifier": null
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

* Apple UDIDs

```bash
$ python -m deviceidentifier.cli.apple_udid 49BBEEE741F04245B245E8842E85CCF0
```
```json
{
    "identifiers": {},
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

* Apple "A" numbers

```bash
python -m deviceidentifier.cli.apple_anumber A1586
```
```json
{
    "identifiers": {},
    "system": {
        "message": "Not implemented",
        "code": "error"
    }
}
```

#### CDMA

* ESNs (not implemented yet in this client)

* Mobile Equipment Identifier (MEIDs)

```bash
$ python -m deviceidentifier.cli.cdma_meid 354403064522046
```

```json
{
    "identifiers": {
        "cdma_meid": {
            "checksum": "6",
            "serial": "452204",
            "regionCode": {
                "origin": "Ireland",
                "code": "35",
                "group": "Comreg"
            },
            "pESN": "808D1904",
            "manufacturer": "440306"
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

#### GSMA

* IMEIs

```bash
$ python -m deviceidentifier.cli.gsma_imei 352073069165968
```

```json
{
    "identifiers": {
        "gsma_imei": {
            "svn": null,
            "reportingBodyIdentifier": {
                "origin": "Ireland",
                "code": "35",
                "group": "Comreg"
            },
            "checksum": "8",
            "tac": {
                "model": null,
                "code": "35207306",
                "modelCode": null,
                "manufacturer": null
            },
            "serial": "916596",
            "type": "IMEI"
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

* Type allocation codes (TAC)

```bash
$ python -m deviceidentifier.cli.gsma_tac
```
```json
{
    "identifiers": {
        "gsma_tac": {

        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```


* ICCIDs

```bash
$ python -m deviceidentifier.cli.gsma_iccid 8965880812100011146
```

```json
{
    "identifiers": {
        "gsma_iccid": {
            "atiiccid": null,
            "simNunber": "001114",
            "majorIndustry": {
                "industry": "Telecommunications administrations and private operating agencies",
                "code": "89",
                "type": "Healthcare, telecommunications and other future industry assignments"
            },
            "checksum": "6",
            "year": "12",
            "month": "August",
            "switch": "10",
            "country": "65",
            "issuer": {
                "code": "88",
                "name": "EZI-PhoneCard"
            }
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

### Identifying an identifier

```bash
$ python -m deviceidentifier.cli.identify iPhone5,2
```

```json
{
    "identifiers": {
        "iPhone5,2": "apple_identifier"
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

## API client implementations

Check out the Open Source libraries for working with the API:

* [Python](https://github.com/reincubate/deviceidentifier-py)
* [C# / .NET](https://github.com/reincubate/deviceidentifier-csharp)

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
