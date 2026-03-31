[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOriginalGeometry Method

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

Returns the original geometry of the instance, before the instance is modified by joins, cuts, coping, extensions, or other post-processing.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public GeometryElement GetOriginalGeometry( 	Options options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOriginalGeometry ( _ 	options As Options _ ) As GeometryElement ``` |

 

| Visual C++ |
| --- |
| ``` public: GeometryElement^ GetOriginalGeometry( 	Options^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB Options](aa41fc13-9f81-836c-4271-82568ba5d7e8.htm)    
     The options used to obtain the geometry. Note that ComputeReferences may not be set to true.

# Remarks

This method returns the original geometry of the instance. The instance's geometry will reflect the values of all instance level parameters (e.g. reference levels for columns) and of the placement conditions (so a beam placed along a 20' long line will be 20' long). It excludes all modifications made to the geometry due to operations like joining, cutting, openings, coping, or extensions.

The geometry will not include the GeometryInstance typically returned when you access the geometry of a FamilyInstance via Element.Geometry. But GeometryInstances may be encountered if there are nested family instances within the family.

The geometry is returned in the coordinates of the FamilySymbol, not the coordinates of the instance. If needed, you can transform the returned GeometryElement using the GetTransformed() method, passing the results from GetTransform(), or some other user-defined transformation.

The geometry returned is from Revit's internal computations and does not represent actual Revit geometry. Thus, you cannot use it as a reference for other geometry.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the options are not valid for this operation (ComputeReferences == true) |

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)