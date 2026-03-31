[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionGeneralW Constructor

---



|  |
| --- |
| [StructuralSectionGeneralW Class](62345498-a884-bfff-d108-ad735416cc11.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of Angle shape.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public StructuralSectionGeneralW( 	double width, 	double height, 	double flangeThickness, 	double webThickness, 	double webFillet, 	double flangeFillet, 	double topWebFillet, 	double centroidHorizontal, 	double centroidVertical, 	StructuralSectionAnalysisParams analysisParams ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	height As Double, _ 	flangeThickness As Double, _ 	webThickness As Double, _ 	webFillet As Double, _ 	flangeFillet As Double, _ 	topWebFillet As Double, _ 	centroidHorizontal As Double, _ 	centroidVertical As Double, _ 	analysisParams As StructuralSectionAnalysisParams _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionGeneralW( 	double width,  	double height,  	double flangeThickness,  	double webThickness,  	double webFillet,  	double flangeFillet,  	double topWebFillet,  	double centroidHorizontal,  	double centroidVertical,  	StructuralSectionAnalysisParams^ analysisParams ) ``` |

#### Parameters

width
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section width.

height
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section height, depth.

flangeThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Flange Thickness.

webThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Thickness.

webFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Fillet - fillet radius between web and flange.

flangeFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Flange Fillet - fillet radius at the flange end.

topWebFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Top Web Fillet - fillet radius at the top of web.

centroidHorizontal
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Distance from centroid to the left extremites along horizontal axis.

centroidVertical
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Distance from centroid to the upper extremites along vertical axis.

analysisParams
:   Type:  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionAnalysisParams](e5bd2059-9102-0c1c-e9d4-16a015a4cb5e.htm)    
     Common set of parameters for structural analysis.

# See Also

[StructuralSectionGeneralW Class](62345498-a884-bfff-d108-ad735416cc11.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)