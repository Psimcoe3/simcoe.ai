[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SheetOrganizationId Property

---



|  |
| --- |
| [ViewSheetSet Class](5553be2c-8ce7-cbc1-b99e-85c74bcf28d3.htm)   [See Also](#seeAlsoToggle) |

[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)  to the  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  for sheets.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual ElementId SheetOrganizationId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property SheetOrganizationId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property ElementId^ SheetOrganizationId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

#### Implements

 [IViewSheetSet SheetOrganizationId](69873730-6de8-19d4-eef7-ae05d8990856.htm)

# Remarks

Ignored when  [!:Autodesk::Revit::DB::PrintSetup::IsAutomatic]  is     false  (  False  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the  [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)  does not reference to  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  , or the target type of  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  is incompatible. |

# See Also

[ViewSheetSet Class](5553be2c-8ce7-cbc1-b99e-85c74bcf28d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)