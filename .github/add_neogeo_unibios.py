import json
import zipfile

with open('db.json', 'r') as file:
    data = json.load(file)

del data['base_files_url']
del data['db_url']

data['archives'] = {
    "neogeo_unibios": {
        "archive_file": {
            "hash": "1986c39676354d19ae648a914bd914f7",
            "size": 101498,
            "url": "http://unibios.free.fr/download/uni-bios-40.zip"
        },
        "description": "Extracting NeoGeo UniBios from http://unibios.free.fr",
        "summary_inline": {
            "files": {
                "games/NEOGEO/uni-bios.rom": {
                    "hash": "4f0aeda8d2d145f596826b62d563c4ef",
                    "size": 131072,
                    "tags": [
                        data['tag_dictionary']['bios'],
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ],
                    "path": "pext",
                    "arc_id": "neogeo_unibios",
                    "arc_at": "uni-bios.rom"
                }
            },
            "folders": {
                "games/NEOGEO": {
                    "arc_id": "neogeo_unibios",
                    "tags": [
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ],
                    "path": "pext"
                }
            }
        },
        "format": "zip",
        "extract": "selective",
    },
    "neogeo_unibioscd": {
        "archive_file": {
            "hash": "e2ec14752f65aef00fc33e68cf2fc301",
            "size": 381292,
            "url": "http://unibios.free.fr/download/uni-bioscd-33.zip"
        },
        "description": "Extracting NeoGeo CD UniBios from http://unibios.free.fr",
        "summary_inline": {
            "files": {
                "games/NeoGeo-CD/uni-bioscd.rom": {
                    "hash": "08ca8b2dba6662e8024f9e789711c6fc",
                    "size": 524288,
                    "tags": [
                        data['tag_dictionary']['bios'],
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ],
                    "path": "pext",
                    "arc_id": "neogeo_unibioscd",
                    "arc_at": "uni-bioscd.rom"
                }
            },
            "folders": {
                "games/NeoGeo-CD": {
                    "arc_id": "neogeo_unibioscd",
                    "tags": [
                        data['tag_dictionary']['games'],
                        data['tag_dictionary']['neogeo']
                    ],
                    "path": "pext"
                }
            }
        },
        "format": "zip",
        "extract": "selective",
    }
}

with open('bios_db.json', 'w') as output_file:
    json.dump(data, output_file)

with zipfile.ZipFile('bios_db.json.zip', 'w', zipfile.ZIP_DEFLATED) as zipped_file:
    zipped_file.writestr('bios_db.json', json.dumps(data))
