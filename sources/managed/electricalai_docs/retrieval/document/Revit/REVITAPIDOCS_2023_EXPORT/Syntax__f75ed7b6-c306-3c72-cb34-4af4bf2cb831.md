[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Division Operator

---



|  |
| --- |
| [UV Class](1724be37-059b-91ff-aa74-d1508082f76d.htm)   [See Also](#seeAlsoToggle) |

Divides the specified 2-D vector by the specified value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static UV operator /( 	UV left, 	double value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Operator / ( _ 	left As UV, _ 	value As Double _ ) As UV ``` |

 

| Visual C++ |
| --- |
| ``` public: static UV^ operator /( 	UV^ left,  	double value ) ``` |

#### Parameters

left
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The value to divide the vector by.

value
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The vector to divide by the value.

#### Return Value

The divided 2-D vector.

# Remarks

The divided vector is obtained by dividing each coordinate of the specified vector by the specified value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the specified value is an infinite number or zero. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when left is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[UV Class](1724be37-059b-91ff-aa74-d1508082f76d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)