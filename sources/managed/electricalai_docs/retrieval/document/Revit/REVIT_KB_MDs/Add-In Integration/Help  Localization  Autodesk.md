---
created: 2026-01-28T20:38:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Localization | Autodesk

> ## Excerpt
> You can let Revit localize the user-visible resources of an external command button (including Text, large icon image, long and short descriptions and tooltip image). You will need to create a .NET Satellite DLL which contains the strings, images, and icons for the button. Then change the values of the tags in the .addin file to correspond to the names of resources in the Satellite dll, but prepended with the @character. So the tag:

---
You can let Revit localize the user-visible resources of an external command button (including Text, large icon image, long and short descriptions and tooltip image). You will need to create a .NET Satellite DLL which contains the strings, images, and icons for the button. Then change the values of the tags in the .addin file to correspond to the names of resources in the Satellite dll, but prepended with the @character. So the tag:

<table summary="" id="GUID-74C35C7C-22E8-4F7F-844F-E602EF45CFA2__TABLE_A672A867F2EC487D938423194AB939BC"><tbody><tr><td><b>Code Region 3-13: Non-localized Text Entry</b></td></tr><tr><td><p><code>&lt;Text&gt;Extension Manager&lt;/Text&gt;</code></p></td></tr></tbody></table>

Becomes:

<table summary="" id="GUID-74C35C7C-22E8-4F7F-844F-E602EF45CFA2__TABLE_5A9C1C832A7145C580EA9EF5E4801E3F"><tbody><tr><td><b>Code Region 3-14: Localized Text Entry</b></td></tr><tr><td><p><code>&lt;Text&gt;@ExtensionText&lt;/Text&gt;</code></p></td></tr></tbody></table>

where ExtensionText is the name of the resource found in the Satellite DLL.

The Satellite DLLs are expected to be in a directory with the name of the language of the language-culture, such as en or en-US. The directory should be located in the directory that contains the add-in assembly. See [http://msdn.microsoft.com/en-us/library/e9zazcx5.aspx](http://msdn.microsoft.com/en-us/library/e9zazcx5.aspx) to create managed Satellite DLLs.

You can force Revit to use a particular language resource DLL, regardless of the language of the Revit session, by specifying the language and culture explicitly with a LanguageType tag.

<table summary="" id="GUID-74C35C7C-22E8-4F7F-844F-E602EF45CFA2__TABLE_23FF102C3FC84D028B44DAB25A7453EF"><tbody><tr><td><b>Code Region 3-15: Using LanguageType Tag</b></td></tr><tr><td><p><code>&lt;LanguageType&gt;English_USA&lt;/LanguageType&gt;</code></p></td></tr></tbody></table>

For example, the entry above would force Revit to always load the values from the en-US Satellite DLL and to ignore the current Revit language and culture settings when considering the localizable members of the external command manifest file.

Revit supports the 11 languages defined in the Autodesk.Revit.ApplicationServices.LanguageType enumerated type: English\_USA, German, Spanish, French, Italian, Dutch, Chinese\_Simplified, Chinese\_Traditional, Japanese, Korean, and Russian.
