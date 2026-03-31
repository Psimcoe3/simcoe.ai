[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAssociatedFamilyParameter Method

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

Gets the associated family parameter of an element parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyParameter GetAssociatedFamilyParameter( 	Parameter elementParameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAssociatedFamilyParameter ( _ 	elementParameter As Parameter _ ) As FamilyParameter ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyParameter^ GetAssociatedFamilyParameter( 	Parameter^ elementParameter ) ``` |

#### Parameters

elementParameter
:   Type:  [Autodesk.Revit.DB Parameter](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)    
     The parameter of an element in family.

#### Return Value

The associated family parameter if there is an association between them, returns    a null reference (  Nothing  in Visual Basic)  if not.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"elementParameter"-is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)