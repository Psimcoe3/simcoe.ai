[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Duplicate Method

---



|  |
| --- |
| [ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)   [See Also](#seeAlsoToggle) |

Generates a copy of current scheme.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public ElementId Duplicate( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Duplicate ( _ 	name As String _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ Duplicate( 	String^ name ) ``` |

#### Parameters

name
:   Type:  System String    
     The desired name of copied scheme.

#### Return Value

The id of copied scheme.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The name is not valid for new generated scheme. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)