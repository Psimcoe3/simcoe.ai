[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Width Property

---



|  |
| --- |
| [ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)   [See Also](#seeAlsoToggle) |

The width of the ImageInstance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public double Width { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Width As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Width { 	double get (); 	void set (double value); } ``` |

# Remarks

If  [LockProportions](2eda8038-9240-00f5-ffa3-a65d8b4df5f2.htm)  is true, then changes to the  Width  will also result in changes to the  [Height](ba996fed-0624-689f-08a8-1488cdb1292a.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for width results in a height that is more than 30000 feet because LockProportions is set to true. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for width must be between 0 and 30000 feet. |

# See Also

[ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)