[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionGeneralLA Constructor

---



|  |
| --- |
| [StructuralSectionGeneralLA Class](ac8289f3-7267-03b2-450a-df1a50ccc844.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of Angle Cold Formed shape.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public StructuralSectionGeneralLA( 	double width, 	double height, 	double wallNominalThickness, 	double wallDesignThickness, 	double innerFillet, 	double lipLength, 	double centroidHorizontal, 	double centroidVertical, 	StructuralSectionAnalysisParams analysisParams ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	height As Double, _ 	wallNominalThickness As Double, _ 	wallDesignThickness As Double, _ 	innerFillet As Double, _ 	lipLength As Double, _ 	centroidHorizontal As Double, _ 	centroidVertical As Double, _ 	analysisParams As StructuralSectionAnalysisParams _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionGeneralLA( 	double width,  	double height,  	double wallNominalThickness,  	double wallDesignThickness,  	double innerFillet,  	double lipLength,  	double centroidHorizontal,  	double centroidVertical,  	StructuralSectionAnalysisParams^ analysisParams ) ``` |

#### Parameters

width
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section width.

height
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section height, depth.

wallNominalThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Represents wall nominal thickness of rectangle.

wallDesignThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Represents wall design thickness of rectangle.

innerFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Inner Fillet - Corner fillet inner radius.

lipLength
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Lip segment length.

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

[StructuralSectionGeneralLA Class](ac8289f3-7267-03b2-450a-df1a50ccc844.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)