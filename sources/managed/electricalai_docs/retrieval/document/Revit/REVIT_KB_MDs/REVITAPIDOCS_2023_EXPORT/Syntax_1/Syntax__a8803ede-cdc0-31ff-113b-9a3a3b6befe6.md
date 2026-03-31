[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSurfaceTransparency Method

---



|  |
| --- |
| [OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)   [See Also](#seeAlsoToggle) |

Sets the projection surface transparency.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public OverrideGraphicSettings SetSurfaceTransparency( 	int transparency ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetSurfaceTransparency ( _ 	transparency As Integer _ ) As OverrideGraphicSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: OverrideGraphicSettings^ SetSurfaceTransparency( 	int transparency ) ``` |

#### Parameters

transparency
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Value of the transparency of the projection surface (0 = opaque, 100 = fully transparent).

#### Return Value

Reference to the changed object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Transparency must be greater than 0 and less than 100. |

# See Also

[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)