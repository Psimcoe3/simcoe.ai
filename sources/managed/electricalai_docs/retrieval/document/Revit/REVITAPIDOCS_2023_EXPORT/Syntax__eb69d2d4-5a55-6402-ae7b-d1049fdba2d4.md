[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)   [See Also](#seeAlsoToggle) |

Creates an  [AlignmentStationLabel](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)  object along with its underlying  [SpotDimension](f3c633ac-1595-cb8d-5c1b-66eb3eefb433.htm)  element. Returns null if element creation fails.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public static AlignmentStationLabel Create( 	Alignment alignment, 	View view, 	AlignmentStationLabelOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	alignment As Alignment, _ 	view As View, _ 	options As AlignmentStationLabelOptions _ ) As AlignmentStationLabel ``` |

 

| Visual C++ |
| --- |
| ``` public: static AlignmentStationLabel^ Create( 	Alignment^ alignment,  	View^ view,  	AlignmentStationLabelOptions^ options ) ``` |

#### Parameters

alignment
:   Type:  [Autodesk.Revit.DB.Infrastructure Alignment](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)    
     The alignment on which the alignment station label is placed.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view for which the alignment station label is created.

options
:   Type:  [Autodesk.Revit.DB.Infrastructure AlignmentStationLabelOptions](65682466-07b4-766b-a215-fefcdcfd32ce.htm)    
     The alignment station options of the label to be created.

# See Also

[AlignmentStationLabel Class](5c51c34b-8b34-99fe-d8c6-b6f1ba7caba7.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)