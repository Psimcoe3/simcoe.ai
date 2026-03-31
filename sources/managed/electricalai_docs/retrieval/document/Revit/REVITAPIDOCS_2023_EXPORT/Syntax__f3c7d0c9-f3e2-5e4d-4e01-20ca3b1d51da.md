[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotchThickness Property

---



|  |
| --- |
| [StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)   [See Also](#seeAlsoToggle) |

The vertical length of the notch profile from the top.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double NotchThickness { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property NotchThickness As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double NotchThickness { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for notchThickness must be between 0 and 30000 feet. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The construction method of the stairs type is not "Precast" or the StairsEndConnectionType of the stairs type is not "Notch", so this related data cannot be set. |

# See Also

[StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)