[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Multiply Method

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

Multiplies this vector by the specified value and returns the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Multiply( 	double value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Multiply ( _ 	value As Double _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ Multiply( 	double value ) ``` |

#### Parameters

value
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The value to multiply with this vector.

#### Return Value

The multiplied vector.

# Remarks

The multiplied vector is obtained by multiplying each coordinate of this vector by the specified value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the specified value is an infinite number. |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)