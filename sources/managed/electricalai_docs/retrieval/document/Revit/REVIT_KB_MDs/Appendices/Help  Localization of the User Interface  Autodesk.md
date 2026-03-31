---
created: 2026-01-28T21:27:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_Localization_of_the_User_Interface_html
author: 
---

# Help | Localization of the User Interface | Autodesk

> ## Excerpt
> If you plan to localize the user interface into languages other than English, be aware of the space requirements.

---
If you plan to localize the user interface into languages other than English, be aware of the space requirements.

The English language is very compact, so translated text usually ends up taking up more space (30% on average for longer strings, 100% or more on short strings (a word or short phrase)). This can present problems if translated text is inserted into dialog boxes that were designed for an English product, because there is not usually sufficient space in available to fit the translated text. The common solution to this problem is to resize the dialog box so that the translated text fits properly, but most times this isn't the best solution.

Instead, by careful design of the dialog box by the developer, the same dialog box resource can be used for most if not all languages without the need for costly and time-consuming re-engineering. This paper tells you how to design 'global' dialog boxes.

These following design rules must be adhered to at all times to prevent globalization and localization problems.

-   The English dialog must be at least 30% smaller than the minimum screen size specified by the product.
    
-   A dialog must be designed with the following amounts of expansion in mind. This amount of extra space should look good in English and avoid resizing for most localization.
    

```
   <table cellpadding="4" cellspacing="0" summary="" class="table" frame="border" border="1" rules="all">
```

**CHARACTERS** **PERCENTAGE** 1-5 characters 100% 6-10 characters 40% 11-100 characters 30% 100 characters or greater 20%

-   Make the invisible control frame around text controls, frames etc. as large as possible to allow for longer translated text. These frames should be at least 30% larger than the English text.

Refer to the [User Interface Text Guidelines for Microsoft Windows User Experience Guidelines](http://msdn.microsoft.com/en-us/library/aa974176.aspx#globallocal#globallocal) for additional information regarding localizing text.
