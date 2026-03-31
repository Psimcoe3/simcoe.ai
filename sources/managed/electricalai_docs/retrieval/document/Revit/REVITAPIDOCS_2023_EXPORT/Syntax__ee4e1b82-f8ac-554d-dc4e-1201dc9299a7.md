[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SupportLayout Property

---



|  |
| --- |
| [HandRailType Class](8db101a3-6229-8b94-4687-9cbaec787ef2.htm)   [See Also](#seeAlsoToggle) |

The support layout method of the handrail.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public RailSupportsLayout SupportLayout { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SupportLayout As RailSupportsLayout 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property RailSupportsLayout SupportLayout { 	RailSupportsLayout get (); 	void set (RailSupportsLayout value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The rail has no support specified so the data being set is not applicable. |

# See Also

[HandRailType Class](8db101a3-6229-8b94-4687-9cbaec787ef2.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)