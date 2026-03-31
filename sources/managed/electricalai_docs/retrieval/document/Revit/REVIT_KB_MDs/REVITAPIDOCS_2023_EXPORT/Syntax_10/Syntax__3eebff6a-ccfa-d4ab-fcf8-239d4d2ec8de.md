[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultFloorType Method

---



|  |
| --- |
| [Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)   [See Also](#seeAlsoToggle) |

Returns id of default floor type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static ElementId GetDefaultFloorType( 	Document document, 	bool isFoundation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDefaultFloorType ( _ 	document As Document, _ 	isFoundation As Boolean _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetDefaultFloorType( 	Document^ document,  	bool isFoundation ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

isFoundation
:   Type:  System Boolean    
     True to return id of foundation floor type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)