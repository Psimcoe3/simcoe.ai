[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AppendItemFromRebar Method

---



|  |
| --- |
| [RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)   [See Also](#seeAlsoToggle) |

Appends an Item to the RebarContainer. Fills its data on base of the Rebar. Will throw exception if given rebar is not shape driven. Will throw exception if given rebar has moved bars in set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public RebarContainerItem AppendItemFromRebar( 	Rebar rebar ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AppendItemFromRebar ( _ 	rebar As Rebar _ ) As RebarContainerItem ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarContainerItem^ AppendItemFromRebar( 	Rebar^ rebar ) ``` |

#### Parameters

rebar
:   Type:  [Autodesk.Revit.DB.Structure Rebar](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)    
     The Rebar.

#### Return Value

The Rebar Container Item.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The RebarShape of rebar has End Treatments -or- Can't create container from free-form rebar. -or- Can't create container from Rebar with moved bars. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)