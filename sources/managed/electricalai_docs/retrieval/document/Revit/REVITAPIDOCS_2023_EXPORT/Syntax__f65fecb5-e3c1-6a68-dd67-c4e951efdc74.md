[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExcessLengthFillBalusterId Property

---



|  |
| --- |
| [BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.htm)   [See Also](#seeAlsoToggle) |

The id of a Baluster family used to fill excess length, which is the extra space along the railing segment that cannot be filled with a pattern. If set to InvalidElementId, it will be the default - the id of the BaseRailingAttr containing the Baluster pattern.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public ElementId ExcessLengthFillBalusterId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExcessLengthFillBalusterId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ExcessLengthFillBalusterId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: Invalid ElementId for leftoverFill of BalusterPattern |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)