[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FixedNumberOfPoints Property

---



|  |
| --- |
| [DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)   [See Also](#seeAlsoToggle) |

The number of points used when the layout is set to 'FixedNumber'.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public int FixedNumberOfPoints { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FixedNumberOfPoints As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int FixedNumberOfPoints { 	int get (); 	void set (int value); } ``` |

# Remarks

To get the actual number of point use GetNumberOfPoints().

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: fixedNumberOfPoints must be at least 2 and at most 200. |

# See Also

[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)