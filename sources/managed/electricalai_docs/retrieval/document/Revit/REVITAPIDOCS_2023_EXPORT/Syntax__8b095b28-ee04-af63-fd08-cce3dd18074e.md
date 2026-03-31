[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [CircuitNamingScheme Class](99de5fb2-6e65-7b1f-1866-347c40d427af.htm)   [See Also](#seeAlsoToggle) |

Creates a new CircuitNamingScheme.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static CircuitNamingScheme Create( 	Document document, 	string name, 	IList<TableCellCombinedParameterData> data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String, _ 	data As IList(Of TableCellCombinedParameterData) _ ) As CircuitNamingScheme ``` |

 

| Visual C++ |
| --- |
| ``` public: static CircuitNamingScheme^ Create( 	Document^ document,  	String^ name,  	IList<TableCellCombinedParameterData^>^ data ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the CircuitNamingScheme.

name
:   Type:  System String    
     The name of CircuitNamingScheme.

data
:   Type:  System.Collections.Generic IList   [TableCellCombinedParameterData](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)    
     The array of TableCellCombinedParameterData to be set as combined parameters.

#### Return Value

The newly created CircuitNamingScheme.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is an empty string or contains only whitespace. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- The given value for name is already in use as a CircuitNamingScheme name. -or- The data contains invalid parameter id. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CircuitNamingScheme Class](99de5fb2-6e65-7b1f-1866-347c40d427af.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)