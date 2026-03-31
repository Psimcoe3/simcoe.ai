[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetReferences Method

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

Gets family instance references corresponding to the reference planes or reference lines of the given reference type in the instance's family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public IList<Reference> GetReferences( 	FamilyInstanceReferenceType referenceType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetReferences ( _ 	referenceType As FamilyInstanceReferenceType _ ) As IList(Of Reference) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Reference^>^ GetReferences( 	FamilyInstanceReferenceType referenceType ) ``` |

#### Parameters

referenceType
:   Type:  [Autodesk.Revit.DB FamilyInstanceReferenceType](ab424c61-4b80-9dcd-3f9a-7b35fa670edf.htm)    
     The family reference type.

#### Return Value

Returns all the family instance references corresponding to reference planes and reference lines of the given reference type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)