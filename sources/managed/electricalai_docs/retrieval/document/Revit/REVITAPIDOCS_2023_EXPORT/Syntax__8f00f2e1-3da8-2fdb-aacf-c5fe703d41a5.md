[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewSymbolicCurve Method

---



|  |
| --- |
| [FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)   [See Also](#seeAlsoToggle) |

Create a symbolic curve in an Autodesk Revit family document.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SymbolicCurve NewSymbolicCurve( 	Curve curve, 	SketchPlane sketchPlane ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewSymbolicCurve ( _ 	curve As Curve, _ 	sketchPlane As SketchPlane _ ) As SymbolicCurve ``` |

 

| Visual C++ |
| --- |
| ``` public: SymbolicCurve^ NewSymbolicCurve( 	Curve^ curve,  	SketchPlane^ sketchPlane ) ``` |

#### Parameters

curve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The geometry curve of the newly created symbolic curve.

sketchPlane
:   Type:  [Autodesk.Revit.DB SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.htm)    
     The sketch plane for the symbolic curve.

#### Return Value

The newly created symbolic curve.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when argument is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when regeneration failed. Thrown when symbolic curve creation failed. |

# See Also

[FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)