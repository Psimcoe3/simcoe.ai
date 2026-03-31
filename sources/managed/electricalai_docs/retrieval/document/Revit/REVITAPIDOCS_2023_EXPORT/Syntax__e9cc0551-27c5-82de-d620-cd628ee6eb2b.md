[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApproximateLength Property

---



|  |
| --- |
| [Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)   [See Also](#seeAlsoToggle) |

Returns the approximate length of the edge.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double ApproximateLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApproximateLength As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ApproximateLength { 	double get (); } ``` |

# Remarks

Estimates the length of the edge by adding together tessellated segments, Will underestimate when the surface is curved.

# See Also

[Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)