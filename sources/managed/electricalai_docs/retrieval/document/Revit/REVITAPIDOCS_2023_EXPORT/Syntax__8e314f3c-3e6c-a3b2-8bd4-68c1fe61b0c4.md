[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddParameter Method

---



|  |
| --- |
| [RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)   [See Also](#seeAlsoToggle) |

Add a parameter to the shape definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public void AddParameter( 	ElementId paramId, 	double defaultValue ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddParameter ( _ 	paramId As ElementId, _ 	defaultValue As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddParameter( 	ElementId^ paramId,  	double defaultValue ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The parameter. To obtain the id of a shared parameter, call RebarShapeParameters.GetElementIdForExternalDefinition.

defaultValue
:   Type:  System Double    
     A default value for this parameter in shapes. The default values should be chosen carefully, because they are required to be consistent as a set of constraints.

# Remarks

A shape parameter must be a shared parameter and have value type double. A parameter must be added to the definition before it can be used to drive the shape in a RebarShapeConstraint object. A parameter that does not drive a constraint is legal and will simply become an editable parameter on any Rebar that is an instance of this RebarShape.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a shared parameter in the current document, or its unit type is not UT\_Reinforcement\_Length or UT\_Angle. -or- The name of a shared parameter identified by paramId was already used by another shared parameter of the element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)