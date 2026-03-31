[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundaryFaceInfo Method

---



|  |
| --- |
| [SpatialElementGeometryResults Class](150ca07e-90b0-506f-9b9c-fd39d194a7ea.htm)   [See Also](#seeAlsoToggle) |

Query the spatial element boundary face information with the given face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<SpatialElementBoundarySubface> GetBoundaryFaceInfo( 	Face face ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoundaryFaceInfo ( _ 	face As Face _ ) As IList(Of SpatialElementBoundarySubface) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<SpatialElementBoundarySubface^>^ GetBoundaryFaceInfo( 	Face^ face ) ``` |

#### Parameters

face
:   Type:  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
     The face from the spatial element's geometry.

#### Return Value

Sub-faces related to the room bounding elements that define the spatial element face. Returns    a null reference (  Nothing  in Visual Basic)  if there is no corresponding boundary information with the given face.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpatialElementGeometryResults Class](150ca07e-90b0-506f-9b9c-fd39d194a7ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)