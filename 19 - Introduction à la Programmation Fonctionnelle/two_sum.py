# Fonction récursive avec tail call (donc optimisée (pas en python hélas))
def two_sum(arr: list[int], target: int, index: int, seen: dict[int, int]) -> list[int]:
    match arr:
        case [] :
            return [-1, -1]
        case [head, *tail]:
            if target-head in seen:
                return [seen[target-head], index]
            else:
                seen[head] = index  # pas foncitonnel mais permet de ne pas copier la map sans tail call optimisation
                # la vraie solution devrait être two_sum(tail, target, index+1, seen|{head: index})
                return two_sum(tail, target, index+1, seen)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum(nums, target, 0, {})
