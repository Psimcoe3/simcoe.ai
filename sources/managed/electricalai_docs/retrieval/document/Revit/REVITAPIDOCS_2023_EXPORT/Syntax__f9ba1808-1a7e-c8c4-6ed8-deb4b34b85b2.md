[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddReferencePoint Method (XYZ)

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Adds a reference point to the DirectShapeType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void AddReferencePoint( 	XYZ refPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddReferencePoint ( _ 	refPoint As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddReferencePoint( 	XYZ^ refPoint ) ``` |

#### Parameters

refPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The coordinates of the new reference point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input point lies outside of Revit design limits. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[AddReferencePoint Overload](55c149cf-7aa1-dae9-5a78-22531a85366a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)