[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Name Property

---



|  |
| --- |
| [LightGroup Class](fd876292-9f3a-7a90-dd41-019631baadca.htm)   [See Also](#seeAlsoToggle) |

The name of the LightGroup

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public string Name { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Name As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Name { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- When setting this property: The name is not valid because it is not unique within this LightGroupManager |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[LightGroup Class](fd876292-9f3a-7a90-dd41-019631baadca.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)