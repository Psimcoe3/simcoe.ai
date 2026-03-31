[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Offset Property

---



|  |
| --- |
| [AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)   [See Also](#seeAlsoToggle) |

The offset of the labels from the alignment, in Revit internal paper space units (standard Imperial feet). A positive offset creates labels to the right of the alignment, a negative - to the left. The default value is null. If null, a predefined offset value will be used, depending on the unit setting for stationing units in the document. For standard imperial, the default is 1/8". For survey imperial, the default is 1/8" (US survey). For metric, the default is 5 mm.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public Nullable<double> Offset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Offset As Nullable(Of Double) 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Nullable<double> Offset { 	Nullable<double> get (); 	void set (Nullable<double> value); } ``` |

# See Also

[AlignmentStationLabelSetOptions Class](15f4337d-738d-ec32-e7bc-4f2c569f4c59.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)