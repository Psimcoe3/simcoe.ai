[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanCreateParts Method

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Indicates if it is possible to create parts from this DirectShapeType element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool CanCreateParts() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanCreateParts As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanCreateParts() ``` |

#### Return Value

True if it is possible to create parts from this DirectShapeType.

# Remarks

While it is generally possible to create parts from DirectShape elements, some characteristics make parts creation impossible. This property is re-evaluated every time the DirectShapeType's geometry is modified (via a call to SetShape or AppendShape). Invalid configurations include: DirectShapeTypes containing a polymesh, or an open geometry, as well as DirectShapeTypes not containing any solids and DirectShapeTypes configured as NotReferenceable (via a call to SetOptions). Finally, if a DirectShapeType has other DirectShapeType instances in its geometry, and one of those other DirectShapeTypes has a configuration that is incompatible with parts creation, the host DirectShapeType will also be incompatible with parts creation.

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)