[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VertexTolerance Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Vertex tolerance.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double VertexTolerance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VertexTolerance As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double VertexTolerance { 	double get (); } ``` |

# Remarks

Two points within this distance are considered coincident. Do not use this value for any purpose other than its intended purpose, which is to check if two points are the same within this tolerance value. Do not use this value to set the distance between two points. Doing so will result in unstable behavior.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)