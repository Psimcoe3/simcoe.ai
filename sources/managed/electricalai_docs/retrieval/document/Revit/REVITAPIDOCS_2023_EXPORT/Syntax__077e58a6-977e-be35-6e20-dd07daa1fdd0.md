[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetTypeId Method

---



|  |
| --- |
| [DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)   [See Also](#seeAlsoToggle) |

Sets the DirectShapeType for the DirectShape element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void SetTypeId( 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetTypeId ( _ 	typeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetTypeId( 	ElementId^ typeId ) ``` |

#### Parameters

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the type corresponding to this DirectShape element. May only be set once.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | typeId is not a valid Element identifier. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)