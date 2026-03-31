---
created: 2026-01-28T20:42:16 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | How to use Application properties to enforce a correct version for your add-in | Autodesk

> ## Excerpt
> Sometimes you need your add-in to operate only in the presence of a particular Update Release of Revit due to the presence of specific fixes or compatible APIs.

---
Sometimes you need your add-in to operate only in the presence of a particular Update Release of Revit due to the presence of specific fixes or compatible APIs.

Properties of Application make it possible to check for specific versions of Revit. While the property VersionNumber will return a string representing the primary version number, the VersionBuild property will return the internal build number of the Autodesk Revit application.

Another useful property is the Application.SubVersionNumber property. It returns a string representing the major-minor version number for the Revit application such as "2018.0.0". This string is updated by Autodesk for all major and minor updates. Point releases (such as 2018.1.0) may have additional APIs and functionality not available in the initial customer release (such as 2018.0.0). Add-ins written to support initial releases will likely be compatible with subscription updates, but add-ins using new features in subscription updates would not be compatible with the initial releases.

The following sample code demonstrates a technique to determine if the Revit version is any Update Release after the initial known Revit release.

<table summary="" id="GUID-15B6EF8F-7B1D-4930-9F90-CC116411F398__TABLE_235B206931404F52BAE7FF73D21C21C2"><tbody><tr><td><b>Code Region: Use VersionBuild to identify if your add-in is compatible</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetVersionInfo</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app</span><span>)</span><span>
</span><span>{</span><span> 
   </span><span>// 20110309_2315 is the datecode of the initial release of Revit 2012 </span><span>
   </span><span>if</span><span> </span><span>(</span><span>app</span><span>.</span><span>VersionNumber</span><span> </span><span>==</span><span> </span><span>"2012"</span><span> </span><span>&amp;&amp;</span><span> 
       </span><span>String</span><span>.</span><span>Compare</span><span>(</span><span>app</span><span>.</span><span>VersionBuild</span><span>,</span><span> </span><span>"20110309_2315"</span><span>)</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
   </span><span>{</span><span>
       </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Supported version"</span><span>,</span><span> 
                      </span><span>"This application supported in this version."</span><span>);</span><span>
   </span><span>}</span><span>
   </span><span>else</span><span>
   </span><span>{</span><span>
       </span><span>TaskDialog</span><span> dialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Unsupported version."</span><span>);</span><span>
       dialog</span><span>.</span><span>MainIcon</span><span> </span><span>=</span><span> </span><span>TaskDialogIcon</span><span>.</span><span>TaskDialogIconWarning</span><span>;</span><span>
       dialog</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>"This Revit 2012 application is supported in UR1 and later releases."</span><span>;</span><span>
       dialog</span><span>.</span><span>Show</span><span>();</span><span>
   </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></tbody></table>
