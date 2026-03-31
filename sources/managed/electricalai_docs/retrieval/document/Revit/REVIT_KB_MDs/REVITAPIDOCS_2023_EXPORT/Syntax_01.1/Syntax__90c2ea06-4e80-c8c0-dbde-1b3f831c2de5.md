[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CompoundStructureLayer Constructor (Double, MaterialFunctionAssignment, ElementId)

---



|  |
| --- |
| [CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)   [See Also](#seeAlsoToggle) |

Creates a default compound structure layer based on the given width, function and material element id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public CompoundStructureLayer( 	double width, 	MaterialFunctionAssignment function, 	ElementId materialId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	function As MaterialFunctionAssignment, _ 	materialId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: CompoundStructureLayer( 	double width,  	MaterialFunctionAssignment function,  	ElementId^ materialId ) ``` |

#### Parameters

width
:   Type:  System Double    
     The width of the layer.

function
:   Type:  [Autodesk.Revit.DB MaterialFunctionAssignment](1cbeb006-f7a2-f6d2-491f-faa0b9a006fc.htm)    
     The function of the layer.

materialId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The material element id of the layer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)

[CompoundStructureLayer Overload](d891bb72-066f-caeb-4322-81e30ae45a24.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)