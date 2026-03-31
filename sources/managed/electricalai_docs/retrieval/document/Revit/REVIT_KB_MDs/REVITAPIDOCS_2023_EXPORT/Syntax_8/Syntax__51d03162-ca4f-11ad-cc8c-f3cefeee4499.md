[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ElementId)

---



|  |
| --- |
| [MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of a mechanical system and adds it to the document.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static MechanicalSystem Create( 	Document ADocument, 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	ADocument As Document, _ 	typeId As ElementId _ ) As MechanicalSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: static MechanicalSystem^ Create( 	Document^ ADocument,  	ElementId^ typeId ) ``` |

#### Parameters

ADocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where the element will be created and added.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The identifier of this mechanical system element's type.

#### Return Value

The newly created mechanical system element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The typeId is not an element id for a valid mechanical system type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.htm)

[Create Overload](8bf8c8c0-e561-6609-385f-e658e49716ac.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)