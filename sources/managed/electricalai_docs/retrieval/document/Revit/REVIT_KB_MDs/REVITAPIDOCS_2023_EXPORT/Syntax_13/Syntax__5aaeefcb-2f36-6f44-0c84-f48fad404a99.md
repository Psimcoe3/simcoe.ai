[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewShapeBuilder Constructor (DirectShapeTargetViewType)

---



|  |
| --- |
| [ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)   [See Also](#seeAlsoToggle) |

A constructor for an ViewShapeBuilder object that takes a view type. It will infer the view normal from view type. View normal and view type are used to validate the geometry to be stored as a view-specific shape representation of a DirectShape object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public ViewShapeBuilder( 	DirectShapeTargetViewType targetViewType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	targetViewType As DirectShapeTargetViewType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ViewShapeBuilder( 	DirectShapeTargetViewType targetViewType ) ``` |

#### Parameters

targetViewType
:   Type:  [Autodesk.Revit.DB DirectShapeTargetViewType](1c5cd94e-3804-54da-73af-505655b0948f.htm)    
     View type for which this shape representation is intended. Currently limited to Plan Views.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | targetViewType is not DirectShapeTargetViewType::Plan |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)

[ViewShapeBuilder Overload](ca873c2a-8ad3-328f-9da4-010428bcb160.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)