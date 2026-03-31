[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreOptionsValid Method

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Validates that the given DirectShapeTypeOptions are allowed for this particular DirectShapeType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public bool AreOptionsValid( 	DirectShapeTypeOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AreOptionsValid ( _ 	options As DirectShapeTypeOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AreOptionsValid( 	DirectShapeTypeOptions^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB DirectShapeTypeOptions](ce6d1f15-bceb-5ad2-f3d1-d93f0447da44.htm)    
     The options object.

#### Return Value

True if the DirectShapeTypeOptions are valid; false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)