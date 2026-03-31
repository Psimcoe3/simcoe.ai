[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpenSharedParameterFile Method

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Enables access to shared parameter groups and definitions that are maintained on disk.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public DefinitionFile OpenSharedParameterFile() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function OpenSharedParameterFile As DefinitionFile ``` |

 

| Visual C++ |
| --- |
| ``` public: DefinitionFile^ OpenSharedParameterFile() ``` |

#### Return Value

An object that represents a shared parameters file that exists on disk. Returns    a null reference (  Nothing  in Visual Basic)  if the file does not exist.

# Remarks

This function is used to return an object that represents a Revit shared parameters file Revit can use only one shared parameters file at one time. The filename for the shared parameters file can be set in the Application.SharedParametersFilename property.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)