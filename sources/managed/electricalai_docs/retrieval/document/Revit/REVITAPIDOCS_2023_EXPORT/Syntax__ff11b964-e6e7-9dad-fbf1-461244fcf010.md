[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidType Method

---



|  |
| --- |
| [AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)   [See Also](#seeAlsoToggle) |

Checks if the type is a valid alignment station label type.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public static bool IsValidType( 	Element type ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidType ( _ 	type As Element _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidType( 	Element^ type ) ``` |

#### Parameters

type
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element type to validate.

# Remarks

Can be used for finding or types to be set to  [TypeId](86352cb2-b367-a806-7427-2fb08e50b425.htm)  when creating alignment label sets with  [Create(Alignment, View, AlignmentStationLabelOptions)](eb69d2d4-5a55-6402-ae7b-d1049fdba2d4.htm)  ; or types to be set to  [TypeId](5b0dfa5d-bc2f-b097-a8d6-c5e78c569add.htm)  when creating alignment labels with  [CreateSet(Alignment, View, AlignmentStationLabelSetOptions)](bbb3fb20-cbc6-f6aa-cc23-ae7ad73747b3.htm)  .

# See Also

[AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)