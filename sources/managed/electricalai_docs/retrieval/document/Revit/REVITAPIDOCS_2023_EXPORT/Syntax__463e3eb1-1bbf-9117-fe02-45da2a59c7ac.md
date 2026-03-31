[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Id Property

---



|  |
| --- |
| [WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)   [See Also](#seeAlsoToggle) |

The id of the sweep or reveal.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public int Id { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Id As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Id { 	int get (); 	void set (int value); } ``` |

#### Field Value

If the wall sweep belongs to a vertically compound structure, this must be a non-negative value. If the wall sweep belongs to a sweep defined outside of compound structures by UI or API the id will typically be -1 and is not used.

# See Also

[WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)