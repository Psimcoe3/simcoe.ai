[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TreadProfile Property

---



|  |
| --- |
| [StairsRunType Class](a76503c0-abd8-0043-883b-134149348542.htm)   [See Also](#seeAlsoToggle) |

The id of the profile of the treads.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId TreadProfile { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TreadProfile As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ TreadProfile { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The profile is neither a valid element id nor invalidElementId. -or- When setting this property: The profile is not a valid tread profile symbol. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The run type has no tread so the data being set is not applicable. |

# See Also

[StairsRunType Class](a76503c0-abd8-0043-883b-134149348542.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)