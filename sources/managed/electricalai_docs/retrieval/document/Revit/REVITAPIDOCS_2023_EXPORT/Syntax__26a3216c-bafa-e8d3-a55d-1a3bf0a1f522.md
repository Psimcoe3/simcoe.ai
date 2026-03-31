[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BeginsWithRiser Property

---



|  |
| --- |
| [StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)   [See Also](#seeAlsoToggle) |

True if the stairs run begins with a riser, false otherwise.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool BeginsWithRiser { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BeginsWithRiser As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool BeginsWithRiser { 	bool get (); 	void set (bool value); } ``` |

# Remarks

If selected, Revit adds a riser to the beginning of the run. If you clear this option, Revit removes the beginning riser and positions the adjacent tread at the base elevation. Clearing this option will change the number of risers in the run. You will need to manually add a riser to maintain the original height.

# See Also

[StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)