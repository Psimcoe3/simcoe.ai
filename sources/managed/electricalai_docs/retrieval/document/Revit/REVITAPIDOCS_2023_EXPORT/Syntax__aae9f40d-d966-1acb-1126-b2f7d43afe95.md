[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DownTextOffset Property

---



|  |
| --- |
| [StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)   [See Also](#seeAlsoToggle) |

The offset of stairs down text.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public XYZ DownTextOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DownTextOffset As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ DownTextOffset { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

The z direction makes no sense in API.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The type of this stairs path is not automatic up/down direction. -or- When setting this property: The stairs path doesn't show down text so the data being set is inapplicable. |

# See Also

[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)