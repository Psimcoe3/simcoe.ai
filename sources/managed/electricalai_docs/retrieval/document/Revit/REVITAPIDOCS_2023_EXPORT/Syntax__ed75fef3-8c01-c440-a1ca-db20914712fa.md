[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)   [See Also](#seeAlsoToggle) |

Checks if the RebarContainer has this item as one of its members.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool Contains( 	RebarContainerItem pItem ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Contains ( _ 	pItem As RebarContainerItem _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Contains( 	RebarContainerItem^ pItem ) ``` |

#### Parameters

pItem
:   Type:  [Autodesk.Revit.DB.Structure RebarContainerItem](764f647c-9c3e-b971-1c44-b63f756e1448.htm)    
     The item to be checked if RebarContainer has it as one of its members

#### Return Value

True if RebarContainer has this item as one of its members, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)