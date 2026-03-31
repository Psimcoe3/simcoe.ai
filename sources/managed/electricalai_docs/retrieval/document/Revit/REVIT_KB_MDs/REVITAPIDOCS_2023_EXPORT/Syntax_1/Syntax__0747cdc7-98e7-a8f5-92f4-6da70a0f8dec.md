[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultTemplateId Property

---



|  |
| --- |
| [ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.htm)   [See Also](#seeAlsoToggle) |

The default template id assigned to this view type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId DefaultTemplateId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DefaultTemplateId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ DefaultTemplateId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

This value will be the view template for all newly created instances of this view type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: val is not valid as a default template id. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)