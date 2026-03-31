[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateDefaultFabricAreaType Method

---



|  |
| --- |
| [FabricAreaType Class](ac1e177f-5041-418f-c220-962887091d3c.htm)   [See Also](#seeAlsoToggle) |

Creates a new FabricAreaType object with a default name.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static ElementId CreateDefaultFabricAreaType( 	Document aDoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateDefaultFabricAreaType ( _ 	aDoc As Document _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ CreateDefaultFabricAreaType( 	Document^ aDoc ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The newly created type id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricAreaType Class](ac1e177f-5041-418f-c220-962887091d3c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)