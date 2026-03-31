[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundingElementFace Method

---



|  |
| --- |
| [SpatialElementBoundarySubface Class](0a8f3677-3320-a8a5-674e-b0d055ac6671.htm)   [See Also](#seeAlsoToggle) |

Returns the face of the bounding element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Face GetBoundingElementFace() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoundingElementFace As Face ``` |

 

| Visual C++ |
| --- |
| ``` public: Face^ GetBoundingElementFace() ``` |

#### Return Value

The face of the bounding element.

# Remarks

Applies only if the options chosen for the extraction of the element's geometry is Finish. Faces do not contain voids in room-bounding elements (such the voids in walls created by doors and windows).

# See Also

[SpatialElementBoundarySubface Class](0a8f3677-3320-a8a5-674e-b0d055ac6671.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)