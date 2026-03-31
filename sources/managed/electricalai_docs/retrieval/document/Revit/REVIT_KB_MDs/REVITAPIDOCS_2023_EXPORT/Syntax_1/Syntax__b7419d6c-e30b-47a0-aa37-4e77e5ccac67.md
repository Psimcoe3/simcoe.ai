[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [RebarCoverType Class](b90685db-d2c5-aecb-ff1f-425ca2e5fae9.htm)   [See Also](#seeAlsoToggle) |

Creates a new CoverType in the document.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static RebarCoverType Create( 	Document doc, 	string name, 	double coverDistance ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document, _ 	name As String, _ 	coverDistance As Double _ ) As RebarCoverType ``` |

 

| Visual C++ |
| --- |
| ``` public: static RebarCoverType^ Create( 	Document^ doc,  	String^ name,  	double coverDistance ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

name
:   Type:  System String

coverDistance
:   Type:  System Double

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | coverDistance cannot be negative. |

# See Also

[RebarCoverType Class](b90685db-d2c5-aecb-ff1f-425ca2e5fae9.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)