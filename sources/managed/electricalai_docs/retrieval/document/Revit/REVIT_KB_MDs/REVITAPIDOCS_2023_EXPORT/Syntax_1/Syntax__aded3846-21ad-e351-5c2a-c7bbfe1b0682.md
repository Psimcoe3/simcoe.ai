[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveReferences Method

---



|  |
| --- |
| [StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)   [See Also](#seeAlsoToggle) |

Removes references from the connection. All references in an array should belong to the connection.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void RemoveReferences( 	IList<Reference> picks ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveReferences ( _ 	picks As IList(Of Reference) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveReferences( 	IList<Reference^>^ picks ) ``` |

#### Parameters

picks
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The array containing picks to be removed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more picks was not permitted to be removed from the connection. Picks should be members of the connection. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)