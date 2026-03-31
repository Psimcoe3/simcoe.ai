[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreTargetAndFallbackCompatible Method

---



|  |
| --- |
| [TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)   [See Also](#seeAlsoToggle) |

Checks whether this combination of fallback and target parameters can be used as a valid combination of inputs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool AreTargetAndFallbackCompatible( 	TessellatedShapeBuilderTarget target, 	TessellatedShapeBuilderFallback fallback ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AreTargetAndFallbackCompatible ( _ 	target As TessellatedShapeBuilderTarget, _ 	fallback As TessellatedShapeBuilderFallback _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AreTargetAndFallbackCompatible( 	TessellatedShapeBuilderTarget target,  	TessellatedShapeBuilderFallback fallback ) ``` |

#### Parameters

target
:   Type:  [Autodesk.Revit.DB TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.htm)    
     What kind of geometrical objects should be built.

fallback
:   Type:  [Autodesk.Revit.DB TessellatedShapeBuilderFallback](ce755fa3-8727-2cd3-dbc3-c952bdc83a17.htm)    
     What should be done if a geometrical object described by 'target' parameter cannot be built using all data from all stored face sets.

#### Return Value

True if the combination of fallback and target are a valid combination, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)