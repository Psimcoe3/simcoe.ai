[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsReadOnly Property

---



|  |
| --- |
| [APIObject Class](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Identifies if the object is read-only or modifiable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool IsReadOnly { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property IsReadOnly As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property bool IsReadOnly { 	bool get (); } ``` |

#### Field Value

If true, the object may not be modified. If false, the object's contents may be modified.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Document project = uiApplication.ActiveUIDocument.Document;
Settings settings = project.Settings;
TaskDialog.Show("Revit","Categories: " + settings.Categories.IsReadOnly.ToString());
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim project As Document = uiApplication.ActiveUIDocument.Document
Dim settings As Settings = project.Settings
TaskDialog.Show("Revit", "Categories: " + settings.Categories.IsReadOnly.ToString())
```

# See Also

[APIObject Class](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)