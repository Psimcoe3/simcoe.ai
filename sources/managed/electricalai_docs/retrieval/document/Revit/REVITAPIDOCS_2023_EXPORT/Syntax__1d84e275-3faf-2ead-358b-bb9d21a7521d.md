[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DiagonalEdgesAreUnderconstrained Property

---



|  |
| --- |
| [BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)   [See Also](#seeAlsoToggle) |

Shape is underconstrained. Please add additional dimension constraints to the shape's diagonal edges. (Diagonal segments with only one dimension constraint are automatically given a second constraint to lie at an angle of exactly 45 degrees, regardless of how they are drawn. The current shape has more than one such segment in sequence, and the resulting constrained edges are co-linear.)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DiagonalEdgesAreUnderconstrained { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DiagonalEdgesAreUnderconstrained As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DiagonalEdgesAreUnderconstrained { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)