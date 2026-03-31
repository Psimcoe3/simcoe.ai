[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarVaryingLengthNumberSuffix Property

---



|  |
| --- |
| [ReinforcementSettings Class](ca904bb8-c5f4-26bb-6220-9f8d5d1ebd1f.htm)   [See Also](#seeAlsoToggle) |

A unique identifier used for a bar within a variable length rebar set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public string RebarVaryingLengthNumberSuffix { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RebarVaryingLengthNumberSuffix As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ RebarVaryingLengthNumberSuffix { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

This property affects only Rebar sets under the following conditions:

* 1. The distribution type (  [!:Autodesk::Revit::DB::Rebar::distributionType]  ) of the Rebar is DistributionType::Enum::VaryingLength.
* 2. There are at least two bars within the Rebar set that have different shape parameter values (i.e at least two bars vary in length).

*The shape parameters of a Rebar can be accessed via  [!:Autodesk::Revit::DB::Structure::RebarShapeDefinition::getParameters]  method.*

*The parameters at a specific index in a Rebar set can be accessed via  [!:Autodesk::Revit::DB::Structure::Rebar::getParameterValueAtIndex]  method.*

This property is assigned to varying Rebar sets only if they are numbered as a whole (i.e.  [NumberVaryingLengthRebarsIndividually](7b74062d-8c65-4145-1d8c-23302ebc5b61.htm)  is set to false).

The values for this property are valid if :

* Input contains at least one character.
* Input contains either alphabetical or numeric characters (not both).

When this property is used, each bar in a varying set will be assigned an incremented value of the suffix. As an example, the suffix values for three bars in a varying set are:

* For alphabetic suffix : Aaz -> Aba -> Abb.
* For numeric suffix : 129 -> 130 -> 131.

These values are automatically incremented by the system.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The rebar number suffix is not valid if :  * Input is empty. * Input contains non-alphanumeric characters. * Input contains both numeric and alphabetic characters. * Input is a value that exceeds the maximum integer representation. * Input contains more than 6 alphabetic characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[ReinforcementSettings Class](ca904bb8-c5f4-26bb-6220-9f8d5d1ebd1f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)