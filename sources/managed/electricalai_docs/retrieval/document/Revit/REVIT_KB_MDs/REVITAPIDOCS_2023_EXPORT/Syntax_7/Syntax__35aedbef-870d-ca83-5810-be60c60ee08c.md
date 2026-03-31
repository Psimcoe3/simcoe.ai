[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EffectInstance Constructor

---



|  |
| --- |
| [EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.htm)   [See Also](#seeAlsoToggle) |

Constructs the effect instance for geometry having the specified vertex format.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public EffectInstance( 	VertexFormatBits vertexFormatBits ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	vertexFormatBits As VertexFormatBits _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: EffectInstance( 	VertexFormatBits vertexFormatBits ) ``` |

#### Parameters

vertexFormatBits
:   Type:  [Autodesk.Revit.DB.DirectContext3D VertexFormatBits](e993d256-56d3-4103-3451-bb42bc90a7d8.htm)    
     The vertex format of the geometry to be used with this effect instance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This EffectInstance is not available because Revit is not currently rendering. In general, this EffectInstance must be used in the scope of the RenderScene() callback of IDirectContext3DServer. |

# See Also

[EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)