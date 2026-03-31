[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Evaluate Method

---



|  |
| --- |
| [FilterStringRuleEvaluator Class](ba8dad25-3f85-1fbb-a164-323c3750018c.htm)   [See Also](#seeAlsoToggle) |

Derived classes override this method to implement the test that determines whether the two given string values satisfy the desired condition or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool Evaluate( 	string lhs, 	string rhs, 	bool caseSensitive ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Evaluate ( _ 	lhs As String, _ 	rhs As String, _ 	caseSensitive As Boolean _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Evaluate( 	String^ lhs,  	String^ rhs,  	bool caseSensitive ) ``` |

#### Parameters

lhs
:   Type:  System String    
     A value from an element in the document.

rhs
:   Type:  System String    
     The user-supplied value against which values from the document are tested.

caseSensitive
:   Type:  System Boolean    
     If true, string comparisons are done case-sensitively.

#### Return Value

True if the given arguments satisfy the condition, otherwise false.

# Remarks

The arguments may be thought of as the left and right operands of a binary expression; for example, "a < b", "x >= 100", etc. The left operand comes from an element in the Revit document (e.g., the value of a parameter.) The right operand is supplied by the user when creating the filter that contains the rule that uses this evaluator.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilterStringRuleEvaluator Class](ba8dad25-3f85-1fbb-a164-323c3750018c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)