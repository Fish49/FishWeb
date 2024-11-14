# FishWeb
Web development is hard, so Im gonna try and make my own web (just for fun).  
hopefully it will be easier (at least for me because i made it)  

## The Plan:
my plan is to create a version of the web thats more simple, intuitive, and powerful. if used Svelte before and liked the reactivity, so i plan to have reactivity built right in, just like svelte.

## Styling
### Scaling:
the main idea with syles is element scale. elements can either:
- fit in the parent, in which case they will need an aspect ratio
- fill the parent
- wrap around their children
- have a constant size (not constant per se, but just not automatically derived from children or parents)

if the parent depends on the child, then the child cannot depend on the parent and vice versa.  
if the child depends on its children or is constant, and the parent depends on its parent or is constant, there must be alignment rules.  

### Box Model
just like in CSS, elements will have margins, borders, and padding.  
images can be set to stretch, fill, fit, or dictate (the latter of which will automatically set the aspect ratio)  

### Position
object position depends on context and pack. context describes the element it is positioned relative to. pack asks if it reserves space in the parent.  
context is one of the following:  
- parent (packed directly into the parent without considering siblings)
- fake-parent (the default, packs into parent naturally, taking into account siblings)
- page (relative to the page, moves when you scroll)
- screen (relative to the screen, stays fixed no matter what)

### Alignment
alignment comes in two parts, origin and box alignment.  
the origin point describes the location of the element relative to its parent. it descibes the point around which post processing effects like rotation occur.  
the box alignment describes where the box shows up relative to the origin.  
the default for both is top-left, which means that by default, the box will snugly fit in the top-left corner of its parent.  
examples:  
![image](/readmefiles/alignment-examples.png)