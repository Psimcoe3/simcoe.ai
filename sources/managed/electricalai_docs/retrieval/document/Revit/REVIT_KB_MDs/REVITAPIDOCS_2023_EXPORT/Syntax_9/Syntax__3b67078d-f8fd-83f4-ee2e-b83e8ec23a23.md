[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Build Method

---



|  |
| --- |
| [TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)   [See Also](#seeAlsoToggle) |

Builds the designated geometrical objects from the stored face sets. Stores the result in this TessellatedShapeBuilder object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void Build() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Build ``` |

 

| Visual C++ |
| --- |
| ``` public: void Build() ``` |

# Remarks

The behavior of this function is affected by Target, Fallback and GStyleId properties of this TessellatedShapeBuilder object. Currently only "Solid/Abort", "AnyGeometry/Mesh" and "Mesh/Salvage" target/fallback combinations are supported. Note that this function does not erase the face sets stored in the builder. If the same builder is used to construct geometrical objects for different collections of face sets, (  [Clear](8c2cd942-f8c3-3288-bac6-8d4d1f064714.htm)  ) should be called while switching from one collection to another.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Throws if data in the stored face sets are so inconsistent, that they cannot be used in their entirety, or if an attempt is made to create unacceptable geometry with too many facets. |

# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)