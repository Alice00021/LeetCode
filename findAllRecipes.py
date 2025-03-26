class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        result = []
        changed = True
        available = set(supplies)
        while changed:
            changed = False
            for i in range(len(recipes)):
                if recipes[i] not in result:
                    can_make = True
                    for ingredient in ingredients[i]:
                        if ingredient not in available:
                            can_make = False
                            break
                    if can_make:
                        result.append(recipes[i])
                        available.add(recipes[i])  
                        changed = True  
        
        return result
    
ex = Solution()
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
#Output: ["bread","sandwich","burger"]
print(ex.findAllRecipes(recipes,ingredients, supplies))
                
                

        