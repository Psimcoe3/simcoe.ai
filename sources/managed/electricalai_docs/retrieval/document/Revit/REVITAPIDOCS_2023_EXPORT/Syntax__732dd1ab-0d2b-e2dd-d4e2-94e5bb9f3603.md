[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SymbolGeometry Property

---



|  |
| --- |
| [GeometryInstance Class](fe25b14f-5866-ca0f-a660-c157484c3a56.htm)   [See Also](#seeAlsoToggle) |

The geometric representation of the symbol which generates this instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public GeometryElement SymbolGeometry { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SymbolGeometry As GeometryElement 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property GeometryElement^ SymbolGeometry { 	GeometryElement^ get (); } ``` |

# Remarks

The geometry will be in the local coordinate space of the symbol. The context of this instance object (such as effective material) will be applied to the symbol. Note that retrieving the value of this property involves extensive parsing or Revit's data structures, so try to minimize calls if performance is critical. Geometry will be parsed with the same options as those used when this object was retrieved. The value of this property and the results of the method GetSymbolGeometry(void) are identical.

# See Also

[GeometryInstance Class](fe25b14f-5866-ca0f-a660-c157484c3a56.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)