[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSingleFabricSheetWithinHost Method

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

Identifies if the specified single Fabric Sheet position is within the host.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsSingleFabricSheetWithinHost( 	Element hostElement, 	Transform transform ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsSingleFabricSheetWithinHost ( _ 	hostElement As Element, _ 	transform As Transform _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsSingleFabricSheetWithinHost( 	Element^ hostElement,  	Transform^ transform ) ``` |

#### Parameters

hostElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     A structural element that will host the Fabric Sheet.

transform
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The transform that defines the placement of the instance single Fabric Sheet.

#### Return Value

True if the single Fabric Sheet instance is within the host, false if the single Fabric Sheet instance is out of host.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)