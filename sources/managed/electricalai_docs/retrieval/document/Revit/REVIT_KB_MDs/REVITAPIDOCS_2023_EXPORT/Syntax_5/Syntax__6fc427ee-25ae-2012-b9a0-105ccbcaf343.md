[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateLessOrEqualRule Method (ElementId, Double, Double)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether double-precision values from the document are less than or equal to a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateLessOrEqualRule( 	ElementId parameter, 	double value, 	double epsilon ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateLessOrEqualRule ( _ 	parameter As ElementId, _ 	value As Double, _ 	epsilon As Double _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateLessOrEqualRule( 	ElementId^ parameter,  	double value,  	double epsilon ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A double-typed parameter used to get values from the document for a given element.

value
:   Type:  System Double    
     The user-supplied value against which values from the document will be compared.

epsilon
:   Type:  System Double    
     Defines the tolerance within which two values may be considered equal.

# Remarks

Values greater than the user-supplied value but within  *epsilon*  are considered equal; therefore, such values satisfy the condition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for value is not finite -or- The given value for value is not a number -or- The given value for epsilon is not finite -or- The given value for epsilon is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateLessOrEqualRule Overload](5b6d084a-a18a-467a-6f4a-10790e1a71fe.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)