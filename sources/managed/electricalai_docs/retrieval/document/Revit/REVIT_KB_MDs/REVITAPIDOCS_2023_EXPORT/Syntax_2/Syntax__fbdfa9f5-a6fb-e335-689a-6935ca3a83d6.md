[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Distance Property

---



|  |
| --- |
| [WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)   [See Also](#seeAlsoToggle) |

Represents the distance from either the top or base of the wall for horizontal sweeps, or the parameter along the wall's path curve for vertical ones.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double Distance { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Distance As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Distance { 	double get (); 	void set (double value); } ``` |

#### Field Value

DistanceMeasuredFrom determines where the measurement starts from, depending on the orientation of the sweep. If the sweep or reveal is vertical, this distance is equal to the parameter along the wall's path curve.

# See Also

[WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)