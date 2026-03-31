[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnableSnaps Property

---



|  |
| --- |
| [ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)   [See Also](#seeAlsoToggle) |

When true the ImageInstance will have its snaps enabled, but only if  [CanHaveSnaps](ac6a3521-50ad-3573-11b1-d29038730dae.htm)  is true

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool EnableSnaps { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property EnableSnaps As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool EnableSnaps { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The image does not have snaps |

# See Also

[ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)