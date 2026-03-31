[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CopyFrom Method

---



|  |
| --- |
| [PanelScheduleTemplate Class](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)   [See Also](#seeAlsoToggle) |

Copies all values from other element to this object.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void CopyFrom( 	Document OtherADoc, 	PanelScheduleTemplate otherElem ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub CopyFrom ( _ 	OtherADoc As Document, _ 	otherElem As PanelScheduleTemplate _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void CopyFrom( 	Document^ OtherADoc,  	PanelScheduleTemplate^ otherElem ) ``` |

#### Parameters

OtherADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document for the otherElem

otherElem
:   Type:  [Autodesk.Revit.DB.Electrical PanelScheduleTemplate](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)    
     The element being copied from.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given template otherElem has different type of this element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PanelScheduleTemplate Class](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)