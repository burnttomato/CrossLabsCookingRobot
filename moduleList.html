# Modules List

This file contains a list of the modules that are planned to be used for the cooking robot. Each module will include parameters, example uses, and any notes that may arise from development and testing. All modules are transcribed from the following, updated [Google Sheets file](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiipvisSo2z4f8iZjyYw6rBdNm7CZ88OOkHevlUx89v0vSZdrDpnFXYAgNjMbJz3S_jCeZckYI0xPF/pubhtml?gid=9782156&single=true&widget=true&headers=false#), which may be more updated than this file.

**Table of Contents**

- [Modules List](#modules-list)
  - [`transfer(item, container)`](#transferitem-container)
    - [Parameters](#parameters)
    - [Examples](#examples)
  - [`blend(items)`](#blenditems)
    - [Parameters](#parameters-1)
    - [Examples](#examples-1)
    - [Notes](#notes)
  - [`garnish(item, container)`](#garnishitem-container)
    - [Parameters](#parameters-2)
    - [Examples](#examples-2)
    - [Notes](#notes-1)
  - [`muddle(ingredient)`](#muddleingredient)
    - [Parameters](#parameters-3)
    - [Examples](#examples-3)
    - [Notes](#notes-2)
  - [`fill(ingredient, container)`](#fillingredient-container)
    - [Parameters](#parameters-4)
    - [Examples](#examples-4)
  - [`stir(container)`](#stircontainer)
    - [Parameters](#parameters-5)
    - [Examples](#examples-5)
    - [Notes](#notes-3)
  - [`shake(time)`](#shaketime)
    - [Parameters](#parameters-6)
    - [Examples](#examples-6)
  - [`strain(container_from, container_to)`](#straincontainer_from-container_to)
    - [Parameters](#parameters-7)
    - [Examples](#examples-7)
  - [`chill(item)`](#chillitem)
    - [Parameters](#parameters-8)
    - [Examples](#examples-8)
  - [`squeeze(ingredient, container)`](#squeezeingredient-container)
    - [Parameters](#parameters-9)
    - [Examples](#examples-9)
  - [`discard(item)`](#discarditem)
    - [Parameters](#parameters-10)
    - [Examples](#examples-10)
  - [`twist(container, ingredient)`](#twistcontainer-ingredient)
    - [Parameters](#parameters-11)
    - [Examples](#examples-11)
    - [Notes](#notes-4)
  - [`express(ingredient, container)`](#expressingredient-container)
    - [Parameters](#parameters-12)
    - [Examples](#examples-12)
    - [Notes](#notes-5)
  - [`cut_wedge(ingredient)`](#cut_wedgeingredient)
    - [Parameters](#parameters-13)
    - [Examples](#examples-13)
  - [`serve()`](#serve)
    - [Examples](#examples-14)
    - [Notes](#notes-6)

## `transfer(item, container)`

`transfer` is a module that is the general term for transferring an item to a container. This is a function that can encompass the equivalent of "pour", "add", and other instructions in recipes that may instruct the reader to add something into a container.

### Parameters

- `item` - the item to be transferred
- `container` - the container that the item will be transferred to

### Examples

In a situation where the recipe may read:

```
Add the ice to the glass
```

The LLM may respond with:

```py
transfer("ice", "glass")
```

## `blend(items)`

`blend` is a module that will blend items together in a blender. This will internally call the `transfer` module to transfer items into the blender. Timings for how long to use the blender are currently not determined, but as of now ingredients will blend for a set period of time (such as 30 seconds).

### Parameters

- `items` - a list of items to be blended together in the blender

### Examples

In a situation where the recipe may read:

```
Blend the berries and ice until they are smooth.
```

The LLM may respond with:

```py
blend(["berries", "ice"])
```

### Notes

Timings are currently undetermined. Certain recipes will specify a certain amount of time to blend ingredients while others will just state "blend until smooth." More discussion and thought will be needed to understand and know how to work around the differences in recipes such as these.

## `garnish(item, container)`

`garnish` will garnish the cocktail by placing the item on the rim of the container.

### Parameters

- `item` - the item or ingredient that will be used to garnish the cocktail
- `container` - the container that the cocktail is presumably in or will be held in

### Examples

In a situation where the recipe may read:

```
Garnish the glass with the wedge of lime.
```

The LLM may respond with:

```py
garnish("wedge of lime", "glass")
```

### Notes

Some garnishes won't balance on a rim, or are meant to be placed directly in the drink. Careful consideration will need to be made to account for these differences.

## `muddle(ingredient)`

`muddle` is a module that will crush an ingredient with a muddle, a spoon, or a blunt tool.

### Parameters

- `ingredient` - the ingredient to be muddled

### Examples

In a situation where the recipe may read:

```
Muddle the limes
```

The LLM may respond with:

```py
muddle("lime")
```

### Notes

Muddling is usually done in a glass, which means that one has to be careful not to use too much pressure to break the glass. In addition, if this LLM is to be applicable to any and all recipes, the location or container of the muddling may also need to be a parameter.

## `fill(ingredient, container)`

`fill` is similar to `transfer`, but the condition for stopping will be until the container is full.

### Parameters

- `ingredient` - the ingredient to fill the container with
- `container` - the container that is to be filled, such as a glass

### Examples

In a situation where the recipe may read:

```
Top off the glass with lemonade.
```

The LLM may respond with:

```py
fill("lemonade", "glass")
```

## `stir(container)`

`stir` is a function that simply instructs the robot to stir the ingredients inside of a container.

### Parameters

- `container` - the container with the ingredients that needs to be stirred or mixed

### Examples

In a situation where the recipe reads:

```
After adding the juice and ice to the glass, stir before serving.
```

The LLM may respond with:

```py
transfer("juice", "glass")
transfer("ice", "glass")
stir("glass")
```

### Notes

Sometimes recipes may call for different intensities of stirring as well as different timings for when to stop stirring. This may or may not need to be accounted for given priorities.

## `shake(time)`

`shake` will shake the shaker with (presumably) the ingredients inside the shaker.

### Parameters

- `time` - the number of seconds that the robot should shake the shaker for

### Examples

In a situation where the recipe reads:

```
Put the ingredients into the shaker with ice and shake for 30 seconds.
```

The LLM may respond with:

```py
transfer("ingredients", "shaker")
transfer("ice", "shaker")
shake(30)
```

## `strain(container_from, container_to)`

`strain` will instruct the robot to strain the contents of one container to another container.

### Parameters

- `container_from` - the container from which the unstrained ingredients are originally stored
- `container_to` - the container to which the ingredients will strained to

### Examples

In a situation where the recipe reads:

```
Strain the shaker into the serving glass.
```

The LLM may respond with:

```py
strain("shaker", "serving glass")
```

## `chill(item)`

`chill` is a module that will chill the item, which can be either a container or an ingredient.

### Parameters

- `item` - the item to be chilled. This can either be a container like a glass or an ingredient

### Examples

In a situation where the recipe reads:

```
Pour the drink into a chilled glass.
```

The LLM may respond with:

```py
chill("glass")
transfer("drink", "glass")
```

## `squeeze(ingredient, container)`

`squeeze` is a module called when some ingredient needs to be squeezed over a container.

### Parameters

- `ingredient` - the ingredient to be squeezed, such as a lemon
- `container` - the container to squeeze into, such as a glass

### Examples

In a situation where the recipe reads:

```
Squeeze a lemon into the glass.
```

The LLM may respond with:

```py
squeeze("lemon", "glass")
```

## `discard(item)`

`discard` is used to throw away items, and is common in recipes to denote that the leftovers of a certain ingredient are not to be used.

### Parameters

- `item` - the item to be discarded

### Examples

In a situation where the recipe reads:

```
Squeeze the lime into the shaker and discard the rind.
```

The LLM may respond with:

```py
squeeze("lime", "shaker")
discard("rind")
```

## `twist(container, ingredient)`

`twist` is a module that is used when the rim of something (usually a glass) is to be decorated with an ingredient such as sugar.

### Parameters

- `container` - the container, usually a glass, that is to be twisted
- `ingredient` - the ingredient to twist the container on

### Examples

In a situation where the recipe reads:

```
Twist the chilled glass over the sugar.
```

The LLM may repond with:

```py
chill("glass")
transfer("drink", "glass")
```

### Notes

Unfortunately, twist is also a term used for twisting a peel, which may cause complications and confusions with the LLM.

## `express(ingredient, container)`

`express` is a module that twists an ingredient over a container, similar to squeezing an ingredient over a container.

### Parameters

- `ingredient` - the ingredient to twist
- `container` - the container to twist the ingredient over

### Examples

In a situation where the receipe reads:

```
Twist the orange peel into your cup.
```

The LLM may respond with:

```py
express("orange peel", "cup")
```

### Notes

"Express" is the official term for twisting an ingredient, since `twist` is already a module.

## `cut_wedge(ingredient)`

`cut_wedge` is a module to cut an ingredient into a wedge, a common action that is used in cocktail recipes.

### Parameters

- `ingredient` - the ingredient to be cut into a wedge

### Examples

In a situation where the recipe may read:

```
Garnish the glass with a wedge of fresh lemon.
```

The LLM may respond with:

```py
cut_wedge("lemon")
garnish("glass", "wedge of lemon")
```

## `serve()`

`serve` is the module used to place the finished product in the serving area, indicating the end of the recipe.

### Examples

In a situation where the recipe may say:

```
And there you have it; serve and enjoy!
```

The LLM may respond with:

```py
serve()
```

### Notes

This module will be automatically called at the end of every recipe, whether explicitly stated or not. This will require the robot/program to remember what the last container (i.e. "serving glass") was in order to serve it.
