[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsPathOffset Property

---



|  |
| --- |
| [StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)   [See Also](#seeAlsoToggle) |

The offset of stairs path to center line of stairs.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double StairsPathOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property StairsPathOffset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double StairsPathOffset { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for stairsPathOffset is not finite -or- When setting this property: The stairsPathOffset is larger than half the width of the stairs. |

# See Also

[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)