[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MinExternalAngleBetweenTriangles Property

---



|  |
| --- |
| [SolidOrShellTessellationControls Class](ab0dd37a-7ed8-4874-2861-0f9a41da0235.htm)   [See Also](#seeAlsoToggle) |

A positive real number specifying the minimum allowed value for the external angle between two adjacent triangles, in radians.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double MinExternalAngleBetweenTriangles { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MinExternalAngleBetweenTriangles As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MinExternalAngleBetweenTriangles { 	double get (); 	void set (double value); } ``` |

# Remarks

A small value yields more smoothly curved triangulated surfaces, usually at the expense of an increase in the number of triangles. Note that this setting has no effect for planar surfaces. This constraint may be approximately enforced.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for minExternalAngleBetweenTriangles must be greater than 0 and no more than 30000 feet. |

# See Also

[SolidOrShellTessellationControls Class](ab0dd37a-7ed8-4874-2861-0f9a41da0235.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)