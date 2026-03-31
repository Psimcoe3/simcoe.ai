[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFamilyDocument Method

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

New family document, including family, titleblock, and annotation symbol

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Document NewFamilyDocument( 	string templateFileName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function NewFamilyDocument ( _ 	templateFileName As String _ ) As Document ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual Document^ NewFamilyDocument( 	String^ templateFileName ) ``` |

#### Parameters

templateFileName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The template file name.

# Remarks

This command corresponds to File->New->Family.../TitleBlock.../Annotation Symbol....

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// create a new family document using Generic Model.rft template
string templateFileName = @"C:\Documents and Settings\All Users\Application Data\Autodesk\RST 2010\Imperial Templates\Generic Model.rft";
Document familyDocument = application.NewFamilyDocument(templateFileName);
if (null == familyDocument)
{
    throw new Exception("Cannot open family document");
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' create a new family document using Generic Model.rft template
Dim templateFileName As String = "C:\Documents and Settings\All Users\Application Data\Autodesk\RST 2010\Imperial Templates\Generic Model.rft"
Dim familyDocument As Document = application.NewFamilyDocument(templateFileName)
If familyDocument Is Nothing Then
    Throw New Exception("Cannot open family document")
End If
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | If 'templateFileName' is    a null reference (  Nothing  in Visual Basic)  or an empty string. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | If the new family document cannot be created. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)