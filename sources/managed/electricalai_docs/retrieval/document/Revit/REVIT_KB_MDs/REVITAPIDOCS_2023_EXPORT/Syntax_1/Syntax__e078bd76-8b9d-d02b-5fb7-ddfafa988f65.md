[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAlignmentStationLabels Method (Alignment, ElementId)

---



|  |
| --- |
| [AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)   [See Also](#seeAlsoToggle) |

Returns all alignment station labels placed on the given alignment in the given view.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public static ICollection<AlignmentStationLabel> GetAlignmentStationLabels( 	Alignment alignment, 	ElementId viewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAlignmentStationLabels ( _ 	alignment As Alignment, _ 	viewId As ElementId _ ) As ICollection(Of AlignmentStationLabel) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<AlignmentStationLabel^>^ GetAlignmentStationLabels( 	Alignment^ alignment,  	ElementId^ viewId ) ``` |

#### Parameters

alignment
:   Type:  [Autodesk.Revit.DB.Infrastructure Alignment](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)    
     The alignment for which the labels are returned.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId of the view for which the labels are returned.

# Remarks

The resulting collection may contain both "individual" labels (created via  [Create(Alignment, View, AlignmentStationLabelOptions)](eb69d2d4-5a55-6402-ae7b-d1049fdba2d4.htm)  ) and "labels in set" (created via  [CreateSet(Alignment, View, AlignmentStationLabelSetOptions)](bbb3fb20-cbc6-f6aa-cc23-ae7ad73747b3.htm)  ). These labels have categories respectively  [OST\_Alignments](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)  and  [OST\_AlignmentStationLabelSets](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)  .

# See Also

[AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)

[GetAlignmentStationLabels Overload](df199e7d-c201-c86e-7a7f-cfd1c36e15df.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)