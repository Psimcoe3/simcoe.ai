[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BottomLevelId Property

---



|  |
| --- |
| [AreaBasedLoadBoundaryLineData Class](52959c6a-9d31-222c-3133-e373047095a9.htm)   [See Also](#seeAlsoToggle) |

The bottom level id of the area based load boundary line.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ElementId BottomLevelId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BottomLevelId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ BottomLevelId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

The bottom level's elevation cannot be higher than the top level.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The ElementId levelId cannot be used as the bottom level. The ElementId levelId is not a Level or it's elevation is higher than the top level's elevation. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[AreaBasedLoadBoundaryLineData Class](52959c6a-9d31-222c-3133-e373047095a9.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)