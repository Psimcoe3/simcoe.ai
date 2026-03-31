[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TypeId Property

---



|  |
| --- |
| [AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)   [See Also](#seeAlsoToggle) |

Specifies the ElementId of the labels' type. The default value is InvalidElementId. in this case,  [CreateSet(Alignment, View, AlignmentStationLabelSetOptions)](bbb3fb20-cbc6-f6aa-cc23-ae7ad73747b3.htm)  will throw an exception.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public ElementId TypeId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TypeId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ TypeId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

Recommended types can be found using  [IsRecommendedTypeForSet(Element)](df3f1355-5c15-5665-23e6-520ce91c8815.htm)  Other valid types can be found using  [IsValidType(Element)](ff11b964-e6e7-9dad-fbf1-461244fcf010.htm)  .

# See Also

[AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)