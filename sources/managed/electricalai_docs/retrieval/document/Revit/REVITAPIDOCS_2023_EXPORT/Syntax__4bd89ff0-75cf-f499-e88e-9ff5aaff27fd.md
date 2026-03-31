[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PostScale Method

---



|  |
| --- |
| [Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)   [See Also](#seeAlsoToggle) |

Scales both the linear and translational parts of this transformation and returns the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public Transform2D PostScale( 	double scale ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PostScale ( _ 	scale As Double _ ) As Transform2D ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform2D^ PostScale( 	double scale ) ``` |

#### Parameters

scale
:   Type:  System Double    
     The scale value.

#### Return Value

Returns a pointer to "this"  [Transform2D](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)  .

# Remarks

The resulting transformation is equivalent to the application of this transformation and then the uniform scale, in this order.

# See Also

[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)