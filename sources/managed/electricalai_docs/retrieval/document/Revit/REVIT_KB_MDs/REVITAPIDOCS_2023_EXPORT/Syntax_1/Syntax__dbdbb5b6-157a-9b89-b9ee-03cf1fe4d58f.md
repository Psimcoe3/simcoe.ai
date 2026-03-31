[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasReflection Property

---



|  |
| --- |
| [Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   [See Also](#seeAlsoToggle) |

The boolean value that indicates whether this transformation produces reflection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool HasReflection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HasReflection As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HasReflection { 	bool get (); } ``` |

# Remarks

Reflection transformation changes the handedness of a coordinate system.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when this transformation is not conformal and the reflection is undefined. |

# See Also

[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)