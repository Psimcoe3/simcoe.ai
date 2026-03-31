[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewOrganizationId Property

---



|  |
| --- |
| [InSessionViewSheetSet Class](61a44d58-c862-5fb6-6a06-dd3d3abac585.htm)   [See Also](#seeAlsoToggle) |

[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)  to the  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  for non-sheet views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual ElementId ViewOrganizationId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property ViewOrganizationId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property ElementId^ ViewOrganizationId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

#### Implements

 [IViewSheetSet ViewOrganizationId](cab190d0-c36b-4bdb-1259-93241c94fd58.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the  [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)  does not reference to  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  , or the target type of  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  is incompatible. |

# See Also

[InSessionViewSheetSet Class](61a44d58-c862-5fb6-6a06-dd3d3abac585.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)