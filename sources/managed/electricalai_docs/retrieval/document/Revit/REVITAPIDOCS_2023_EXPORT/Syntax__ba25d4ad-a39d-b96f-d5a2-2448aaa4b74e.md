[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionAnalysisParams Constructor (Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double)

---



|  |
| --- |
| [StructuralSectionAnalysisParams Class](e5bd2059-9102-0c1c-e9d4-16a015a4cb5e.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of StructuralSectionAnalysisParams.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public StructuralSectionAnalysisParams( 	double principalAxesAngle, 	double sectionArea, 	double perimeter, 	double nominalWeight, 	double momentOfInertiaStrongAxis, 	double momentOfInertiaWeakAxis, 	double elasticModulusStrongAxis, 	double elasticModulusWeakAxis, 	double plasticModulusStrongAxis, 	double plasticModulusWeakAxis, 	double torsionalMomentOfInertia, 	double torsionalModulus, 	double warpingConstant, 	double shearAreaStrongAxis, 	double shearAreaWeakAxis ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	principalAxesAngle As Double, _ 	sectionArea As Double, _ 	perimeter As Double, _ 	nominalWeight As Double, _ 	momentOfInertiaStrongAxis As Double, _ 	momentOfInertiaWeakAxis As Double, _ 	elasticModulusStrongAxis As Double, _ 	elasticModulusWeakAxis As Double, _ 	plasticModulusStrongAxis As Double, _ 	plasticModulusWeakAxis As Double, _ 	torsionalMomentOfInertia As Double, _ 	torsionalModulus As Double, _ 	warpingConstant As Double, _ 	shearAreaStrongAxis As Double, _ 	shearAreaWeakAxis As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionAnalysisParams( 	double principalAxesAngle,  	double sectionArea,  	double perimeter,  	double nominalWeight,  	double momentOfInertiaStrongAxis,  	double momentOfInertiaWeakAxis,  	double elasticModulusStrongAxis,  	double elasticModulusWeakAxis,  	double plasticModulusStrongAxis,  	double plasticModulusWeakAxis,  	double torsionalMomentOfInertia,  	double torsionalModulus,  	double warpingConstant,  	double shearAreaStrongAxis,  	double shearAreaWeakAxis ) ``` |

#### Parameters

principalAxesAngle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Rotation angle between the principal axes and cross section reference planes.

sectionArea
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Cross section area.

perimeter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Painting surface of the unit length.

nominalWeight
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Unit weight (not mass) per unit length, for self-weight calculation or quantity survey.

momentOfInertiaStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Moment of Inertia about main strong axis (I).

momentOfInertiaWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Moment of Inertia about main weak axis (I).

elasticModulusStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Elastic section modulus about main strong axis for calculation of bending stresses.

elasticModulusWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Elastic section modulus about main weak axis for calculation of bending stresses.

plasticModulusStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Plastic section modulus in bending about main strong axis (Z, Wpl)

plasticModulusWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Plastic section modulus in bending about main weak axis.

torsionalMomentOfInertia
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Torsional Moment of inertia (J, IT, K), for calculation of torsional deformation

torsionalModulus
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section modulus for calculations of torsion stresses (Ct)

warpingConstant
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Warping constant (Cw, Iomega, H)

shearAreaStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Shear area (reduced extreme shear stress coefficient) in the direction of strong axis (Wq).

shearAreaWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Shear area (reduced extreme shear stress coefficient) in the direction of

# See Also

[StructuralSectionAnalysisParams Class](e5bd2059-9102-0c1c-e9d4-16a015a4cb5e.htm)

[StructuralSectionAnalysisParams Overload](c8199eba-0a13-09c9-cbc8-bb81a7f20ced.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)