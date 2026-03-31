[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallOffset Property

---



|  |
| --- |
| [WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)   [See Also](#seeAlsoToggle) |

The offset from the sweep or reveal to the wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double WallOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WallOffset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double WallOffset { 	double get (); 	void set (double value); } ``` |

#### Field Value

If the sweep is a solid sweep, a negative value moves it toward the wall core. If the sweep is a reveal, a negative offset value moves it away from the wall.

# See Also

[WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)