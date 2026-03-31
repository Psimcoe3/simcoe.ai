[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValid Method

---



|  |
| --- |
| [EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.htm)   [See Also](#seeAlsoToggle) |

Tests whether the effect instance is valid for rendering.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool IsValid() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValid As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValid() ``` |

#### Return Value

True if the effect instance is valid for rendering, false otherwise.

# Remarks

The effect instances are internally associated with low-level graphics state and may become invalidated when the state changes. Therefore, an application should test each effect instance for validity before using it when submitting geometry. If the effect instance becomes invalid, the application should re-create it.

# See Also

[EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)