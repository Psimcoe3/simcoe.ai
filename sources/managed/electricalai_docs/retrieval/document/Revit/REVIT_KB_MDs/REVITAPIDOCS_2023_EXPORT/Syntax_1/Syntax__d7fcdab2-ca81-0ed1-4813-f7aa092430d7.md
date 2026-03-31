[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Segments Property

---



|  |
| --- |
| [Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)   [See Also](#seeAlsoToggle) |

The segments in the dimension.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public DimensionSegmentArray Segments { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Segments As DimensionSegmentArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property DimensionSegmentArray^ Segments { 	DimensionSegmentArray^ get (); } ``` |

# Remarks

Returns a read only array of segments in the dimension. The references of the dimension can be mapped to segments in order. The first segment here wrapped by first and second references; the nth segment is wrapped by nth and n+1st references.

# See Also

[Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)