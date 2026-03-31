[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFormByCap Method

---



|  |
| --- |
| [FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)   [See Also](#seeAlsoToggle) |

Create new Form element by cap operation (to create a single-surface form), and add it into the Autodesk Revit family document.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Form NewFormByCap( 	bool isSolid, 	ReferenceArray profile ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFormByCap ( _ 	isSolid As Boolean, _ 	profile As ReferenceArray _ ) As Form ``` |

 

| Visual C++ |
| --- |
| ``` public: Form^ NewFormByCap( 	bool isSolid,  	ReferenceArray^ profile ) ``` |

#### Parameters

isSolid
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Indicates if the Form is Solid or Void.

profile
:   Type:  [Autodesk.Revit.DB ReferenceArray](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)    
     The profile of the newly created cap. It should consist of only one curve loop.

#### Return Value

If creation was successful new form is returned.

# See Also

[FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)