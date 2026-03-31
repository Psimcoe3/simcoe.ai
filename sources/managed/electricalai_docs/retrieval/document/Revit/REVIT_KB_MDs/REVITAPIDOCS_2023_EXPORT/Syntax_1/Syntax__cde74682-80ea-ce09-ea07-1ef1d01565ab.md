[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transparency Property

---



|  |
| --- |
| [ViewDisplayModel Class](9864e320-a160-dd24-23f6-a30c482a8e5f.htm)   [See Also](#seeAlsoToggle) |

The percentage (0..100) of surface transparency 0 means the surfaces are opaque, 100 means they are fully transparent

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public int Transparency { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Transparency As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Transparency { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The value is invalid. The valid range is 0 through 100 |

# See Also

[ViewDisplayModel Class](9864e320-a160-dd24-23f6-a30c482a8e5f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)