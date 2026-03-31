[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnSharedFamilyFound Method

---



|  |
| --- |
| [IFamilyLoadOptions Interface](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)   [See Also](#seeAlsoToggle) |

A method called when the shared family was found in the target document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` bool OnSharedFamilyFound( 	Family sharedFamily, 	bool familyInUse, 	out FamilySource source, 	out bool overwriteParameterValues ) ``` |

 

| Visual Basic |
| --- |
| ``` Function OnSharedFamilyFound ( _ 	sharedFamily As Family, _ 	familyInUse As Boolean, _ 	<OutAttribute> ByRef source As FamilySource, _ 	<OutAttribute> ByRef overwriteParameterValues As Boolean _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool OnSharedFamilyFound( 	Family^ sharedFamily,  	bool familyInUse,  	[OutAttribute] FamilySource% source,  	[OutAttribute] bool% overwriteParameterValues ) ``` |

#### Parameters

sharedFamily
:   Type:  [Autodesk.Revit.DB Family](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)    
     The shared family in the current family document.

familyInUse
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Indicates if one or more instances of the family is placed in the project.

source
:   Type:  [Autodesk.Revit.DB FamilySource](d8554318-b292-2a6c-590a-c2af54c49ad6.htm)   %    
     This indicates if the family will load from the project or the current family.

overwriteParameterValues
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)   %    
     This indicates whether or not to overwrite the parameter values of existing types.

#### Return Value

Return true to continue loading the family, false to cancel.

# Remarks

Triggered only when the family is both loaded and changed.

# See Also

[IFamilyLoadOptions Interface](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)