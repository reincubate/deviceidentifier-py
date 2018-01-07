# deviceidentifier

Utils to manipulate and learn from assorted device identifier formats via Reincubate's [DeviceIdentifier API](https://www.reincubate.com/deviceidentifier-api/) API.

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

##### Apple serial numbers: legacy (80s & 90s), old (early 2000s) and post-2010 formats

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

##### Apple model numbers

```bash
$ python -m deviceidentifier.cli.apple_model MC605LL/A
```
```json
{
    "identifiers": {
        "apple_model": {
            "code": "C605",
            "region": "USA, Canada, or replacement unit",
            "appleIdentifierLookup": {
                "sku": "iPhone 4",
                "variant": "GSM"
            },
            "type": "Retail",
            "colour": "Black",
            "appleIdentifier": "iPhone3,1",
            "size": "32GB"
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

##### Apple identifiers

```bash
$ python -m deviceidentifier.cli.apple_identifier iPhone5,3
```
```json
{
    "identifiers": {
        "apple_identifier": {
            "sku": "iPhone 5c",
            "variant": null
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

##### Apple internal names

These are referred to as the "board ID" in some areas by Apple. However, it is not the same as the [BOaRD ID](https://www.theiphonewiki.com/wiki/BORD) or the logic board ID that Macs use (eg. *Mac-F4208DC8*), and as such we felt that term was unhelpful.

```bash
$ python -m deviceidentifier.cli.apple_internal_name N92AP
```
```json
{
    "identifiers": {
        "apple_identifier": {
            "sku": "iPhone 4",
            "variant": "CDMA"
        },
        "identifier": "iPhone3,3"
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

##### Apple UDIDs

```bash
$ python -m deviceidentifier.cli.apple_udid B958E359-34C2-42F4-BD0C-C985E6D5376B
```
```json
{
    "identifiers": {
        "apple_udid": {
            "valid": true,
            "compromised": false
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

##### Apple "A" numbers

```bash
python -m deviceidentifier.cli.apple_anumber A1586
```
```json
{
    "identifiers": {
        "apple_identifier": {
            "sku": "iPhone 6",
            "variant": null
        },
        "identifier": "iPhone7,2"
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

#### CDMA

##### Mobile Equipment Identifier (MEIDs)

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

##### IMEIs (enriched with data from Apple's GSX service for clients with access)

```bash
$ python -m deviceidentifier.cli.gsma_imei 990001858419963
```

```json
{
    "identifiers": {
        "gsma_imei": {
            "svn": null,
            "gsx": {
                "realPurchaseDate": "2012-11-19",
                "simStatus": "Locked",
                "initialCarrier": "Sprint - United States USA",
                "seller": "SPRINT PURCH AGENCY NEXTEL SYS CORP",
                "coverageStatus": "Out Of Warranty (No Coverage)",
                "appleSerial": "DX4JJSKCDTD3",
                "appleId": null,
                "model": "IPHONE 4S,MM,16GB,WHITE",
                "saleRegion": "United States",
                "estimatedPurchaseDate": "2012-11-19"
            },
            "reportingBodyIdentifier": {
                "origin": "For multi RAT 3GPP2/3GPP",
                "code": "99",
                "group": "GHA"
            },
            "checksum": "3",
            "tac": "99000185",
            "tacLookup": {
                "product": "iPhone 4s",
                "modelCode": null,
                "manufacturer": "Apple"
            },
            "serial": "841996",
            "type": "IMEI",
            "appleSerialLoopup": {
                "manufactureDate": "2012-10-07",
                "configurationCode": {
                    "colour": null,
                    "code": "DTD3",
                    "size": null
                },
                "uniqueId": {
                    "productionNo": 30714,
                    "value": "SKC"
                },
                "coverageUrl": "https://checkcoverage.apple.com/gb/en?sn=DX4JJSKCDTD3",
                "configuration": {
                    "sku": "iPhone 4S",
                    "image": {
                        "url": "https://di-api.reincubate.com/resource-b07a09fb6ea5fad57fb4254240b8d0f2/",
                        "x": 120,
                        "y": 120
                    }
                },
                "serialType": "2010",
                "manufacturer": "DX4"
            }
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

##### Type allocation codes (TAC)

```bash
$ python -m deviceidentifier.cli.gsma_tac 01326300
```
```json
{
    "identifiers": {
        "gsma_tac": {
            "product": "iPhone 4",
            "modelCode": "MD198HN/A",
            "manufacturer": "Apple"
        }
    },
    "system": {
        "message": "",
        "code": "ok"
    }
}
```

##### ICCIDs

```bash
$ python -m deviceidentifier.cli.gsma_iccid 8965880812100011146
```

```json
{
    "identifiers": {
        "gsma_iccid": {
            "atiiccid": null,
            "simNumber": "001114",
            "majorIndustry": {
                "industry": "Telecommunications administrations and private operating agencies",
                "code": "89",
                "type": "Healthcare, telecommunications and other future industry assignments"
            },
            "checksum": "6",
            "year": "12",
            "month": "08",
            "switch": "10",
            "issuer": {
                "country": {
                    "code": "65",
                    "name": "India"
                },
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
