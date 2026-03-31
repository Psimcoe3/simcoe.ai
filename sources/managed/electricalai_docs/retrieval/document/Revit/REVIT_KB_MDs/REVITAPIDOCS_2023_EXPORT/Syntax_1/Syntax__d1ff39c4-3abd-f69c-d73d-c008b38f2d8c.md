[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Multiply Operator

---



|  |
| --- |
| [Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   [See Also](#seeAlsoToggle) |

Multiplies the two specified transforms.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static Transform operator *( 	Transform left, 	Transform right ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Operator * ( _ 	left As Transform, _ 	right As Transform _ ) As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: static Transform^ operator *( 	Transform^ left,  	Transform^ right ) ``` |

#### Parameters

left
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The first transformation.

right
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The second transformation.

#### Return Value

The transformation equal to the composition of the two transformations.

# Remarks

The combined transformation has the same effect as applying the right transformation first, and the left transformation, second. So, (T1(T2(p)) = (T1 \* T2) (p).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the handle of the first or second transformation is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)