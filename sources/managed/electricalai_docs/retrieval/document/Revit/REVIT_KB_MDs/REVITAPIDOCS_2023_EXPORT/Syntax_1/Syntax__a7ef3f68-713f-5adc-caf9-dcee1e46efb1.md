[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetOptions Method

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Sets the options to use for this DirectShapeType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public void SetOptions( 	DirectShapeTypeOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetOptions ( _ 	options As DirectShapeTypeOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetOptions( 	DirectShapeTypeOptions^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB DirectShapeTypeOptions](ce6d1f15-bceb-5ad2-f3d1-d93f0447da44.htm)    
     Options to use for this DirectShapeType.

# Remarks

The new options take effect immediately.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The DirectShapeTypeOptions provided are not valid for this DirectShapeType. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)