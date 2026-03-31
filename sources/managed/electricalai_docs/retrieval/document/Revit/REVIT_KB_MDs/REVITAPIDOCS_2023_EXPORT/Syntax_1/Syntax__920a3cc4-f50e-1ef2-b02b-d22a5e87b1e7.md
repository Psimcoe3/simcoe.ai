[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RevitLinkOptions Constructor (Boolean, WorksetConfiguration)

---



|  |
| --- |
| [RevitLinkOptions Class](3f710983-5a4d-d515-a633-12b06a419b30.htm)   [See Also](#seeAlsoToggle) |

Creates a RevitLinkOptions object, specifying relative or absolute path type, and the desired workset configuration.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public RevitLinkOptions( 	bool relative, 	WorksetConfiguration config ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	relative As Boolean, _ 	config As WorksetConfiguration _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RevitLinkOptions( 	bool relative,  	WorksetConfiguration^ config ) ``` |

#### Parameters

relative
:   Type:  System Boolean    
     True if the link should use a relative path. False if it should use an absolute path.

config
:   Type:  [Autodesk.Revit.DB WorksetConfiguration](eefef6f4-0892-4bb5-8840-5e99aebc65c9.htm)    
     A WorksetConfiguration object specifying the worksets to open when creating the link. Leave as    a null reference (  Nothing  in Visual Basic)  if the file is not workshared. Optionally, this may also be    a null reference (  Nothing  in Visual Basic)  for a workshared file, in which case Revit will open all worksets.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RevitLinkOptions Class](3f710983-5a4d-d515-a633-12b06a419b30.htm)

[RevitLinkOptions Overload](5efd776b-eac8-915a-a770-c87cf47e64be.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)