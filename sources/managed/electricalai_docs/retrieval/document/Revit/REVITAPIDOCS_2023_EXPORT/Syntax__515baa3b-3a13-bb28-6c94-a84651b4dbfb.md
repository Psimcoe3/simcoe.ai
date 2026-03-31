[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnFamilyFound Method

---



|  |
| --- |
| [IFamilyLoadOptions Interface](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)   [See Also](#seeAlsoToggle) |

A method called when the family was found in the target document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` bool OnFamilyFound( 	bool familyInUse, 	out bool overwriteParameterValues ) ``` |

 

| Visual Basic |
| --- |
| ``` Function OnFamilyFound ( _ 	familyInUse As Boolean, _ 	<OutAttribute> ByRef overwriteParameterValues As Boolean _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool OnFamilyFound( 	bool familyInUse,  	[OutAttribute] bool% overwriteParameterValues ) ``` |

#### Parameters

familyInUse
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Indicates if one or more instances of the family is placed in the project.

overwriteParameterValues
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)   %    
     This determines whether or not to overwrite the parameter values of existing types. The default value is false.

#### Return Value

Return true to continue loading the family, false to cancel.

# Remarks

Triggered only when the family is both loaded and changed.

# See Also

[IFamilyLoadOptions Interface](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)