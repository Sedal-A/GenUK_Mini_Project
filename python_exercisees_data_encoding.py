# Data encoding exercises
​# Reading and writing CSV
​
1. Read the `ford_escort.csv` example file using the Python csv library and print each row. Remember there's a header line!
​
1. Extend the above so that the data is read into a dictionary.
​
1. Write the following data as CSV to a file. Add a header row with likely column titles.
​
```py
['Joe', 'Bloggs', 40]
['Jane', 'Smith', 50]
```
​
1. Write another block of code that will __append__ the following data to the file created in #3.
​
```py
['Mike', 'Wazowski', 40]
```











import ford_escort.csv

with open(ford_escort, mode"w") as file:
    reader = csv.Dictreader(file, delimiter = " ")
    for row in reader:
        print(row)
​











## Reading and writing JSON
​
1. Read the `example.json` handout file using the native Python json library. Print the object that is created
​
1. Print the "id" of all the items in the menu
​
1. Write the following data as JSON to a file.
​
```py
{
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}
```



{
    "menu": {
        "items": [
            {"id": "Open"},
            {"id": "OpenNew", "label": "Open New"},
            {"id": "ZoomIn", "label": "Zoom In"},
            {"id": "ZoomOut", "label": "Zoom Out"},
            {"id": "OriginalView", "label": "Original View"},
            {"id": "Quality"},
            {"id": "Pause"},
            {"id": "Mute"},
            {"id": "Find", "label": "Find..."},
            {"id": "FindAgain", "label": "Find Again"},
            {"id": "Copy"},
            {"id": "CopyAgain", "label": "Copy Again"},
            {"id": "CopySVG", "label": "Copy SVG"},
            {"id": "ViewSVG", "label": "View SVG"},
            {"id": "ViewSource", "label": "View Source"},
            {"id": "SaveAs", "label": "Save As"},
            {"id": "Help"},
            {"id": "About", "label": "About Adobe CVG Viewer..."}
        ]
    }
}









