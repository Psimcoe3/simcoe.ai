[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DistributionType Property

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

The type of rebar distribution(also known as Rebar Set Type).

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public DistributionType DistributionType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DistributionType As DistributionType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property DistributionType DistributionType { 	DistributionType get (); 	void set (DistributionType value); } ``` |

# Remarks

The possible values of this property are:

* Uniform
* VaryingLength

For a uniform distribution type: all bars parameters are the same as the first bar in set. For a varying length distribution type: bars parameters can vary(primarly in length) taking in consideration the constraints of the first bar in set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)