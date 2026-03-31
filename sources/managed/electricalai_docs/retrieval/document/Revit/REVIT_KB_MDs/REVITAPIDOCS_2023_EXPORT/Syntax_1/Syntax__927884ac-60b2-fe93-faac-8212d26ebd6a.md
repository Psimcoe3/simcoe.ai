[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilterViewId Property

---



|  |
| --- |
| [IFCExportOptions Class](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.htm)   [See Also](#seeAlsoToggle) |

Id of the view whose visibility settings will govern the contents in the exported IFC file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId FilterViewId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FilterViewId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ FilterViewId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

#### Field Value

This should be set to the id of the view, or InvalidElementId if there is to be no special filtering applied (all model elements will be exported). Default is InvalidElementId.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[IFCExportOptions Class](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)