[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLabelForGroup Method

---



|  |
| --- |
| [LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)   [See Also](#seeAlsoToggle) |

Gets the user-visible name for a built-in parameter group. To get the name of parameter group "Other", pass an empty, default-constructed ForgeTypeId.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static string GetLabelForGroup( 	ForgeTypeId groupTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetLabelForGroup ( _ 	groupTypeId As ForgeTypeId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetLabelForGroup( 	ForgeTypeId^ groupTypeId ) ``` |

#### Parameters

groupTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     The identifier of the parameter group to get the user-visible name, or an empty ForgeTypeId for group "Other".

# Remarks

The name is obtained in the current Revit language.

# See Also

[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)