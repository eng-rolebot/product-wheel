[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# Product-Wheel <img align="right" img src="https://github.com/eng-rolebot/product-wheel/blob/master/images/logo.png" width="200">
UW Capstone project 2020



## Background
-----------
Product Wheel is the name of a production planning method used in many industries where multiple types of products are made on a single manufacturing line of equipment. 

Implementing the Product Wheel helps to schedule the manufacturing process with a standard production sequence. It helps to eliminate frequent repetition of low volume products and simplifies changeovers so that throughput increases, inventory stock decreases, and product delivery performance increases. In addition, having standard patterns and predictable inventory requirements dramatically reduce the number of rush jobs to be scheduled, and provide the schedulers more bandwidth to manage the rush orders that do come in. 

<img align="right" img src="https://github.com/eng-rolebot/product-wheel/blob/master/images/product-wheel-image.png?raw=true">

Despite these many benefits, Product Wheel design, in reality, is often not optimal. Manufacturers may use old-established principles, that may not be robust enough. 

In this project, we will try to apply Machine Learning methods to evaluate effects of different input process parameters on a chemical manufacturing of a product with codename "Corian", in order to optimize Product Wheel, minimize the amount of scrap material during product types changeover, and reduce production cost as a result.

* *Image source: http://www.leandynamics.us/product_wheels*

## Project Introduction 
-----------
To put the phrase "Product Wheel" in a more reatlistic approach, one must define the overall product wheel cost. It is composed of two major costs, the annual transition cost and the average inventory carrying cost. Both in which affects one another. However, since the average inventory carrying cost isn't provided, the product wheel will be optimized from the perspective of annual transition cost.
   
In a product wheel, there are multiple campaigns that are interconnected,such as A->B->C->D->A->B->C->D, etc.  Campaign A's inventory must be able to sustain through the whole cycle until the next A campaign is reached. In between campaigns, there are transition costs. It is crucial to minimize the transition cost by manipulating factors. In the context of Corians, the transition time could fluctuate depend on factors such as number of sheets processed, the production rate, the machine downtime, the labor, and the demand rate. It could also depend on factors that are more associated to the corian product itself, such as color, the sheets dimensions, the material's durability, and the variation in temperature or other parameters for different corians. By applying appropriate machine learning methods, the production wheel length can be minimized by creating the most profitable algorithms that can manipulate the factors mentioned above. With a shorter product wheel, the production line will be able to maximize responsiveness with regard to changes from a standpoint of customer demand,  while lowering the inventory cost at the same time. 

The potential users for this algorithm could be any production engineer, from any company, that is in seek of to optimizing the efficieny of the production line. The primary use case is to minimize product wheel cost at SKU level within supplied constraints by optimizing transition cost. In terms of stretch use cases, it would be ideal to explore more factors that weren't explored, such as technical maintenance, lead time uncertainty, policies, batch sizes, and sales constraints. For now, Wesley from MFG Analytics provided approximately 4189 rows of labeled data, which is sufficient in kicking off the project. Hopefully, more data would be given as the project moves forward. 


## Structure

```
|-Licence

|-README

|-.gitignore

|-images

  |-DIRECTlogo-Final.png
  
  |-logo.png
  
  |-Signature_Center_Purple_RGB.png
  
|-.travis.yml


```

## Instructions
-----------
### Dependencies:

## Data Dependencies

## Running the nosetests
-----------

## Use Case: Example 
-----------
## The result of the model

## Future work
-----------
Right now we only use transition time as well as transition sheet as our standard for the annual transition cost and  we only have limited datasets and lack the data of the inventory carrying costs. So in the future, we might consider more factors to determine the annual transition cost. Besides, we hope we can obtain more data from companies and the inventory carrying costs to achieve the total product wheel cost.

## Acknowledgements
-----------


<img align="center" img src="https://github.com/eng-rolebot/product-wheel/blob/master/images/DIRECTlogo-Final.png?raw=true" width="300"> <img align="center" img src="https://github.com/eng-rolebot/product-wheel/blob/master/images/Signature_Center_Purple_RGB.png?raw=true" width="300">
